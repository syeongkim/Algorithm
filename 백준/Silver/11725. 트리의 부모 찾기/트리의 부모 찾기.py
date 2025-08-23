import sys
sys.setrecursionlimit(10**6) 

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0 for _ in range(N+1)]
def findParentNode(node):
    for child in tree[node]:
        if visited[child] == 0:
            visited[child] = node
            findParentNode(child)

findParentNode(1)

for i in visited[2:]:
    print(i)