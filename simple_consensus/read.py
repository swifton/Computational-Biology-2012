import string
import LOD
import random
import copy

genotype = open("genotype")
phenotype = open("phenotype")

i = 0

line = genotype.readline()

gen = [0 for x in range(0)]

while (line != ""):
    g = [0 for x in range(0)]
    line = line.split(" ")
    for val in line[0]:
        if (val != '\t' and val != '\n'):
            g.append(float(val))
    i += 1
    gen.append(g)
    line = genotype.readline()

ph = phenotype.readline()

i = 0
l = 0
ph = ph.split(" ")
ph = ph[0]
phen = [0 for x in range(0)]

while (l != -1):
    l = string.find(ph,"\t",i,len(ph))
    phen.append(float(ph[i:l]))
    i = l + 1

def GWLOD(gen, phen):
    a = [0 for x in range(0)]

    for j in range(len(gen)):
        a.append(LOD.LOD(gen[j],phen))

    return max(a)

maxLOD = GWLOD(gen,phen)

print 'maxLOD =', maxLOD

perc = [x for x in range(100)]

for j in perc:
    d = copy.copy(phen)
    random.shuffle(d)
    perc[j] = GWLOD(gen, d)
    print 'perc[', j, '] =', perc[j]
    # If you don't print, it's too boring to wait for so long.

for j in xrange(5):
    perc.remove(max(perc))

c = max(perc)

for j in range(len(gen)):
    b = LOD.LOD(gen[j],phen)
    if (b > c):
        print j
        print b
