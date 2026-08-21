#!/usr/bin/env python3
import os, re, sys, json, hashlib, html, unicodedata, shutil, subprocess
from pathlib import Path
from collections import OrderedDict
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, SimpleDocTemplate, PageTemplate, Frame, Paragraph,
    Spacer, PageBreak, Table, TableStyle, KeepTogether, Flowable, HRFlowable)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import fitz
from pypdf import PdfReader, PdfWriter

SRC = Path(os.environ.get('GREEK_SRC','oral/100-crucial-questions/answers/revision-v3-el'))
OUT = Path(os.environ.get('GREEK_OUT','build_greek'))
OUT.mkdir(parents=True, exist_ok=True)
SOURCE_COMMIT=os.environ.get('SOURCE_COMMIT','63a844d881072d13fd6e33423b9e01fb8f91f0d9')
BOOK_TITLE='100 ΚΑΙΡΙΕΣ ΕΡΩΤΗΣΕΙΣ ΣΤΗΝ ΨΥΧΙΑΤΡΙΚΗ'
PDF_TITLE='100 Καίριες Ερωτήσεις στην Ψυχιατρική'

# fonts
FONT_DIR=Path('/usr/share/fonts/truetype/noto')
font_paths={
 'Serif':FONT_DIR/'NotoSerif-Regular.ttf','SerifB':FONT_DIR/'NotoSerif-SemiBold.ttf',
 'Sans':FONT_DIR/'NotoSans-Regular.ttf','SansM':FONT_DIR/'NotoSans-Medium.ttf',
 'SansB':FONT_DIR/'NotoSans-SemiBold.ttf','Math':FONT_DIR/'NotoSansMath-Regular.ttf'}
for k,p in font_paths.items():
    if not p.exists(): raise SystemExit(f'Missing font {p}')
    pdfmetrics.registerFont(TTFont(k,str(p)))
pdfmetrics.registerFontFamily('SerifFam',normal='Serif',bold='SerifB')
pdfmetrics.registerFontFamily('SansFam',normal='Sans',bold='SansB')

BLUE=HexColor('#314C63'); TEXT=HexColor('#202326'); MID=HexColor('#6D737A')
LIGHT=HexColor('#F3F1ED'); RULE=HexColor('#C8D0D6'); PALE=HexColor('#F7F8F9')
PAGE_W,PAGE_H=A4
INNER=36*mm; OUTER=32*mm; TOP=22*mm; BOTTOM=22*mm
BODY_W=PAGE_W-INNER-OUTER

styles={
 'eyebrow':ParagraphStyle('eyebrow',fontName='SansB',fontSize=9.2,leading=11.2,textColor=BLUE,spaceAfter=10),
 'title':ParagraphStyle('title',fontName='SerifB',fontSize=16.5,leading=20.0,textColor=TEXT,spaceAfter=5),
 'section':ParagraphStyle('section',fontName='SansB',fontSize=9.25,leading=11.2,textColor=BLUE,spaceBefore=12,spaceAfter=7),
 'body':ParagraphStyle('body',fontName='Serif',fontSize=10.25,leading=14.25,textColor=TEXT,spaceAfter=8,allowWidows=1,allowOrphans=1),
 'bullet':ParagraphStyle('bullet',fontName='Serif',fontSize=10.05,leading=13.8,textColor=TEXT,leftIndent=13,firstLineIndent=-9,spaceAfter=4,bulletIndent=0),
 'spine':ParagraphStyle('spine',fontName='SansB',fontSize=9.45,leading=12.1,textColor=TEXT,spaceAfter=0),
 'spinenum':ParagraphStyle('spinenum',fontName='SansM',fontSize=9.45,leading=12.1,textColor=BLUE,spaceAfter=0),
 'followq':ParagraphStyle('followq',fontName='SerifB',fontSize=12.7,leading=16.2,textColor=TEXT,spaceAfter=8),
 'followlabel':ParagraphStyle('followlabel',fontName='SansB',fontSize=8.7,leading=10.5,textColor=BLUE,spaceBefore=12,spaceAfter=5),
 'small':ParagraphStyle('small',fontName='Sans',fontSize=8.3,leading=10.5,textColor=MID),
 'toc':ParagraphStyle('toc',fontName='Serif',fontSize=8.55,leading=11.0,textColor=TEXT),
 'tocn':ParagraphStyle('tocn',fontName='SansB',fontSize=8.2,leading=11.0,textColor=BLUE),
}

