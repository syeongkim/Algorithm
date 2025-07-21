import sys
sys.setrecursionlimit(10**7)

n, m =  sys.stdin.readline().split()
n = int(n)
m = int(m)
vertex = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    vertex[a].append(b)
    vertex[b].append(a)
    
def cc(vertex, v, visited):
    visited[v] = 1
    for k in vertex[v]:
        if (visited[k] == 0):
            visited[k] = 1
            cc(vertex, k, visited)
    
cnt = 0
for i in range(1, n+1, 1):
    if visited[i] == 0:
        cc(vertex, i, visited)
        cnt += 1
        
print(cnt)