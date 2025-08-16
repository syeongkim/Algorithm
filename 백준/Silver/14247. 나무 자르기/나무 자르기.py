n = int(input())
tree = list(map(int, input().split()))
grow = list(map(int, input().split()))
treeGrowList = []

for i in range(n):
    treeGrowList.append((tree[i], grow[i]))

treeGrowList.sort(key = lambda x: x[1])

sum = 0
for i in range(n):
    sum += treeGrowList[i][0] + i * treeGrowList[i][1]
    
print(sum)