SYMBOLS=re.compile(r'([→≥≤≠−])')
def rich(s):
    s=html.escape(s.strip(), quote=False)
    # markdown emphasis
    s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)',r'<i>\1</i>',s)
    s=SYMBOLS.sub(r'<font name="Math">\1</font>',s)
    return s

def plain_md(s):
    s=re.sub(r'\*\*(.+?)\*\*',r'\1',s)
    s=re.sub(r'(?<!\w)\*([^*]+?)\*(?!\w)',r'\1',s)
    return s.strip()

def git_blob_sha(data:bytes):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

class TaggedParagraph(Paragraph):
    def __init__(self,text,style,tag=None,label=None,**kw):
        self._tag=tag; self._label=label
        super().__init__(text,style,**kw)

class BookDoc(BaseDocTemplate):
    def __init__(self,filename,opener_pages=None,page_q=None,collect=False,**kw):
        super().__init__(filename,pagesize=A4,**kw)
        self.collect=collect; self.qstarts=OrderedDict(); self.followups=[]
        self.opener_pages=set(opener_pages or []); self.page_q=page_q or {}
        odd=Frame(INNER,BOTTOM,BODY_W,PAGE_H-TOP-BOTTOM,id='oddframe',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
        even=Frame(OUTER,BOTTOM,BODY_W,PAGE_H-TOP-BOTTOM,id='evenframe',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
        po=PageTemplate('Odd',[odd],onPage=self._page); pe=PageTemplate('Even',[even],onPage=self._page)
        po.autoNextPageTemplate='Even'; pe.autoNextPageTemplate='Odd'
        self.addPageTemplates([po,pe])
    def afterFlowable(self,f):
        if isinstance(f,TaggedParagraph) and f._tag:
            if f._tag.startswith('QMAIN:'):
                q=int(f._tag.split(':')[1]); self.qstarts[q]=self.page
                self.canv.bookmarkPage(f'q{q:03d}'); self.canv.addOutlineEntry(f._label,f'q{q:03d}',level=0,closed=False)
            elif f._tag.startswith('FOLLOW:'):
                key=f._tag.split(':',1)[1]; dest='f_'+re.sub(r'\W+','_',key)
                self.followups.append((key,self.page,f._label)); self.canv.bookmarkPage(dest); self.canv.addOutlineEntry(f._label,dest,level=1,closed=False)
    def _page(self,c,doc):
        p=doc.page; odd=p%2==1
        c.saveState()
        c.setFillColor(MID); c.setFont('Sans',8.2)
        # outside folio
        if odd: c.drawRightString(PAGE_W-OUTER,12.5*mm,str(p))
        else: c.drawString(OUTER,12.5*mm,str(p))
        if p not in self.opener_pages:
            q=self.page_q.get(p)
            c.setFillColor(BLUE); c.setFont('SansB',7.4)
            if odd:
                c.drawString(INNER,PAGE_H-12.5*mm,BOOK_TITLE)
                if q: c.drawRightString(PAGE_W-OUTER,PAGE_H-12.5*mm,f'Q{q}')
            else:
                if q: c.drawString(OUTER,PAGE_H-12.5*mm,f'Q{q}')
                c.drawRightString(PAGE_W-INNER,PAGE_H-12.5*mm,BOOK_TITLE)
            c.setStrokeColor(RULE); c.setLineWidth(.35); c.line(OUTER if not odd else INNER,PAGE_H-15*mm,PAGE_W-(INNER if not odd else OUTER),PAGE_H-15*mm)
        c.restoreState()

def read_questions():
    files=sorted(SRC.glob('Q[0-9][0-9][0-9].md'))
    if len(files) not in (1,100): raise RuntimeError(f'Expected 100 sources, found {len(files)}')
    qs=[]
    for f in files:
        txt=f.read_text(encoding='utf-8')
        lines=txt.splitlines()
        m=re.match(r'#\s+Q(\d+)\.\s+(.*)',lines[0])
        if not m: raise RuntimeError(f'Bad title {f}')
        q=int(m.group(1)); title=m.group(2).strip()
        sections=[]; cur=None
        for line in lines[1:]:
            if line.startswith('## '):
                cur={'heading':line[3:].strip(),'lines':[]}; sections.append(cur)
            elif cur is not None: cur['lines'].append(line)
        qs.append({'q':q,'title':title,'sections':sections,'path':str(f),'sha':git_blob_sha(f.read_bytes()),'bytes':f.stat().st_size})
    return qs

def blocks(lines):
    out=[]; buf=[]
    def flush():
        nonlocal buf
        if buf: out.append(('p',' '.join(x.strip() for x in buf))); buf=[]
    for ln in lines:
        if ln.startswith('### '): flush(); out.append(('h3',ln[4:].strip()))
        elif re.match(r'^\s*[-•]\s+',ln): flush(); out.append(('bullet',re.sub(r'^\s*[-•]\s+','',ln)))
        elif re.match(r'^\s*\d+\.\s+',ln): flush(); out.append(('num',re.sub(r'^\s*\d+\.\s+','',ln)))
        elif ln.strip()=='': flush()
        else: buf.append(ln)
    flush(); return out

def section_kind(h):
    hlow=h.lower()
    if 'άξονας ανάκλησης' in hlow: return 'recall'
    if 'πρότυπη προφορική' in hlow: return 'model'
    if 'βασικά σημεία' in hlow: return 'facts'
    if 'ερωτήσ' in hlow and 'εξεταστ' in hlow: return 'follow'
    if 'παγίδ' in hlow: return 'traps'
    if 'σύγχρονη πρακτική' in hlow or 'τρέχουσα πρακτική' in hlow: return 'current'
    if 'ιστορικ' in hlow or 'κλασικ' in hlow: return 'historical'
    return 'generic'

def section_label(kind,h):
    mapping={'recall':'ΑΞΟΝΑΣ ΑΝΑΚΛΗΣΗΣ','model':'ΠΡΟΤΥΠΗ ΠΡΟΦΟΡΙΚΗ ΑΠΑΝΤΗΣΗ','facts':'ΒΑΣΙΚΑ ΣΗΜΕΙΑ ΓΙΑ ΤΙΣ ΕΞΕΤΑΣΕΙΣ',
      'follow':'ΕΡΩΤΗΣΕΙΣ ΕΞΕΤΑΣΤΗ','traps':'ΣΥΧΝΕΣ ΠΑΓΙΔΕΣ / ΠΑΓΙΔΕΣ ΕΞΕΤΑΣΤΗ','current':'ΑΠΑΝΤΗΣΗ ΕΞΕΤΑΣΕΩΝ VS ΣΥΓΧΡΟΝΗ ΠΡΑΚΤΙΚΗ',
      'historical':'ΙΣΤΟΡΙΚΟ ΣΤΟΙΧΕΙΟ ΕΞΕΤΑΣΕΩΝ'}
    return mapping.get(kind,h.upper())

def historical_box(blks):
    elems=[]
    for typ,txt in blks:
        if typ in ('p','bullet','num'):
            if typ=='p': elems.append(Paragraph(rich(txt),styles['body']))
            else: elems.append(Paragraph('• '+rich(txt),styles['bullet']))
    box=Table([[elems]],colWidths=[BODY_W],hAlign='LEFT')
    box.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PALE),('BOX',(0,0),(-1,-1),0.35,RULE),('LINEBEFORE',(0,0),(0,-1),2.0,BLUE),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    return box

def traps_box(blks):
    elems=[]
    for typ,txt in blks:
        if typ in ('bullet','num'): elems.append(Paragraph('• '+rich(txt),styles['bullet']))
        elif typ=='p': elems.append(Paragraph(rich(txt),styles['body']))
    box=Table([[elems]],colWidths=[BODY_W],hAlign='LEFT')
    box.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),LIGHT),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
    return box

