from Bio import SeqIO
import operator

input_file = open("rosalind_long.txt",'r')		
sequences = SeqIO.parse(input_file,'fasta')
seq_dict = {}
overlap_dict = {}
seq_list = []

def compute_superstring(seq_list):
	str_tuple = max(overlap_dict.iterkeys(), key=(lambda key: overlap_dict[key]))
	x,y = str_tuple
	overlap_value = overlap_dict[str_tuple]
	seq_list.remove(x)
	seq_list.remove(y)
	x = x[:-overlap_value]
	new_string = x + y
	seq_list.append(new_string)
	overlap_dict.clear()



def compute_overlap(string1, string2):
	overlap = 0
	len1 = len(string1)
	len2 = len(string2)
	i = 1
	min_len = min(len1, len2)
	while i < min_len:
		if string1[-i:] == string2[:i]:
			overlap_dict[(string1, string2)] = i
		i+=1
	

def find_superstring(seq_list):
	while not len(seq_list) == 1:
		for i in range(len(seq_list) - 1):
			for j in range(i+1, len(seq_list)):
				compute_overlap(seq_list[i], seq_list[j])
				compute_overlap(seq_list[j], seq_list[i])
				pass
		compute_superstring(seq_list)

	return seq_list[0]

for fasta_seq in sequences:
	name, value = fasta_seq.id, str(fasta_seq.seq)
	seq_dict[name] = value

seq_list = list(seq_dict.values())
superstring = find_superstring(seq_list)
print superstring
