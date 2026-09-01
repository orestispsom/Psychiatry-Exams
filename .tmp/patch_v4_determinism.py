import sys
from pathlib import Path
p=Path(sys.argv[1])
s=p.read_text('utf-8')
start=s.index('def remove_unused_base14_f1(path):')
end=s.index('def norm(s):', start)
new='''def remove_unused_base14_f1(path):\n    """Remove an unused /F1 Helvetica resource only when it exists.\n\n    Crucially, do not rewrite the PDF when there is nothing to remove;\n    pypdf serialization can regenerate document IDs and make otherwise\n    identical builds byte-nondeterministic.\n    """\n    reader=PdfReader(str(path))\n    removable=[]\n    for idx,page in enumerate(reader.pages):\n        c=page.get_contents()\n        if c and b'/F1' in c.get_data():\n            raise RuntimeError('Refusing Helvetica cleanup: /F1 is referenced by visible page content')\n        res=page.get('/Resources')\n        fonts=res.get('/Font') if res else None\n        if fonts and '/F1' in fonts:\n            removable.append(idx)\n    if not removable:\n        return 0\n    writer=PdfWriter(clone_from=reader)\n    removed=0\n    for idx in removable:\n        page=writer.pages[idx]\n        res=page.get('/Resources')\n        fonts=res.get('/Font') if res else None\n        if fonts and '/F1' in fonts:\n            del fonts['/F1']; removed+=1\n    tmp=Path(str(path)+'.clean.tmp')\n    with tmp.open('wb') as fh:\n        writer.write(fh)\n    tmp.replace(path)\n    return removed\n\n'''
s=s[:start]+new+s[end:]
p.write_text(s,'utf-8')
print('patched deterministic no-op Helvetica cleanup',p)
