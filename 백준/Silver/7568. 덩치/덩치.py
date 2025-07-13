n = int(input())
people = []

for _ in range(n):
    people.append(list(map(int, input().split())))
    
def getRank(element):
    rank = 0
    for i in range(n):
        if ((element[0] < people[i][0]) and (element[1] < people[i][1])):
            rank += 1
    return rank
    
for i in range(n):
    rank = getRank(people[i])
    print(rank + 1, end = ' ')