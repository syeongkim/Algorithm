R, C = map(int, input().split())
map = []
map.append(['.']*(C+2))
for _ in range(R):
    temp = list(input())
    temp.insert(0, '.')
    temp.append('.')
    map.append(temp)
map.append(['.']*(C+2))

disappear = []
for i in range(R+2):
    for j in range(C+2):
        if (map[i][j] == 'X'):
            cnt = 0
            if (map[i-1][j] == '.'):
                cnt += 1
            if (map[i+1][j] == '.'):
                cnt += 1
            if (map[i][j-1] == '.'):
                cnt += 1
            if (map[i][j+1] == '.'):
                cnt += 1
            if (cnt >= 3):
                disappear.append([i, j])

for location in disappear:
    map[location[0]][location[1]] = '.'

xmin = 11
xmax = -1
ymin = 11
ymax = -1
for i in range(R+2):
    for j in range(C+2):
        if (map[i][j] == 'X'):
            if (i < ymin):
                ymin = i
            if (i > ymax):
                ymax = i
            if (j < xmin):
                xmin = j
            if (j > xmax):
                xmax = j

for i in range(ymin, ymax+1, 1):
    for j in range(xmin, xmax+1, 1):
        print(map[i][j], end = '')
    print('')