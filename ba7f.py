import re
alphabet = ['A','C','G','T']

def smallParsimony(graph,leaf_nodes,nodes,root,idx):
	scoreA = dict()
	scoreC= dict()
	scoreG = dict()
	scoreT = dict()
	tag = dict()
	for node in nodes:
		tag[node] = 0
		if node in leaf_nodes:
			tag[node] = 1
			scoreA[node] = 99999
			scoreC[node] = 99999
			scoreG[node] = 99999
			scoreT[node] = 99999
			if node[idx] == "A":
				scoreA[node] = 0
			elif node[idx] == "C":
				scoreC[node] = 0
			elif node[idx] == "G":
				scoreG[node] == 0
			elif node[idx] == "T":
				scoreT[idx] = 0

	ripeNode = getRipeNode(graph,tag)
	while ripeNode:
		tag[ripeNode] = 1
		





def constructGraph(edges):
	graph = dict()
	nodes = set()
	child_nodes = set()
	for edge in edges:
		s,e = edge.split('->')
		nodes.add(s)
		nodes.add(e)
		child_nodes.add(e)
		s = s.strip()
		e = e.strip().split()
		try:
			graph[s].extend(e)
		except:
			graph[s] = e
	
	root = nodes - child_nodes
	return(graph,nodes,root)


leaf_pattern = re.compile("[A,C,G,T]+")
file = open("test.txt","r")
edges = file.read().splitlines()
n = edges[0]
del edges[0]
scores = []

graph, nodes, root = constructGraph(edges)
leaf_nodes = set()
for node in nodes:
	if leaf_pattern.match(node):
		leaf_nodes.add(node)
idx = 0
leaf = next(iter(leaf_nodes))
print(graph)
"""
while idx < len(leaf):
	scores.append(smallParsimony(graph,leaf_nodes,nodes,root,idx))
	break
"""