cTable = {'A':'T','G':'C','C':'G','T':'A'}

def reverseCompliment(kmers):
	rcSet = set()
	for kmer in kmers:
		rc = ""
		for c in kmer[::-1]:
			rc += cTable[c]
		rcSet.add(rc)

	return rcSet


file = open("rosalind_dbru.txt","r")
output_file = open("output.txt","w")
kmers = file.read().splitlines()
klen = len(kmers[0])
kmers = set(kmers)
kmers.update(reverseCompliment(kmers))
kmers = sorted(kmers)
for kmer in kmers:
	output_file.write(str((kmer[0:klen-1], kmer[1:klen])).replace("'",''))
	output_file.write('\n')

output_file.close()