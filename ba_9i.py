def LastToFirst(char_at_pos, pos, firstCol):
	rank_of_char = rank_table[char_at_pos].index(pos)
	pos_in_first = firstCol.index(char_at_pos) + rank_of_char
	return pos_in_first

def BWMatching(firstCol, lastCol, pattern):
	top = 0
	bottom = len(lastCol) - 1
	while top <= bottom:
		if pattern:
			symbol = pattern[-1:]
			pattern = pattern[:-1]
			searchSpace = lastCol[top:bottom+1]
			if symbol in searchSpace:
				topIndex = searchSpace.index(symbol) + top
				bottomIndex = searchSpace.rfind(symbol) + top
				top = LastToFirst(symbol, topIndex, firstCol)
				bottom = LastToFirst(symbol, bottomIndex, firstCol)
			else:
				return 0
		else:
			return bottom - top + 1



file = open("test.txt","r")

lastCol = file.readline().rstrip()
patterns = file.readline().split()
firstCol = ''.join(sorted(lastCol))

rank_table = dict()
for i in range(len(lastCol)):
	try:
		rank_table[lastCol[i]].append(i)
	except:
		rank_table[lastCol[i]] = [i]

occurrences = list()
for pattern in patterns:
	occurrences.append(BWMatching(firstCol, lastCol, pattern))

print(*occurrences, sep=' ')

