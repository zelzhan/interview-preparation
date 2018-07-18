"""Given a directed graph, design an algorithm to find out whether there is a
route between two nodes."""

#Comlexity O(V+E)
def BFS(graph, root, target):
  visited = []
  queue = []
  queue.append(root)
  while queue:
    node = queue.pop(0)
    if node not in visited:
      visited.append(node)
      neighboors = graph[node]
      for neighboor in neighboors:
        queue.append(neighboor)
  if target in visited: return True
  return False



if __name__ == '__main__':
  graph = {'A': ['B', 'C'],
         'B': ['E', 'D'],
         'C': ['D'],
         'D': ['F'],
         'E': ['F'],
         'F': [],
         'G': []}
  print(BFS(graph, 'F', 'A'))
  
