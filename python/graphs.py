def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    for neighbor in graph.adj_list[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
        

    return visited
    
    


class Graph:
    def __init__(self, size):
        self.adj_list = [[] for _ in range(size)]

    def add_edge(self, start, end):
        self.adj_list[start].append(end)
        self.adj_list[end].append(start)


if __name__ == "__main__":
    graph = Graph(7)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,3)
    graph.add_edge(1,4)
    graph.add_edge(2,5)
    graph.add_edge(2,6)


    print(dfs(graph,0))