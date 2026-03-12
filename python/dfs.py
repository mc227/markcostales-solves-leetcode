class Graph:
    def __init__(self, size):
        self.adj_list = [[] for _ in range(size)]

    def add_edge(self, start, end):
        self.adj_list[start].append(end)
        self.adj_list[end].append(start)


def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []
    visited.add(start)
    order.append(start)
    for neighbor in graph.adj_list[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return visited, order


if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)

    print("Graph:")
    print("    0")
    print("   / \\")
    print("  1   2")
    print(" / \\   \\")
    print("3   4   5")
    print()

    print("Adjacency list:")
    for i, neighbors in enumerate(g.adj_list):
        print(f"  {i}: {neighbors}")

    print()
    result, order = dfs(g, 0)
    print(f"DFS visited: {result}")
    print(f"DFS order:   {order}")