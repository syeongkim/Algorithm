bingo = []
answer = []
check = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for i in range(5):
    temp = input().split()
    for j in temp:
        bingo.append(j)
    
for i in range(5):
    temp = input().split()
    for j in temp:
        answer.append(j)

def bingoCheck(check):
    cnt = 0
    for row in check:
        if row == [1, 1, 1, 1, 1]:
            cnt += 1

    for i in range(5):
        col = []
        for j in range(5):
            col.append(check[j][i])
        if col == [1, 1, 1, 1, 1]:
            cnt += 1

    diag = True
    for i in range(5):
        if check[i][i] == 0:
            diag = False
            break
    if (diag == True):
        cnt += 1

    diag = True
    for i in range(5):
        if check[i][4-i] == 0:
            diag = False
            break
    if (diag == True):
        cnt += 1
    return cnt

for i in range(25):
    ans = answer[i]
    idx = bingo.index(ans)
    row = idx // 5
    col = idx % 5
    check[row][col] = 1
    if bingoCheck(check) >= 3:
        print(i+1)
        break