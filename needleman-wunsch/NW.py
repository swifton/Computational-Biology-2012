import random
import copy

def score(seq1, seq2, sigma,elements): # sigma == BLOSUM62, elements - list of aminoacids.
    V =[[0]] # The matrix of scores
    K= [[0]] # This matrix is used to store the alignment
    
    for i in xrange(len(seq1)): # Filling the first row
        V.append([0])
        K.append([0])
        V[i+1][0] = V[i][0] + sigma[elements.index('*')][elements.index(seq1[i])]
        K[i+1][0] = 0

    for j in xrange(len(seq2)): # Filling the first column
        V[0].append(V[0][j] + sigma[elements.index('*')][elements.index(seq2[j])])
        K[0].append(1)

    for i in xrange(len(seq1)): # Filling the rest
        for j in xrange(len(seq2)):
            a = []
            a.append(V[i][j+1] + sigma[elements.index('*')][elements.index(seq1[i])])
            a.append(V[i+1][j] + sigma[elements.index('*')][elements.index(seq2[j])])
            a.append(V[i][j] + sigma[elements.index(seq2[j])][elements.index(seq1[i])])

            K[i+1].append(a.index(max(a))) # Saving data for traceback
                   
            V[i+1].append(max(a))
    # traceback
    s1 = ''
    s2 = ''
    while (i > -1 or j > -1): # At the end of the previous loop i == len(seq1), j == len(seq2)
        ind = K[i+1][j+1]
        if (ind == 0):
            s1 += seq1[i]
            s2 += '_'
            i -= 1
        elif (ind == 1):
            s1 += '_'
            s2 += seq2[j]
            j -= 1
        elif (ind == 2):
            s1 += seq1[i]
            s2 += seq2[j]
            i -= 1
            j -= 1
    return V,s1[::-1], s2[::-1] # Need to reverse the sequences, because started from the end

File = open("BLOSUM62.txt")

line = File.readline()
elements = line[:len(line)-1].split()
sigma = [0 for x in xrange(0)]

for i in elements:
    line = File.readline()
    line = [float(x) for x in line.split()[1:]]
    sigma.append(line)

seq1 = 'DEADLY'
seq2 = 'DDGEARLYK'

A = score(seq1,seq2,sigma,elements)
sc = A[0][len(seq1)][len(seq2)]
print A[0]
print A[1]
print A[2]
print sc

perc = [x for x in range(1000)] # array of permutation scores
counter = 0 # number of scores that are greater than the initial one

for j in perc:
    d = copy.copy(seq2) # copying 
    l = list(d)
    random.shuffle(l) # permuting
    d = ''.join(l)
    perc[j] = score(seq1, d,sigma,elements)[0][len(seq1)][len(seq2)]
    if (sc < perc[j]): # counting the number of greater scores
        counter += 1

print 'p =', counter*1.0/1000

pr = [] # This is the array of proteins
pr.append('MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH')
pr.append('MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH')
pr.append('MVHLTDAEKAAVSCLWGKVNSDEVGGEALGRLLVVYPWTQRYFDSFGDLSSASAIMGNAKVKAHGKKVITAFNDGLNHLDSLKGTFASLSELHCDKLHVDPENFRLLGNMIVIVLGHHLGKDFTPAAQAAFQKVVAGVATALAHKYH')
pr.append('MVHWTAEEKQLITGLWGKVNVAECGAEALARLLIVYPWTQRFFASFGNLSSPTAILGNPMVRAHGKKVLTSFGDAVKNLDNIKNTFSQLSELHCDKLHVDPENFRLLGDILIIVLAAHFSKDFTPECQAAWQKLVRVVAHALARKYH')
pr.append('MVEWTDQERTIISNIFSTLDYEDVGSKSLIRCLIVYPWTQRYFAGFGNLYNAEAIKNNPNIAKHGVTVLHGLDRAVKNMDNIKETYKELSELHSEKLHVDPDNFKLLSDCLTIVVATKMGSKFTPEIQATFQKFLAVVVSALGRQYH')
pr.append('MVAFSDKQEGLVNGAYEAFKADIPKYSVVFYTTILEKAPAAKNLFSFLANGVDATNPKLTGHAEKLFGLVRDSAAQLRASGGVVADAALGAVHSQKAVNDAQFVVVKEALVKTLKEAVGDKWSDELGTAVELAYDELAAAIKKAY')
pr.append('MDPRLPAWALVLLGPALVFALGPAPTPEMREKLCGHHFVRALVRVCGGPRWSTEARRPATGGDRELLQWLERRHLLHGLVADSNLTLGPGLQPLPQTSHHHRHHRAAATNPARYCCLSGCTQQDLLTLCPY')

for i in xrange(6): # doing the same thing for proteins
    A = score(pr[0],pr[i+1],sigma,elements)
    sc = A[0][len(pr[0])][len(pr[i+1])]
    print 'score #',i,' =', sc

    perc = [x for x in range(1000)]
    counter = 0

    for j in perc:
        d = copy.copy(pr[i+1])
        l = list(d)
        random.shuffle(l)
        d = ''.join(l)
        perc[j] = score(pr[0], d,sigma,elements)[0][len(pr[0])][len(pr[i+1])]
        if (sc < perc[j]):
            counter += 1

    print 'p #',i,' =', counter*1.0/1000
    print counter
