def Count(pos, symbol, lastCol):
	return lastCol[:pos].count(symbol)

def BWMatching(firstCol, lastCol, pattern):
	top = 0
	bottom = len(lastCol) - 1
	while top <= bottom:
		if pattern:
			symbol = pattern[-1:]
			pattern = pattern[:-1]
			searchSpace = lastCol[top:bottom+1]
			if symbol in searchSpace:
				top = firstOccurrence[symbol] + Count(top, symbol, lastCol)
				bottom = firstOccurrence[symbol] + Count(bottom +1, symbol, lastCol) - 1
			else:
				return 0
		else:
			return bottom - top + 1



file = open("rosalind_ba9m.txt","r")

lastCol = file.readline().rstrip()
patterns = file.readline().split()
firstCol = ''.join(sorted(lastCol))

alphabet = set(firstCol)
firstOccurrence = dict()

for char in alphabet:
	firstOccurrence[char] = firstCol.index(char)

occurrences = list()
for pattern in patterns:
	occurrences.append(BWMatching(firstCol, lastCol, pattern))

print(*occurrences, sep=' ')