from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    distance = [-1 for _ in range(n+1)]
    
    for node in edge:
        graph[node[0]].append(node[1])
        graph[node[1]].append(node[0])
    
    queue = deque([1])
    distance[1] = 0
    
    while queue:
        curr = queue.popleft()
        adjacents = graph[curr]
        for n in adjacents:
            if distance[n] == -1:
                queue.append(n)
                distance[n] = distance[curr] + 1
                
    maxDistance = max(distance)
    for d in distance:
        if d == maxDistance:
            answer += 1
    return answer