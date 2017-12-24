from Bio import SeqIO
import csv

seq_list = []
protein_string = ""

# Input dataset file
input_file = open("rosalind_splc.txt",'r')		
sequences = SeqIO.parse(input_file,'fasta')

# CSV file containing the RNA Codon table. Entries are of type UUA,L
rna_codon_file = open("RNA_Codon_table", 'r')		
reader = csv.reader(rna_codon_file)

# Converting CSV file to dictionary 
rna_codon_table = {line[0]:line[1] for line in reader}		

# Extracting the given sequences
for fasta_seq in sequences:
	seq_list.append(str(fasta_seq.seq))		  

# Taking the longest sequence in input file as the DNA input sequence and removing it from the list of sequences
dna_string = max(seq_list, key=len)
seq_list.remove(dna_string)		

for substring in seq_list:
	dna_string = dna_string.replace(substring,'')

dna_string = dna_string.replace('T','U')

for i in range(0, len(dna_string), 3):
	sub = dna_string[i:i+3]
	# Concatinating protein sequence
	protein_string = protein_string+rna_codon_table.get(sub)		
	pass
#printing the protein sequence
print(protein_string.replace('Stop',''))