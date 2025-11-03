from collections import deque

def solution(n, results):
    answer = 0
    winGraph = [[] for _ in range(n+1)]
    loseGraph = [[] for _ in range(n+1)]
    
    for result in results:
        a, b = result[0], result[1]
        winGraph[a].append(b)
        loseGraph[b].append(a)
        
    for i in range(1, n+1):
        for node in winGraph[i]:
            for loseNode in loseGraph[i]:
                if loseNode not in loseGraph[node]:
                    loseGraph[node].append(loseNode)
            
        for node in loseGraph[i]:
            for winNode in winGraph[i]:
                if winNode not in winGraph[node]:
                    winGraph[node].append(winNode)
            
    for i in range(1, n+1):
        if len(winGraph[i]) + len(loseGraph[i]) == n-1:
            answer += 1
        
    return answer