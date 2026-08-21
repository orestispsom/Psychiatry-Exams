import sys, re
from pathlib import Path
p=Path(sys.argv[1])
s=p.read_text('utf-8')

# 1) Parse consecutive Markdown table rows as one reusable table block.
a=s.index('def blocks(lines):')
b=s.index('def section_kind(h):')
new_blocks=r'''def blocks(lines):
    out=[]; buf=[]; i=0
    def flush():
        nonlocal buf
        if buf: out.append(('p',' '.join(x.strip() for x in buf))); buf=[]
    while i < len(lines):
        ln=lines[i]
        if ln.lstrip().startswith('|'):
            flush(); rows=[]
            while i < len(lines) and lines[i].lstrip().startswith('|'):
                rows.append(lines[i].strip()); i+=1
            out.append(('table',rows)); continue
        if ln.startswith('### '): flush(); out.append(('h3',ln[4:].strip()))
        elif re.match(r'^\s*[-•]\s+',ln): flush(); out.append(('bullet',re.sub(r'^\s*[-•]\s+','',ln)))
        elif re.match(r'^\s*\d+\.\s+',ln): flush(); out.append(('num',re.sub(r'^\s*\d+\.\s+','',ln)))
        elif ln.strip()=='': flush()
        else: buf.append(ln)
        i+=1
    flush(); return out

'''
s=s[:a]+new_blocks+s[b:]

# 2) Typeset the source table inside the established publication vocabulary.
marker='def historical_box(blks):\n'
table_fn=r'''def markdown_table(raw_rows):
    rows=[]
    for line in raw_rows:
        cells=[c.strip() for c in line.strip().strip('|').split('|')]
        if cells and all(re.fullmatch(r':?-{3,}:?',c.replace(' ','')) for c in cells):
            continue
        rows.append(cells)
    if not rows: return Spacer(1,1)
    n=max(len(r) for r in rows)
    for r in rows: r.extend(['']*(n-len(r)))
    body=ParagraphStyle('tablebody-v4',parent=styles['body'],fontSize=8.8,leading=11.2,spaceAfter=0)
    head=ParagraphStyle('tablehead-v4',parent=body,fontName='SansB',fontSize=8.5,leading=10.8,textColor=TEXT)
    data=[]
    for ri,row in enumerate(rows):
        st=head if ri==0 else body
        data.append([Paragraph(rich(c),st) for c in row])
    if n==2: widths=[35*mm,BODY_W-35*mm]
    else: widths=[BODY_W/n]*n
    tab=Table(data,colWidths=widths,hAlign='LEFT',repeatRows=1,splitByRow=1)
    tab.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('GRID',(0,0),(-1,-1),0.35,RULE),
        ('BACKGROUND',(0,0),(-1,0),LIGHT),
        ('LEFTPADDING',(0,0),(-1,-1),5),
        ('RIGHTPADDING',(0,0),(-1,-1),5),
        ('TOPPADDING',(0,0),(-1,-1),5),
        ('BOTTOMPADDING',(0,0),(-1,-1),5),
    ]))
    return tab

'''
assert marker in s
s=s.replace(marker,table_fn+marker,1)

# 3) Add table rendering to generic sections.
old_h3="""                elif typ=='h3': story.append(Paragraph(rich(txt),styles['followq']))"""
new_h3="""                elif typ=='h3': story.append(Paragraph(rich(txt),styles['followq']))\n                elif typ=='table': story.append(markdown_table(txt)); story.append(Spacer(1,2*mm))"""
assert old_h3 in s
s=s.replace(old_h3,new_h3,1)

# 4) Any learner-facing H3 whose title begins Qxx[a]. is an examiner follow-up,
# regardless of the enclosing section. Preserve the established label/question styling,
# tag it for PDF navigation, and keep the first answer paragraph with it when possible.
old_generic="""            for typ,txt in blks:
                if typ=='p': story.append(Paragraph(rich(txt),styles['body']))
                elif typ in ('bullet','num'): story.append(Paragraph('• '+rich(txt),styles['bullet']))
                elif typ=='h3': story.append(Paragraph(rich(txt),styles['followq']))
                elif typ=='table': story.append(markdown_table(txt)); story.append(Spacer(1,2*mm))
"""
new_generic="""            i=0
            while i<len(blks):
                typ,txt=blks[i]
                if typ=='p':
                    story.append(Paragraph(rich(txt),styles['body']))
                elif typ in ('bullet','num'):
                    story.append(Paragraph('• '+rich(txt),styles['bullet']))
                elif typ=='h3':
                    m=re.match(r'(Q\\d+[a-z]?)\\.\\s*(.*)',txt,re.I)
                    if m:
                        key=m.group(1); qtxt=m.group(2)
                        first=[]
                        if i+1<len(blks) and blks[i+1][0]=='p':
                            first=[Paragraph(rich(blks[i+1][1]),styles['body'])]
                            i+=1
                        story.append(KeepTogether([
                            Paragraph('ΕΡΩΤΗΣΗ ΕΞΕΤΑΣΤΗ',styles['section']),
                            TaggedParagraph(key+'. '+rich(qtxt),styles['followq'],f'FOLLOW:{key}'),
                            *first
                        ]))
                    else:
                        story.append(Paragraph(rich(txt),styles['followq']))
                elif typ=='table':
                    story.append(markdown_table(txt)); story.append(Spacer(1,2*mm))
                i+=1
"""
assert old_generic in s
s=s.replace(old_generic,new_generic,1)

# 5) Source-fidelity comparison treats Markdown table cells as content, not pipe syntax.
a=s.index('def source_lines(q):')
b=s.index('def question_pdf_text(')
source_fn=r'''def source_lines(q):
    txt=Path(q['path']).read_text(encoding='utf-8')
    out=[]
    for line in txt.splitlines():
        z=line.strip()
        if not z or z.startswith('## '): continue
        if z.startswith('|'):
            cells=[c.strip() for c in z.strip('|').split('|')]
            if cells and all(re.fullmatch(r':?-{3,}:?',c.replace(' ','')) for c in cells): continue
            for c in cells:
                c=plain_md(c)
                if len(c)>=2: out.append(c)
            continue
        if z.startswith('# '): z=re.sub(r'^#\s+Q\d+\.\s*','',z)
        elif z.startswith('### '):
            z=z[4:]; z=re.sub(r'^Q\d+[a-z]?\.\s*','',z,flags=re.I)
        z=re.sub(r'^\d+\.\s*','',z); z=re.sub(r'^[-•]\s*','',z); z=plain_md(z)
        if len(z)>=2: out.append(z)
    return out

'''
s=s[:a]+source_fn+s[b:]
p.write_text(s,'utf-8')
print('patched',p)
