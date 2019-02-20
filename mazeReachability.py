#python3

import sys

global pathExists
pathExists = 0

def explore(graph, vertex, goalVertex, visited):
    visited[vertex] = True
    
    if (vertex == goalVertex):
        global pathExists
        pathExists = 1

    else:
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                explore(graph, neighbor, goalVertex, visited)

inputs = sys.stdin.read()
tokens = list(map(int, inputs.split()))

numVertices = int(tokens[0])
graph = [[] for i in range(numVertices + 1)]
numEdges = tokens[1]
tokens = tokens[2:]
for i in range(0, len(tokens) - 3, 2):
    graph[tokens[i]].append(tokens[i + 1])
    graph[tokens[i + 1]].append(tokens[i])
    
query = [tokens[-2], tokens[-1]]
explore(graph, query[0], query[1], [False for i in range(numVertices + 1)])
print(pathExists)
