from Bio import SeqIO
cTable = {'A':'T','G':'C','C':'G','T':'A'}

def getReverseComplement(kmer):
	rc = ""
	for c in kmer[::-1]:
		rc += cTable[c]

	return rc

def getHammingDistance(s1, s2):
	diff = 0
	for c1,c2 in zip(s1,s2):
		if c1 != c2:
			diff += 1

	return diff

def getCorrectSequence(seq, correct_reads):
	for cseq in correct_reads:
		dist = getHammingDistance(seq, cseq)
		if dist == 1:
			return cseq


input_file = open("rosalind_corr.txt",'r')		
sequences = SeqIO.parse(input_file,'fasta')
reads = []
for fasta_seq in sequences:
	reads.append(str(fasta_seq.seq))

correct_seq = set()
incorrect_seq = set()
for read in reads:
	if reads.count(read) > 1:
		correct_seq.add(read)
	else:
		reverse = getReverseComplement(read)
		if reads.count(reverse) > 0:
			correct_seq.add(read)
		else:
			incorrect_seq.add(read)

correct_seq_rc = set()
for seq in correct_seq:
	correct_seq_rc.add(getReverseComplement(seq))

correct_seq.update(correct_seq_rc)

for seq in incorrect_seq:
	correct = getCorrectSequence(seq, correct_seq)
	print(seq+"->"+correct)
	