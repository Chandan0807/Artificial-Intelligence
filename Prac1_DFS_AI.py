# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:
        
        # Constructor
        def __init__(self):
                # default dictionary to store graph
                self.graph = defaultdict(list)

        # function to add an edge to graph
        def addEdge(self,u,v):
                self.graph[u].append(v)

        # Function to print a BFS of graph
        def DFSUtil(self, v, visited):
                visited[v] = True
                print(v, end = " ")

                for i in self.graph[v]:
                        if visited[i] == False:
                            self.DFSUtil(i, visited)

                            def DFSUtil(self, v):
                                    visited = [False] * (len(self.graph))
                                    self.DFSUtil(v, visited)
# Driver code

# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print ("Following is Depth First Traversal" " (starting from vertex 2)")
g.DFS(2)
