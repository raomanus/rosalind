from Bio import SeqIO

input_file = open("rosalind_grph.txt",'r')		
sequences = SeqIO.parse(input_file,'fasta')
seq_dict = {}

def compute_overlap(key1, key2):
	string1 = seq_dict[key1]
	string2 = seq_dict[key2]
	if string1[-3:] == string2[:3]:
		print(key1, key2)
		pass
	if string2[-3:] == string1[:3]:
		print(key2, key1)
		pass

for fasta_seq in sequences:
	name, value = fasta_seq.id, str(fasta_seq.seq)
	seq_dict[name] = value

seq_list = list(seq_dict.keys())

for i in range(len(seq_list) - 1):
	for j in range(i+1, len(seq_list)):
		compute_overlap(seq_list[i], seq_list[j])
	pass