import sys
from pathlib import Path
p=Path(sys.argv[1])
s=p.read_text('utf-8')
marker='def norm(s):\n'
insert='''def canonicalize_pdf_id(path):\n    """Set deterministic trailer IDs without reserializing PDF objects."""\n    import hashlib as _hashlib\n    data=Path(path).read_bytes()\n    pattern=re.compile(br'/ID\\[<[0-9A-Fa-f]{32}><[0-9A-Fa-f]{32}>\\]')\n    matches=list(pattern.finditer(data))\n    if len(matches)!=1:\n        raise RuntimeError(f'Expected exactly one PDF trailer /ID, found {len(matches)}')\n    seed=_hashlib.sha256((SOURCE_COMMIT+'|Q11-derived-locked-A4|Greek-v4-final-r1').encode('utf-8')).hexdigest().upper()\n    replacement=f'/ID[<{seed[:32]}><{seed[32:64]}>]'.encode('ascii')\n    if len(replacement)!=matches[0].end()-matches[0].start():\n        raise RuntimeError('Deterministic /ID replacement changed byte length')\n    data=data[:matches[0].start()]+replacement+data[matches[0].end():]\n    Path(path).write_bytes(data)\n    return seed[:32], seed[32:64]\n\n'''
if insert.strip() not in s:
    assert marker in s
    s=s.replace(marker,insert+marker,1)
old="    removed_f1_resources=remove_unused_base14_f1(final)\n    report=qa(final,QUESTIONS,starts,body_offset)\n"
new="    removed_f1_resources=remove_unused_base14_f1(final)\n    canonical_pdf_ids=canonicalize_pdf_id(final)\n    report=qa(final,QUESTIONS,starts,body_offset)\n    report['canonical_pdf_ids']=list(canonical_pdf_ids)\n"
if old not in s:
    raise SystemExit('canonical ID call target not found')
s=s.replace(old,new,1)
p.write_text(s,'utf-8')
print('patched deterministic PDF trailer IDs',p)
