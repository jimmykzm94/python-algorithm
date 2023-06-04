# graph = [
#     [0,1,1,0,0],
#     [0,0,1,1,1],
#     [1,0,0,1,1],
#     [1,1,0,1,1],
#     [1,1,0,0,0]
# ]

graph = [
    [0,0,1,0,0],
    [1,0,1,1,1],
    [0,0,0,1,1],
    [0,1,0,1,1],
    [0,1,0,0,0]
]

visited = [[0 for _ in range(len(graph[0]))] for _ in range(len(graph))]
start = (0,0)
goal = (4,0)

def adjacent(graph, index):
    output = []
    lastIndex_i = len(graph) - 1
    lastIndex_j = len(graph[0]) - 1
    offsets = [(-1,0), (1,0), (0,-1), (0,1)]

    for dx, dy in offsets:
        x,y = index[0] + dx, index[1] + dy
        if 0 <= x <= lastIndex_i and 0 <= y <= lastIndex_j:
            if not visited[x][y] and graph[x][y] != 1:
                output.append((x,y))
            
    return output

def bfs(graph, start):
    queue = []
    queue.append(start)
    visited[start[0]][start[1]] = 1

    while queue:
        index = queue.pop(0)
        if index == goal:
            break

        for neighbor in adjacent(graph, index):
            queue.append(neighbor)
            visited[neighbor[0]][neighbor[1]] = 1

print('Breath')
bfs(graph,start)
print(*visited)