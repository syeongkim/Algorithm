import sys

R, C = map(int, sys.stdin.readline().split())
room = [['*' for _ in range(C)] for _ in range(R)]

numOfObstacle = int(sys.stdin.readline())
for _ in range(numOfObstacle):
    br, bc = map(int, sys.stdin.readline().split())
    room[br][bc] = 'x'
    
sr, sc = map(int, sys.stdin.readline().split())
directions = list(map(int, sys.stdin.readline().split()))

def move(r, c, direction):
    if direction == 1:
        r -= 1
    elif direction == 2:
        r += 1
    elif direction == 3:
        c -= 1
    else:
        c += 1
    return r, c

idx = 0
moveCnt = 0
room[sr][sc] = 0
r, c = sr, sc

while True:
    cnt = 0
    for _ in range(len(directions)):
        direction = directions[idx % len(directions)]
        if direction == 1:
            if r == 0 or room[r-1][c] != '*':
                cnt += 1
            else:
                r, c = move(r, c, direction)
                break
            
        elif direction == 2:
            if r == R - 1 or room[r+1][c] != '*':
                cnt += 1
            else:
                r, c = move(r, c, direction)
                break

        elif direction == 3:
            if c == 0 or room[r][c-1] != '*':
                cnt += 1
            else:
                r, c = move(r, c, direction)
                break
            
        else:
            if c == C - 1 or room[r][c+1] != '*':
                cnt += 1
            else:
                r, c = move(r, c, direction)    
                break

        idx += 1
        
    if cnt == len(directions):
        print(r, c)
        break
    else:
        moveCnt += 1
        room[r][c] = moveCnt