def build_story(qs):
    story=[]
    for qi,q in enumerate(qs):
        if qi: story.append(PageBreak())
        story.append(TaggedParagraph(f'ΕΡΩΤΗΣΗ {q["q"]}',styles['eyebrow'],tag=f'QMAIN:{q["q"]}',label=f'Q{q["q"]}. {q["title"]}'))
        story.append(Paragraph(rich(q['title']),styles['title']))
        story.append(Spacer(1,3.2*mm))
        # blue title rule
        story.append(HRFlowable(width='100%',thickness=0.8,color=BLUE,spaceBefore=0,spaceAfter=4.3*mm))
        for sec in q['sections']:
            kind=section_kind(sec['heading']); blks=blocks(sec['lines'])
            if kind=='recall':
                story.append(Paragraph(section_label(kind,sec['heading']),styles['section']))
                nums=[]
                # the parser removes numeric labels, so enumerate num blocks
                for typ,txt in blks:
                    if typ=='num': nums.append(txt)
                    elif typ=='p' and txt: nums.append(txt)
                data=[]
                for i,txt in enumerate(nums,1):
                    data.append([Paragraph(str(i),styles['spinenum']),Paragraph(rich(txt),styles['spine'])])
                if data:
                    tab=Table(data,colWidths=[12*mm,BODY_W-12*mm],hAlign='LEFT')
                    tab.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),1.2),('BOTTOMPADDING',(0,0),(-1,-1),1.2),('LINEBEFORE',(1,0),(1,-1),0.45,RULE)]))
                    story.append(tab); story.append(Spacer(1,3*mm))
                continue
            story.append(Paragraph(section_label(kind,sec['heading']),styles['section']))
            if kind=='historical': story.append(historical_box(blks)); story.append(Spacer(1,3)); continue
            if kind=='traps' and sum(1 for t,_ in blks if t=='bullet')>=3: story.append(traps_box(blks)); story.append(Spacer(1,3)); continue
            if kind=='current':
                story.append(HRFlowable(width='100%',thickness=0.5,color=RULE,spaceBefore=0,spaceAfter=3))
            if kind=='follow':
                seq=0; current=[]
                i=0
                while i<len(blks):
                    typ,txt=blks[i]
                    if typ=='h3':
                        seq+=1
                        mt=re.match(r'(Q\d+[a-z]?)\.\s*(.*)',txt,re.I)
                        key=mt.group(1) if mt else f'Q{q["q"]}{chr(96+seq)}'
                        qtxt=mt.group(2) if mt else txt
                        label=Paragraph('ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΤΗ',styles['followlabel'])
                        qp=TaggedParagraph(rich(qtxt),styles['followq'],tag=f'FOLLOW:{key}',label=f'{key}. {qtxt}')
                        first=None
                        if i+1<len(blks) and blks[i+1][0]=='p':
                            first=Paragraph(rich(blks[i+1][1]),styles['body']); i+=1
                        elems=[label,qp]+([first] if first else [])
                        story.append(KeepTogether(elems))
                    elif typ=='p': story.append(Paragraph(rich(txt),styles['body']))
                    elif typ in ('bullet','num'): story.append(Paragraph('• '+rich(txt),styles['bullet']))
                    i+=1
                continue
            for typ,txt in blks:
                if typ=='p': story.append(Paragraph(rich(txt),styles['body']))
                elif typ in ('bullet','num'): story.append(Paragraph('• '+rich(txt),styles['bullet']))
                elif typ=='h3': story.append(Paragraph(rich(txt),styles['followq']))
            if kind=='current':
                story.append(HRFlowable(width='100%',thickness=0.5,color=RULE,spaceBefore=1,spaceAfter=2))
    return story

