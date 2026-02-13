from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        for v in range(self.V):
            if not visited[v]:
                self.topological_sort_util(v, visited, stack)

        return stack

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor,visited, stack)
        
        stack.insert(0,v)

if __name__ == "__main__":
    g = Graph(3)
    g.add_edge(0,1)
    g.add_edge(0,2)
    print(g.topological_sort())

    """
    # Start: visited = [False, False, False, False, False, False]
    #                   node0  node1  node2  node3  node4  node5

    topological_sort_util(5, visited, stack)
        visited[5] = True
        # Now: visited = [False, False, False, False, False, True]
        #                                                    ↑ only node 5
        
        for neighbor in self.graph[5]:   # neighbors are [2, 0]
            
            # First: neighbor = 2
            if not visited[2]:   # visited[2] is False → True → go in
                topological_sort_util(2, visited, stack)
                    visited[2] = True
                    # Now: visited = [False, False, True, False, False, True]
                    
                    for neighbor in self.graph[2]:   # neighbors are [3]
                        if not visited[3]:   # False → go in
                            topological_sort_util(3, ...)
                                visited[3] = True
                                # and so on...
    """
    