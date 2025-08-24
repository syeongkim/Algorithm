import heapq
import sys

N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    
distance = [10**9] * (N+1)
def dijkstra(X):
    distance[X] = 0
    queue = []
    heapq.heappush(queue, (0, X))
    
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + 1
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(queue, (cost, node))
                
dijkstra(X)
    
ans = []
for i in range(1, N+1, 1):
    if distance[i] == K:
        ans.append(i)
    
if len(ans) == 0:
    print("-1")
else:
    for node in ans:
        print(node)