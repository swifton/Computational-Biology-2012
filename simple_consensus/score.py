import math

def PWM(M):
    n = len(M)
    M = transpose(M)
    l = len(M)
    PWM = [range(4) for x in range(l)]
    
    for j in range(l):
        PWM[j][0] = M[j].count('A') * 1.0 / n
        PWM[j][1] = M[j].count('C') * 1.0 / n
        PWM[j][2] = M[j].count('G') * 1.0 / n
        PWM[j][3] = M[j].count('T') * 1.0 / n
    return PWM


def PWMScore(M):
    l = len(M[0])
    P = PWM(M)

    q = range(4)
    q[0] = 0.35
    q[1] = 0.15
    q[2] = 0.15
    q[3] = 0.35
    
    s = 0
    for j in range(l):
        for i in range(4):
            if (P[j][i] != 0):
                s += P[j][i] * math.log10(P[j][i] / q[i])
    return s
    
def transpose(M):
    n = len(M)
    m = len(M[0])
    B = [range(n) for x in range(m)]
    for i in range(n):
        for j in range(m):
            B[j][i] = M[i][j]
    return B
