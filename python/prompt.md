Here's a prompt you can use:

---

**Prompt:**

Trace through this code step by step, showing:
1. The value of `visited` after each change
2. Each recursive call with its arguments
3. What `stack` looks like after each `stack.insert(0, v)`

```python
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
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
                self.topological_sort_util(neighbor, visited, stack)
        stack.insert(0, v)

if __name__ == "__main__":
    g = Graph(3)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    print(g.topological_sort())
```

Show me the graph visually first, then trace the execution.

---

Want me to run this trace for you now?