file = open("rosalind_dna.txt","r");
count_a = 0;
count_c = 0;
count_g = 0;
count_t = 0;

for line in file:
	count_a += line.count('A');
	count_c += line.count('C');
	count_g += line.count('G');
	count_t += line.count('T');

file.close();
print(count_a, count_c, count_g, count_t);