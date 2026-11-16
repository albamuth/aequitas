import zipfile
import numpy as np
z = zipfile.ZipFile('C:/PROJECTS/Aequitas/06-simulation/data/exiobase/IOT_2022_pxp.zip')
with z.open('energy/F.txt') as f:
    reg = f.readline().rstrip(b'\n').split(b'\t')
    f.readline(); f.readline()
    for line in f:
        if not line.strip():
            continue
        p = line.rstrip(b'\n').split(b'\t')
        v = np.array(p[1:], dtype=float)
        nz = np.nonzero(v)[0]
        print(p[0].decode(), 'ncols', len(v), 'nonzero', len(nz), 'sum', v.sum())
        if len(nz):
            regs = sorted(set(reg[1 + i].decode() for i in nz))
            print('  regions with nonzero:', regs[:60])
            print('  first nz cols', nz[:10], 'DE nz', sum(1 for i in nz if reg[1 + i] == b'DE'))
