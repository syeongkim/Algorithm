n, k = input().split()
n = int(n)
k = int(k)
pick = []

for i in range(n):
    pick.append(int(input()))
    
cnt = 0
point = 0
find = False
for i in range(n):
    next = pick[point]
    cnt += 1
    if (next == k):
        find = True
        print(cnt)
        break
    point = next

if (not find):
    print(-1)