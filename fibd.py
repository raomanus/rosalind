file = open("rosalind_fibd.txt","r")
line = file.readline()
line = line.strip()

line = line.split()
n = int(line[0])
m = int(line[1])

r1 = 1
r2 = 1
arr = [0,1,1]
for i in range (3, m+1):
	temp = r2 + r1
	r1 = r2
	r2 = temp
	arr.append(r2)

for i in range(m+1,n+1):
	idx = i-(m+1)
	if idx == 0:
		temp = r2 + r1 - 1
	else:
		temp = r2 + r1 - arr[idx]
	r1 = r2
	r2 = temp
	arr.append(r2)


print(r2)