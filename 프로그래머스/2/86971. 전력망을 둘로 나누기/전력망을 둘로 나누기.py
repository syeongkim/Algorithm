from collections import deque

def solution(n, wires):
    answer = n
    for i in range(len(wires)):
        graph = [[] for _ in range(n + 1)]
        for wire in wires:
            if wires[i] != wire:
                a, b = wire[0], wire[1]
                graph[a].append(b)
                graph[b].append(a)
        cnt = 0
        visited = [0 for _ in range(n+1)]
        q = deque()
        for j in range(1, n+1):
            if len(graph[j]) > 0 and visited[j] == 0:
                q.append(j)
                while q:
                    prev = q.popleft()
                    visited[prev] = 1
                    cnt += 1
                    nextNodes = graph[prev]
                    for node in nextNodes:
                        if visited[node] == 0:
                            q.append(node)
                diff = abs(n - cnt - cnt)
                answer = min(diff, answer)
                if answer == 0:
                    return 0
        
    return answer