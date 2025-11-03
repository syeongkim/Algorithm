N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

answer = 0
cranes.sort(reverse=True)
boxes.sort(reverse=True)

if boxes[0] > cranes[0]:
    answer = -1
else:
    boxPositions = [0] * N
    visited = [0] * M
    count = 0
    
    while count < M:
        for i in range(N):
            while boxPositions[i] < M:
                if visited[boxPositions[i]] == 0 and cranes[i] >= boxes[boxPositions[i]]:
                    visited[boxPositions[i]] = 1
                    boxPositions[i] += 1
                    count += 1
                    break
                boxPositions[i] += 1

        answer += 1
    
print(answer)