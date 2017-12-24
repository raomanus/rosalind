file = open("rosalind_ba9k_437_1_dataset.txt", "r")

transform = file.readline()
transform = transform.rstrip()
pos = int(file.readline())

char_at_pos = transform[pos]
rank_table = dict()

for i in range(len(transform)):
	try:
		rank_table[transform[i]].append(i)
	except:
		rank_table[transform[i]] = [i]

rank_of_char = rank_table[char_at_pos].index(pos)
transform = sorted(transform)

pos_in_first = transform.index(char_at_pos) + rank_of_char
print(pos_in_first)