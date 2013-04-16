import math

def LOD(marker, phen):
    zero = [0 for x in range(0)]
    one = [0 for x in range(0)]
    uA = 0
    uB = 0
    uF = 0
    j = 0
    l = 0

    for i in xrange(334):
        if (marker[i] == 0):
            zero.append(phen[i])
        else:
            one.append(phen[i])

    if (len(zero) != 0):
        uA = sum(zero)/len(zero)
        sA = math.sqrt(sum((x - uA) * (x - uA) for x in zero) / len(zero))

    if (len(one) != 0):
        uB = sum(one)/len(one)
        sB = math.sqrt(sum((x - uB) * (x - uB) for x in one) / len(one))
    
    uF = sum(phen)/len(phen)
    sF = math.sqrt(sum((x - uF) * (x - uF) for x in phen) / len(phen))

    LOD = sum(math.log10(math.exp(- (x - uA) * (x - uA) / (2 * sA * sA))/math.sqrt(2 * math.pi * sA * sA)) for x in zero)
    LOD += sum(math.log10(math.exp(- (x - uB) * (x - uB) / (2 * sB * sB))/math.sqrt(2 * math.pi * sB * sB)) for x in one)
    LOD -= sum(math.log10(math.exp(- (x - uF) * (x - uF) / (2 * sF * sF))/math.sqrt(2 * math.pi * sF * sF)) for x in phen)

    return LOD
    
