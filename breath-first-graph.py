graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = []
start = '5'
goal = '4'

def bfs(graph, node):
   queue = []
   queue.append(node)
   visited.append(node)
    
   while queue:
      n = queue.pop(0)
      if n == goal:
         break

      for child in graph[n]:
         if child not in visited:
          queue.append(child)
          visited.append(child)
    

#Start
print("Breadth-First Search: graph tree")
bfs(graph, start)
print(*visited)