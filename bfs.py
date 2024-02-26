from collections import deque
graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': ['F'],
  'F': [],
}
def bfs(graph, start):
  visited = set() 
  queue = deque([start])
  while queue:
    node = queue.popleft()
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.append(neighbor)
bfs(graph, 'A')
