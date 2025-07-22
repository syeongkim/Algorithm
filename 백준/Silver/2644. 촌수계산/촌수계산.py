n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
  parent, child = map(int, input().split())
  graph[parent].append(child)
  graph[child].append(parent)

def dfs(a, b, cnt):
  if (a == b):
    print(cnt)
    exit()
  else:
    cnt += 1
    visited[a] = 1
    queue = graph[a]
    for i in queue:
      if (visited[i] == 0):
        dfs(i, b, cnt)

cnt = 0
dfs(a, b, cnt)
print(-1)