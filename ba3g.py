def findEulerPath(graph, start):
	path = []
	stack = [start]
	location = graph[start].pop()
	keys = list(graph.keys())
	while len(stack) != 0:
		if (location not in keys) or (len(graph[location]) == 0):
			path.append(location)
			location = stack.pop()
		else:
			stack.append(location)
			location = graph[location].pop()
	path.append(start)
	return path[::-1]

def constructGraph(edges):
	graph = dict()
	inDegree = dict()
	outDegree = dict()
	for edge in edges:
		s,e = edge.split('->')
		s = s.strip()
		e = e.strip().split(',')
		try:
			graph[s].extend(e)
		except:
			graph[s] = e
		try:
			outDegree[s] += len(e)
		except:
			outDegree[s] = len(e)
		for end in e:
			try:
				inDegree[end] += 1
			except:
				inDegree[end] = 1

	return(graph,outDegree,inDegree)

file = open("rosalind_ba3g.txt","r")
edges = file.read().splitlines()
start = None

graph,outDegree,inDegree = constructGraph(edges)

inKeys = list(inDegree.keys())
outKeys = list(outDegree.keys())

for ik in outKeys:
	if ik in inKeys:
		if inDegree[ik] < outDegree[ik]:
			start = ik
	else:
		start = ik

path = findEulerPath(graph, start)
output = path[0]

for node in path[1:]:
	output += "->"+node

print(output)