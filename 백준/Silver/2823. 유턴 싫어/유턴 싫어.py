import sys

R, C = map(int, sys.stdin.readline().split())
map = []

for _ in range(R):
    map.append(list(sys.stdin.readline()))
    
for i in range(R):
    for j in range(C):
        if map[i][j] == 'X':
            continue
        cnt = 0
        if i > 0 and map[i-1][j] == '.':
            cnt += 1
        if i < R-1 and map[i+1][j] == '.':
            cnt += 1
        if j > 0 and map[i][j-1] == '.':
            cnt += 1
        if j < C-1 and map[i][j+1] == '.':
            cnt += 1
        if cnt < 2:
            print(1)
            exit()

print(0)