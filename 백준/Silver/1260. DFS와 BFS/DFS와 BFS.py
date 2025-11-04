from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(N+1):
    graph[i].sort()
    
# dfs
dfsVisited = [0 for _ in range(N+1)]
def dfs(node):
    dfsVisited[node] = 1
    print(node, end=' ')
    for next in graph[node]:
        if dfsVisited[next] == 0:
            dfs(next)
dfs(V)
dfsVisited[V] = 1
print()

# bfs
bfsQueue = deque([V])
bfsVisited = [0 for _ in range(N+1)]
bfsVisited[V] = 1
while bfsQueue:
    curr = bfsQueue.popleft()
    print(curr, end=' ')
    for next in graph[curr]:
        if bfsVisited[next] == 0:
            bfsVisited[next] = 1
            bfsQueue.append(next)