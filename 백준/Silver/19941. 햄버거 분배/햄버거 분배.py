N, K = map(int, input().split())
location = input()
visited = []

for i in location:
    if i == 'H':
        visited.append(0)
    else:
        visited.append(-1)
        
for i in range(N):
    if location[i] == 'P':
        start = i - K
        end = i + K 
        if start < 0:
            start = 0
        if end > N - 1:
            end = N - 1
        for j in range(start, end+1, 1):
            if visited[j] == 0:
                visited[j] = 1
                break

print(visited.count(1))