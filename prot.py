import csv

input_file = open("rosalind_prot.txt", 'r')
rna_codon_file = open("RNA_Codon_table", 'r')		
reader = csv.reader(rna_codon_file)

# Converting CSV file to dictionary 
rna_codon_table = {line[0]:line[1] for line in reader}

protein_string = ""

for line in input_file:
	line = line.strip()
	for i in range(0, len(line), 3):
		sub = line[i:i+3]
		# Concatinating protein sequence
		protein_string = protein_string+rna_codon_table.get(sub)		
		pass

#printing the protein sequence
print(protein_string.replace('Stop',''))