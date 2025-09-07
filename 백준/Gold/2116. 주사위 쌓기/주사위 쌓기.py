N = int(input())
dices = []
idx = [5, 3, 4, 1, 2, 0]

for _ in range(N):
    dices.append(list(map(int, input().split())))
    
answer = 0

for i in range(6):
    sum = 0
    bottom = dices[0][i]
    for j in range(N):
        bottomIdx = dices[j].index(bottom)
        up = dices[j][idx[bottomIdx]]
        sides = []
        for x in dices[j]:
            if x != bottom and x != up:
                sides.append(x)
        sum += max(sides)
        bottom = up
    answer = max(answer, sum)
    
print(answer)