def page_q_map(qstarts,total):
    starts=sorted(qstarts.items(),key=lambda x:x[1]); mp={}
    for idx,(q,s) in enumerate(starts):
        e=(starts[idx+1][1]-1) if idx+1<len(starts) else total
        for p in range(s,e+1): mp[p]=q
    return mp

def build_body(qs):
    p1=OUT/'body_pass1.pdf'; d1=BookDoc(str(p1)); d1.build(build_story(qs)); starts=dict(d1.qstarts)
    total=fitz.open(p1).page_count
    pmap=page_q_map(starts,total)
    p2=OUT/'body.pdf'; d2=BookDoc(str(p2),opener_pages=set(starts.values()),page_q=pmap); d2.build(build_story(qs))
    # qstarts should be stable
    if dict(d2.qstarts)!=starts: raise RuntimeError(f'Pagination changed pass1/pass2: {starts} vs {dict(d2.qstarts)}')
    return p2, starts, d2.followups

def cover_pdf(path):
    c=canvas.Canvas(str(path),pagesize=A4); c.setTitle(PDF_TITLE)
    x=36*mm; right=PAGE_W-32*mm
    c.setFillColor(BLUE); c.setFont('SansB',9.2); c.drawString(x,PAGE_H-45*mm,'ΟΙ')
    c.setStrokeColor(BLUE); c.setLineWidth(1); c.line(x,PAGE_H-51*mm,right,PAGE_H-51*mm)
    c.setFont('SerifB',48); c.drawString(x,PAGE_H-112*mm,'100')
    c.setFillColor(TEXT); c.setFont('SerifB',24)
    c.drawString(x,PAGE_H-147*mm,'ΚΑΙΡΙΕΣ ΕΡΩΤΗΣΕΙΣ')
    c.drawString(x,PAGE_H-162*mm,'ΣΤΗΝ ΨΥΧΙΑΤΡΙΚΗ')
    c.setStrokeColor(RULE); c.setLineWidth(.7); c.line(x,PAGE_H-178*mm,right,PAGE_H-178*mm)
    c.setFillColor(MID); c.setFont('SansM',9.5); c.drawString(x,PAGE_H-190*mm,'ΕΠΑΝΑΛΗΨΗ ΠΡΟΦΟΡΙΚΩΝ ΕΞΕΤΑΣΕΩΝ')
    c.setFont('Sans',8.3); c.drawString(x,37*mm,'Πλήρης έκδοση 100 ερωτήσεων')
    c.showPage(); c.save()

