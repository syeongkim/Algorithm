from collections import deque
answer = []

N, M = map(int, input().split())

queue = deque()
for i in range(1, N+1):
    queue.append([i])
    
while queue:
    curr = queue.popleft()
    if len(curr) == M:
        answer.append(curr)
    else:
        for n in range(1, N+1):
            if n not in curr:
                queue.append(curr + [n])
                
for item in answer:
    item.sort()
    
answer = list(set(tuple(item) for item in answer))
answer.sort()
for item in answer:
    for number in item:
        print(number, end=' ')
    print()