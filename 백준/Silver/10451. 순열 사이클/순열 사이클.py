T = int(input())

def visit(v):
    visited[v] = 1
    next = sun[v]
    if (visited[next] == 0):
        visit(next)

for i in range(T):
    n = int(input())
    sun = list(map(int, input().split()))
    sun.insert(0, 0)
    visited = [0] * (n + 1)
    cnt = 0

    for i in range(1, n + 1):
        if (visited[i] == 0):
            visit(i)
            cnt += 1
    print(cnt)