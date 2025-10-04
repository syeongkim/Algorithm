from collections import deque

def solution(priorities, location):
    answer = 0
    runningOrder = []
    queue = deque()
    
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))
        
    while queue:
        item = queue.popleft()
        num, priority = item[0], item[1]
        if priority == max(priorities):
            runningOrder.append(num)
            priorities.remove(priority)
        else:
            queue.append((num, priority))
            
    answer = runningOrder.index(location) + 1
    return answer