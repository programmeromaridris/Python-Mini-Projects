

graph = {
   "A": {"B": 3, "C": 3},
   "B": {"A": 3, "D": 3.5, "E": 2.8},
   "C": {"A": 3, "E": 2.8, "F": 3.5},
   "D": {"B": 3.5, "E": 3.1, "G": 10},
   "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
   "F": {"G": 2.5, "C": 3.5},
   "G": {"F": 2.5, "E": 7, "D": 10},
}

class Graph:
    def __init__(self, graph = {}):
        self.graph = graph # Dictionary for the adjacency list
    
    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph: # Check if the node is already added
            self.graph[node1] = {} # if not, create the node
        self.graph[node1][node2] = weight # else,  add a connection to its neighbor
        
        
G = Graph(graph=graph)

G.graph        