def toc_pdf(path,qs,starts):
    doc=SimpleDocTemplate(str(path),pagesize=A4,leftMargin=36*mm,rightMargin=32*mm,topMargin=24*mm,bottomMargin=20*mm)
    st=[Paragraph('ΠΕΡΙΕΧΟΜΕΝΑ',ParagraphStyle('toctitle',fontName='SerifB',fontSize=22,leading=26,textColor=TEXT,spaceAfter=4)),Paragraph('Οι 100 ερωτήσεις',styles['small']),Spacer(1,7*mm)]
    data=[]
    for q in qs:
        n=Paragraph(f'Q{q["q"]}',styles['tocn']); title=Paragraph(rich(q['title']),styles['toc']); pg=Paragraph(str(starts[q['q']]),ParagraphStyle('pg',parent=styles['tocn'],alignment=TA_RIGHT))
        data.append([n,title,pg])
    tab=Table(data,colWidths=[13*mm,doc.width-25*mm,12*mm],repeatRows=0,hAlign='LEFT')
    tab.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),2.0),('BOTTOMPADDING',(0,0),(-1,-1),2.0),('LINEBELOW',(0,0),(-1,-1),0.2,HexColor('#E5E8EA'))]))
    st.append(tab)
    def pagenum(c,d):
        c.saveState(); c.setFont('Sans',8); c.setFillColor(MID); c.drawCentredString(PAGE_W/2,11*mm,roman(d.page)); c.restoreState()
    doc.build(st,onFirstPage=pagenum,onLaterPages=pagenum)

