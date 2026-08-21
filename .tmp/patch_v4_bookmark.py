import sys
from pathlib import Path
p=Path(sys.argv[1])
s=p.read_text('utf-8')
old="TaggedParagraph(key+'. '+rich(qtxt),styles['followq'],f'FOLLOW:{key}'),"
new="TaggedParagraph(key+'. '+rich(qtxt),styles['followq'],tag=f'FOLLOW:{key}',label=f'{key}. {qtxt}'),"
if old not in s:
    raise SystemExit('bookmark patch target not found')
s=s.replace(old,new,1)
p.write_text(s,'utf-8')
print('patched bookmark label fallback',p)
