file = open("data.txt")
line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
line4 = file.readline()

def mult(a,b):
    d = range(0,112)
    for i in d:
        d[i]  = a[i] * b[i]
    return d

def first(a,b):
    d = range(0,112)
    for i in d:
        d[i] = a[i] * (1 - b[i])
    return d

def nott(a,b):
    d = range(0,112)
    for i in d:
        d[i] = (1 - a[i]) * (1 - b[i])
    return d

g80 = range(1,113)
g4 = range(1,113)
g2 = range(1,113)

for i in range(1,113):
    g80[i - 1] = int(line2[4 + 2 * i])
    g4[i - 1] = int(line3[3 + 2 * i])
    g2[i - 1] = int(line4[3 + 2 * i])


th80 = sum(g80) * 1.0 / 112
th80 = [1 - th80, th80]
th4 = sum(g4) * 1.0 / 112
th4 = [1 - th4, th4]

th480 = [[0 for x in xrange(2)] for x in xrange(2)]

th480[1][1] = sum(mult(g80,g4)) * 1.0 / sum(g80)
th480[1][0] = sum(first(g4,g80)) * 1.0 / (112 - sum(g80))
th480[0][1] = 1 - th480[1][1]
th480[0][0] = 1 - th480[1][0]

th24 = [[0 for x in xrange(2)] for x in xrange(2)]

th24[1][1] = sum(mult(g2,g4)) * 1.0 / sum(g4)
th24[1][0] = sum(first(g2,g4)) * 1.0 / (112 - sum(g4))
th24[0][1] = 1 - th24[1][1]
th24[0][0] = 1 - th24[1][0]

th2480 = [[[0 for x in xrange(2)] for x in xrange(2)] for x in xrange(2)]

th2480[1][1][1] = sum(mult(mult(g80,g4),g2)) * 1.0 / sum(mult(g80,g4))
th2480[0][1][1] = 1 - th2480[1][1][1]
th2480[1][1][0] = sum(mult(g2,first(g4,g80))) * 1.0 / sum(first(g4,g80))
th2480[0][1][0] = 1 - th2480[1][1][0]
th2480[1][0][1] = sum(mult(g2,first(g80,g4))) * 1.0 / sum(first(g80,g4))
th2480[0][0][1] = 1 - th2480[1][0][1]
th2480[1][0][0] = sum(mult(g2, nott(g80,g4))) * 1.0 / sum(nott(g80,g4))
th2480[0][0][0] = 1 - th2480[1][0][0]

f1 = 1
f2 = 1

for i in range(0,112):
    f1 *= th80[g80[i]] * th480[g4[i]][g80[i]] * th24[g2[i]][g4[i]]
    f2 *= th80[g80[i]] * th4[g4[i]] * th2480[g2[i]][g4[i]][g80[i]]

print f1, f2