def roman(n):
    vals=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    out='';
    for v,s in vals:
        while n>=v: out+=s; n-=v
    return out.lower()

def blank_pdf(path):
    c=canvas.Canvas(str(path),pagesize=A4); c.showPage(); c.save()

def assemble(cover,toc,body,starts,followups):
    cv=fitz.open(cover); tc=fitz.open(toc); bd=fitz.open(body)
    front_count=cv.page_count+tc.page_count
    blank_needed = front_count%2==1  # body begins on recto physical odd
    bl=None
    if blank_needed:
        bl=OUT/'blank.pdf'; blank_pdf(bl); front_count+=1
    out=fitz.open(); out.insert_pdf(cv); out.insert_pdf(tc)
    if bl: out.insert_pdf(fitz.open(bl))
    body_offset=out.page_count; out.insert_pdf(bd)
    toc_entries=[[1,'Περιεχόμενα',1]]
    for q,p in starts.items(): toc_entries.append([1,f'Q{q}. {next(x["title"] for x in QUESTIONS if x["q"]==q)}',body_offset+p])
    for key,p,label in followups:
        # child level, physical page
        toc_entries.append([2,label,body_offset+p])
    # sort maintaining hierarchy can be odd if followups appended; build correct ordered sequence instead
    toc_entries=[[1,'Περιεχόμενα',2]]
    fu_by_q={}
    for key,p,label in followups:
        m=re.match(r'Q(\d+)',key,re.I); q=int(m.group(1)) if m else None
        fu_by_q.setdefault(q,[]).append((p,label))
    for q in QUESTIONS:
        n=q['q']; toc_entries.append([1,f'Q{n}. {q["title"]}',body_offset+starts[n]])
        for p,label in fu_by_q.get(n,[]): toc_entries.append([2,label,body_offset+p])
    out.set_toc(toc_entries)
    out.set_metadata({'title':PDF_TITLE,'author':'','subject':'Επανάληψη προφορικών εξετάσεων Ψυχιατρικής','keywords':'ψυχιατρική, προφορικές εξετάσεις'})
    final=OUT/'The_100_Crucial_Questions_in_Psychiatry_v3_GREEK_COMPLETE_A4.pdf'; out.save(final,garbage=4,deflate=True,clean=True); out.close()
    return final,body_offset,tc.page_count,blank_needed


def remove_unused_base14_f1(path):
    """Remove ReportLab's unused /F1 Helvetica resource only when no page content stream references /F1."""
    reader=PdfReader(str(path))
    for page in reader.pages:
        c=page.get_contents()
        if c and b'/F1' in c.get_data():
            raise RuntimeError('Refusing Helvetica cleanup: /F1 is referenced by visible page content')
    writer=PdfWriter(clone_from=reader)
    removed=0
    for page in writer.pages:
        res=page.get('/Resources')
        fonts=res.get('/Font') if res else None
        if fonts and '/F1' in fonts:
            del fonts['/F1']; removed+=1
    tmp=Path(str(path)+'.clean.tmp')
    with tmp.open('wb') as fh:
        writer.write(fh)
    tmp.replace(path)
    return removed

def norm(s):
    s=unicodedata.normalize('NFC',s)
    s=s.replace('\u00ad','').replace('–','-').replace('—','-').replace('−','-')
    s=re.sub(r'\s+',' ',s).strip()
    return s

def source_lines(q):
    txt=Path(q['path']).read_text(encoding='utf-8')
    out=[]
    for line in txt.splitlines():
        z=line.strip()
        if not z or z.startswith('## '):
            continue
        if z.startswith('# '):
            z=re.sub(r'^#\s+Q\d+\.\s*','',z)
        elif z.startswith('### '):
            z=z[4:]
            z=re.sub(r'^Q\d+[a-z]?\.\s*','',z,flags=re.I)
        z=re.sub(r'^\d+\.\s*','',z)
        z=re.sub(r'^[-•]\s*','',z)
        z=plain_md(z)
        if len(z)>=2:
            out.append(z)
    return out

