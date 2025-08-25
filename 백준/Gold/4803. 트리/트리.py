import sys

def dfs(x, parent):
    visited[x] = 1
    for nxt in graph[x]:
        if visited[nxt] == 0:
            if not dfs(nxt, x):
                return False
        elif nxt != parent:
            return False
    return True

cnt = 0
while True:
    cnt += 1
    n, m = map(int, sys.stdin.readline().split())
    if (n == 0 and m == 0):
        break

    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    tree = 0
    for i in range(1, n+1):
        if visited[i] == 0:
            res = dfs(i, -1)
            if res == True:
                tree += 1
        else:
            continue

    if (tree == 0):
        print(f"Case {cnt}: No trees.")
    elif (tree == 1):
        print(f"Case {cnt}: There is one tree.")
    else:
        print(f"Case {cnt}: A forest of {tree} trees.")
    