import score
import  copy

def subsequences(seq, k):
    subseq = ["" for x in range(0)]
    i = 0
    while (i + k <= len(seq)):
        subseq.insert(i + 1, seq[i:i + k])
        i += 1
    return subseq

file = open("kruppel.fa.txt")
line = file.readline()
i = -1
sequence = ["" for x in range(0)]
k = input('Input k (length of motif)\n');
T = input('Input T (number of motifs)\n');
motifs = [0 for x in xrange(T)]
newmotifs = [0 for x in xrange(T)]
scores = [0 for x in xrange(T)]

while (line != ""):
    if (line[0] == ">"):
        i += 1
        sequence.insert(i + 1,"")
    else:
        sequence[i] += line[:len(line) - 1]
    line = file.readline()

A = subsequences(sequence[0], k)
B = subsequences(sequence[1], k)



for s1 in A:
    for s2 in B:
         M = [s1,s2]
         sco = score.PWMScore(M)
         i = 0
         for sc in scores:
             if (sc < sco):
                 scores[i] = sco
                 motifs[i] = copy.copy(M)
                 break
             i += 1
p = 0

for i in xrange(2, len(sequence)):
    A = subsequences(sequence[i], k)
    scores = [0 for x in xrange(T)]
    for motif in motifs:
        motif.append("")
        for s in A:
            motif[i] =  s
            p += 1
            sco = score.PWMScore(motif)
            j = 0 
            for sc in scores:
                if (sc < sco):
                    scores[j] = sco
                    newmotifs[j] = copy.copy(motif)
                    break
                j += 1
    motifs = copy.deepcopy(newmotifs)

for motif in motifs:
    print score.PWM(motif)
