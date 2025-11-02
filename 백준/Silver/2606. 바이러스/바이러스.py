from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
answer = 0
visited = [0 for _ in range(N+1)]
queue = deque([1])
visited[1] = 1
while queue:
    curr = queue.popleft()
    nextNodes = graph[curr]
    for node in nextNodes:
        if visited[node] == 0:
            queue.append(node)
            visited[node] = 1
            
print(visited.count(1) - 1)