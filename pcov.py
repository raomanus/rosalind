def getSuperString(kmers):
	dbGraph = dict()
	superString = ""
	for kmer in kmers:
		dbGraph[kmer[:-1]] = kmer[1:]

	keys = list(dbGraph.keys())
	k = keys[0]

	while len(superString) < len(kmers):
		superString+=dbGraph[k][-1]
		k = dbGraph[k]

	return superString


file = open("rosalind_pcov.txt","r")
kmers = file.read().splitlines()
print(getSuperString(kmers))