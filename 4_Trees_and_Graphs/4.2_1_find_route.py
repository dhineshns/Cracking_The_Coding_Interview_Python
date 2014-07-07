graph = {'a':['c'], 'b':['c'], 'c': ['d'], 'd':['e'], 'e':['f'], 'f':[] }
print graph

def findRoute(graph, start, end, path=[]):
	path.append(start)
	if start == end:
		return path.append(start)
	if end in graph[start]:
		path.append(end) 
		return path
	for i in graph[start]:
		return findRoute(graph, i, end, path)

print findRoute(graph, 'b', 'f')