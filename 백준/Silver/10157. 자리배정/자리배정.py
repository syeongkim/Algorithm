C, R = map(int, input().split())
K = int(input())
visited = [[0] * (C+1) for _ in range(R+1)]
    
if (K > C * R):
    print(0)
    exit()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0
x = 1
y = 1
visited[y][x] = 1
for i in range(K-1):
    next_x = x + dx[d]
    next_y = y + dy[d]
    if (next_x > 0 and next_x <= C and next_y > 0 and next_y <= R and visited[next_y][next_x] == 0):
        visited[next_y][next_x] = 1
        x = next_x
        y = next_y
    else:
        d = (d+1)%4
        x += dx[d]
        y += dy[d]
        visited[y][x] = 1

print(x, y)