import sys

global maxX
global maxY
global maxSteps
global minDiff
global visited
global M

minDiff = sys.maxsize

def pails(file_name):
    f = open(file_name, 'r')
    g = open('pails.out', 'w')
    lines = f.read().splitlines()
    boiler = list(map(int, lines[0].split()))
    global maxX
    maxX = boiler[0]
    global maxY
    maxY = boiler[1]
    global maxSteps
    maxSteps = boiler[2]
    global M
    M = boiler[3]
    global visited
    visited = [[False for i in range(maxY + 1)] for j in range(maxX + 1)]
    explore(0, 0, 0)
    g.write("%i\n" % minDiff)

def explore(X, Y, K):
    if visited[X][Y]:

        global minDiff
        minDiff = min(minDiff, abs(M - (X + Y)))
        return minDiff
    if K >= maxSteps:
        minDiff = min(minDiff, abs(M - (X + Y)))
        return minDiff
    visited[X][Y] = True
    explore(maxX, Y, K + 1)
    explore(X, maxY, K + 1)
    explore(0, Y, K + 1)
    explore(X, 0, K + 1)
    if X >= (maxY - Y):
        explore(X - (maxY - Y), maxY, K + 1)
    elif X < (maxY - Y):
        explore(0, X + Y, K + 1)
    if Y >= (maxX - X):
        explore(maxX, Y - (maxX - X), K + 1)
    elif Y < (maxX - X):
        explore(X + Y, 0, K + 1)    

pails('pails.in')
