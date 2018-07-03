import sys

class ComeHome:
    def __init__(self):

        f = open('comehome.in', 'r')
        self.n = int(f.readline())
                
        self.vertices = []

        for i in range(self.n):
            line = f.readline().strip("\n").split(" ")
            first = line[0]
            second = line[1]
            dist = int(line[2])

            if first not in self.vertices:
                if first == 'Z':
                    self.vertices.insert(0, first)
                else:
                    self.vertices.append(first)
            if second not in self.vertices:
                if second == 'Z':
                    self.vertices.insert(0, second)
                else:
                    self.vertices.append(second)

        f = open('comehome.in', 'r')
        self.n = int(f.readline())
        
        self.reported = [[0 for i in range(len(self.vertices))] for i in range(len(self.vertices))]

        for i in range(self.n):
            line = f.readline().strip("\n").split(" ")
            first = line[0]
            second = line[1]
            dist = int(line[2])
            first_reported = self.reported[self.vertices.index(first)][self.vertices.index(second)]
            if (first_reported > 0 and dist < first_reported) or first_reported == 0:
                print(first, second, dist)
                self.reported[self.vertices.index(first)][self.vertices.index(second)] = dist
                self.reported[self.vertices.index(second)][self.vertices.index(first)] = dist

        self.visited = [False for i in range(len(self.vertices))]
        self.distance = [sys.maxsize for i in range(len(self.vertices))]
        self.parent = [None for i in range(len(self.vertices))]

        print(self.reported)
        
    def solve(self):

        source = 0
        self.visited[source] = True
        self.distance[source] = 0

        current = source
        
        while False in self.visited:

            print(self.distance)
            
            neighbors = self.reported[current]
            self.visited[current] = True
            
            for n in range(len(neighbors)):
                if self.distance[current] + neighbors[n] < self.distance[n] and self.visited[n] == False and neighbors[n] > 0:
                    self.distance[n] = self.distance[current] + neighbors[n]
                    self.parent[n] = current

            min_dist = sys.maxsize
            min_vertex = None
            for i in range(len(self.distance)):
                if self.distance[i] < min_dist and self.visited[i] == False:
                    min_dist = self.distance[i]
                    min_vertex = i

            current = min_vertex

        min_dist = sys.maxsize
        min_vertex = None
        for i in range(len(self.vertices)):
            if ord(self.vertices[i]) < 90 and self.distance[i] < min_dist:
                min_dist = self.distance[i]
                min_vertex = self.vertices[i]

        g = open('comehome.out', 'w')
        g.write(min_vertex + (" %i\n") % min_dist)
        #print(self.vertices)

C = ComeHome()
C.solve()
