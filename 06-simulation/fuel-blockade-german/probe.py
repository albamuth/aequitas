import zipfile, itertools, sys
z = zipfile.ZipFile('06-simulation/data/exiobase/IOT_2022_pxp.zip')


def head(n, k, w=300):
    with z.open(n) as f:
        for i in range(k):
            print(n, i, repr(f.readline()[:w].decode()))


head('Z.txt', 5, 200)
head('Y.txt', 4, 400)
head('x.txt', 4, 200)
head('energy/F.txt', 8, 120)
names = [l.decode().split('\t')[1] for l in itertools.islice(z.open('unit.txt'), 1, 201)]
print(len(names))
for i, n in enumerate(names):
    print(i, n)
