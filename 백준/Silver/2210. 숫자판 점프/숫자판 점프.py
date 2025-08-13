numberBoard = []
answer = []

for _ in range(5):
    numberBoard.append(input().split())

def findAnswer(i, j, number):
    number += numberBoard[i][j]
    if len(number) == 6:
        answer.append(number)
        return 0
    if i > 0:
        findAnswer(i-1, j, number)
    if j > 0:
        findAnswer(i, j-1, number)
    if i < 4:
        findAnswer(i+1, j, number)
    if j < 4:
        findAnswer(i, j+1, number)
    
for i in range(5):
    for j in range(5):
        findAnswer(i, j, "")
        
answer = set(answer)
print(len(answer))