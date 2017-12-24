from Bio import SeqIO
gap_cost = -1
match_cost = 1
mismatch_cost = -100

def getCost(a,b):
	if a == b:
		return match_cost
	elif a == '-' or b == '-':
		return gap_cost
	else:
		return mismatch_cost



def editDist(X,Y,m,n):
	distMat = [[0 for x in range(n+1)] for x in range(m+1)]
	for i in range(0,m+1):
		distMat[i][0] = gap_cost*i

	for j in range(0,n+1):
		distMat[0][j] = gap_cost*j	

	for i in range(1,m+1):
		for j in range(1,n+1):
			match = distMat[i-1][j-1] + getCost(X[i-1],Y[j-1])
			delete = distMat[i-1][j] + gap_cost
			insert = distMat[i][j-1] + gap_cost
			distMat[i][j] = max(match,delete,insert)


	s1 = ""
	t1 = ""
	i = m
	j = n

	while i > 0 or j > 0:
		if i > 0  and distMat[i][j] == distMat[i-1][j] + gap_cost:
			s1 += X[i-1]
			t1 += "-"
			i -= 1
		elif j > 0 and distMat[i][j] == distMat[i][j-1] + gap_cost:
			s1 += "-"
			t1 += Y[j-1]
			j -= 1
		elif i > 0 and j > 0 and distMat[i][j] == distMat[i-1][j-1] + getCost(X[i-1],Y[j-1]):
			s1 += X[i-1]
			t1 += Y[j-1]
			i -= 1
			j -= 1

	return (distMat[m][n],s1[::-1],t1[::-1])


input_file = open("rosalind_mgap.txt",'r')		
sequences = SeqIO.parse(input_file,'fasta')
strings = []
for fasta_seq in sequences:
	strings.append(str(fasta_seq.seq))

s = strings[0]
t = strings[1]
slen = len(s)
tlen = len(t)

dist, res1, res2 = editDist(s,t,slen,tlen)
print(dist)
print(res1)
print(res2)
d1 = res1.count('-')
d2 = res2.count('-')

print(d1+d2)
