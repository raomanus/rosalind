import math
input_file = open("rosalind_prob.txt", 'r')

lines = input_file.readlines()
count_gc = 0
count_at = 0
b = []
dna_string = lines[0]

# calculating number of GC and AT occurences in the DNA string
count_gc = dna_string.count('G') + dna_string.count('C')
count_at = dna_string.count('A') + dna_string.count('T')

#getting the list of GC values from A
gc_list = lines[1].split()

for gc_count in gc_list:
	gc_percentage = float(gc_count)/2
	at_percentage = 0.5 - gc_percentage
	gc_percentage = gc_percentage**count_gc
	at_percentage = at_percentage**count_at
	b.append(float("{0:.3f}".format(math.log10(gc_percentage*at_percentage))))

output = ""

#formatting the output in the required string form
for i in b:
	output = output + str(i) + " "

print(output)