def question_pdf_text(pdf,q,start_body,end_body,body_offset):
    parts=[]
    for bp in range(start_body,end_body+1):
        p=pdf[body_offset+bp-1]
        for line in p.get_text('text').splitlines():
            z=line.strip()
            if not z or z==BOOK_TITLE or re.fullmatch(r'Q\d+',z) or re.fullmatch(r'\d+',z):
                continue
            parts.append(z)
    return norm(' '.join(parts))

def qa(final,qs,starts,body_offset):
    pdf=fitz.open(final)
    missing=[]; total=0
    for q in qs:
        st=starts[q['q']]
        e=starts.get(q['q']+1, pdf.page_count-body_offset+1)-1
        actual=question_pdf_text(pdf,q['q'],st,e,body_offset)
        for src in source_lines(q):
            total+=1
            if norm(src) not in actual:
                missing.append({'q':q['q'],'line':src[:260]})
    oob=[]; repl=[]
    for pi,page in enumerate(pdf,1):
        for b in page.get_text('dict').get('blocks',[]):
            for l in b.get('lines',[]):
                for sp in l.get('spans',[]):
                    x0,y0,x1,y1=sp['bbox']; txt=sp.get('text','')
                    if x0 < -1 or y0 < -1 or x1 > PAGE_W+1 or y1 > PAGE_H+1:
                        oob.append((pi,txt[:60],sp['bbox']))
                    if '\ufffd' in txt:
                        repl.append((pi,txt))
    start_errors=[]
    for q in qs:
        phys=body_offset+starts[q['q']]-1
        t=pdf[phys].get_text('text')
        if f'ΕΡΩΤΗΣΗ {q["q"]}' not in t or q['title'][:25] not in t:
            start_errors.append(q['q'])
    fonts={}
    for page in pdf:
        for f in page.get_fonts(full=True): fonts[f[3]]=f
    report={'source_commit':SOURCE_COMMIT,'questions':len(qs),'physical_pages':pdf.page_count,'body_pages':pdf.page_count-body_offset,
      'body_offset_physical_pages':body_offset,'question_start_pages_body':starts,'source_lines_total':total,'source_lines_missing':len(missing),'missing_examples':missing[:25],
      'out_of_bounds':len(oob),'replacement_glyphs':len(repl),'question_start_errors':start_errors,'fonts':sorted(fonts.keys()),'base14_fonts':[n for n in sorted(fonts.keys()) if n in {'Helvetica','Times-Roman','Courier','Symbol','ZapfDingbats'}]}
    return report

if __name__=='__main__':
    QUESTIONS=read_questions()
    # source manifest
    sm={str(q['q']):{'path':q['path'],'git_blob_sha':q['sha'],'bytes':q['bytes']} for q in QUESTIONS}
    body,starts,followups=build_body(QUESTIONS)
    cover=OUT/'cover.pdf'; cover_pdf(cover)
    toc=OUT/'contents.pdf'; toc_pdf(toc,QUESTIONS,starts)
    final,body_offset,toc_pages,blank_needed=assemble(cover,toc,body,starts,followups)
    removed_f1_resources=remove_unused_base14_f1(final)
    report=qa(final,QUESTIONS,starts,body_offset)
    report['unused_f1_resources_removed']=removed_f1_resources
    report['contents_pages']=toc_pages; report['recto_blank_added']=blank_needed; report['followup_bookmarks']=len(followups)
    sha=hashlib.sha256(final.read_bytes()).hexdigest(); report['pdf_sha256']=sha
    manifest={'source_commit':SOURCE_COMMIT,'source_directory':str(SRC),'sources':sm,'pdf':final.name,'pdf_sha256':sha,'body_page_starts':starts,'followups':[{'key':k,'body_page':p,'label':l} for k,p,l in followups]}
    (OUT/'GREEK_COMPLETE_book_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    (OUT/'GREEK_COMPLETE_QA_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    if report['source_lines_missing'] or report['out_of_bounds'] or report['replacement_glyphs'] or report['question_start_errors'] or report.get('base14_fonts'):
        raise SystemExit(2)
