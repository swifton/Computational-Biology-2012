def E(a):
    b = [0 for x in range(0)]
    
    s = a[2] * a[6]
    l = a[4] * a[5]
    b.append([s / (s + l), l / (s + l)])
    
    s = a[0] * a[4]
    l = a[1] * a[3]
    b.append([s / (s + l), l / (s + l)])
    
    s = a[4] * a[8]
    l = a[6] * a[7]
    b.append([s / (s + l), l / (s + l)])

    return b
        
def M(b):
    a[0] = b[1][0] / 6
    a[1] = b[1][1] / 6
    a[2] = b[0][0] / 6
    a[3] = b[1][1] / 6
    a[4] = (b[0][1] + b[1][0] + b[2][0]) / 6
    a[5] = b[0][1] / 6
    a[6] = (b[0][0] + b[2][1]) / 6
    a[7] = b[2][1] / 6
    a[8] = b[2][0] / 6
    return a

a = [1.0/12 for x in xrange(9)]
a[4] = 3.0/12 #10011
a[6] = 2.0/12 #10111
j = 0

while (abs(a[4] - j)>0.000000001):
    j = a[4]
    b = E(a)
    a = M(b)

print a
print b
