file = open("rosalind_ba9i.txt","r");

text = file.readline()
text = text.rstrip()
i = len(text)-1
rotations = []

while i > -1:
	last_char = text[-1:]
	text = text[:-1]
	text = last_char + text
	rotations.append(text)
	i -= 1

rotations = sorted(rotations)
bwt_string = ''

for rotation in rotations:
	bwt_string += rotation[-1:]

print(bwt_string)
