from Bio import SeqIO
import sys
gap_cost = 1
match_cost = 0
mismatch_cost = 1
mod_value=134217727
sys.setrecursionlimit(3000)
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
			distMat[i][j] = min(match,delete,insert)

	return (distMat[m][n], distMat)

def getNumAlignments(s, t, i, j, optDist, costMatrix, countMatrix):
	if i == 0 and j == 0:
		return 1
	elif i == 0 and j > 0:
		return j*gap_cost
	elif i > 0 and j == 0:
		return i*gap_cost
	elif countMatrix[i][j] != -1:
		return countMatrix[i][j]
	else:
		a = s[i-1]
		b = t[j-1]
		totalAlignments = 0
		if optDist - getCost(a,b) == costMatrix[i-1][j-1]:
			totalAlignments = (totalAlignments + getNumAlignments(s, t, i-1, j-1, optDist - getCost(a,b), costMatrix, countMatrix))
		if optDist - gap_cost == costMatrix[i-1][j]:
			totalAlignments = (totalAlignments + getNumAlignments(s, t, i-1, j, optDist - gap_cost, costMatrix, countMatrix))
		if optDist - gap_cost == costMatrix[i][j-1]:
			totalAlignments += (totalAlignments + getNumAlignments(s, t, i, j-1, optDist - gap_cost, costMatrix, countMatrix))

		countMatrix[i][j] = totalAlignments
		return totalAlignments

input_file = open("rosalind_ctea.txt",'r')		
sequences = SeqIO.parse(input_file,'fasta')
strings = []
for fasta_seq in sequences:
	strings.append(str(fasta_seq.seq))

s = strings[0]
t = strings[1]
slen = len(s)
tlen = len(t)

optDist, costMatrix = editDist(s,t,slen,tlen)

countMatrix = [[-1 for x in range(tlen+1)]for x in range(slen+1)]

numAlignments = getNumAlignments(s, t, slen, tlen, optDist, costMatrix, countMatrix)
mod_value = numAlignments%mod_value
print(optDist,mod_value,countMatrix[slen][tlen])

