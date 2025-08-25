import heapq
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append((b, cost))
    
distance = [10**9 for _ in range(N+1)]
def dijkstra(x):
    distance[x] = 0
    queue = []
    heapq.heappush(queue, (0, x))
    
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for item in graph[now]:
            node = item[0]
            cost = item[1]
            temp = dist + cost
            if temp < distance[node]:
                distance[node] = temp
                heapq.heappush(queue, (temp, node))
    
A, B = map(int, sys.stdin.readline().split())
dijkstra(A)
print(distance[B])