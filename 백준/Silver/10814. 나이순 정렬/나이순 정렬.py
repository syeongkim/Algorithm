judge = []

num = int(input())
for _ in range(num):
    age, name = input().split()
    judge.append([int(age), name])

judge = sorted(judge, key = lambda x: x[0])

for i in judge:
    print(i[0], i[1])