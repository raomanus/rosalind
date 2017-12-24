import csv

input_file = open("rosalind_mrna.txt", 'r')
rna_codon_file = open("RNA_Codon_table", 'r')
reader = csv.reader(rna_codon_file)

rna_codon_table = {line[0]:line[1] for line in reader}
protein_list = list(rna_codon_table.values())

for line in input_file:
	product = 1
	seq_list = list(line.strip())
	seq_list.append("Stop")
	for char in seq_list:
		count_char = protein_list.count(char)
		product *=count_char
	
	mod_value = product % 1000000
	print(mod_value)
