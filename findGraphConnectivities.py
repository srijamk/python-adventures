#python3

import sys
global cc
cc = 0

def explore(graph, vertex, visited):
    visited[vertex] = True
    global cc
    ccNumber[vertex] = cc
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            explore(graph, neighbor, visited)

def dfs(graph, neighbor, visited):
    for nodeIndex in range(1, len(graph)):
        if not visited[nodeIndex]:
            explore(graph, nodeIndex, visited)
            global cc
            cc += 1
    return cc

inputs = sys.stdin.read()
tokens = list(map(int, inputs.split()))
numVertices = int(tokens[0])
ccNumber = [0 for i in range(numVertices + 1)]
graph = [[] for i in range(numVertices + 1)]
numEdges = tokens[1]
tokens = tokens[2:]
for i in range(0, len(tokens) - 1, 2):
    graph[tokens[i]].append(tokens[i + 1])
    graph[tokens[i + 1]].append(tokens[i])
    
print(dfs(graph, 1, [False for i in range(numVertices + 1)]))
