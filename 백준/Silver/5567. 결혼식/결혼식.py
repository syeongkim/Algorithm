n = int(input())
m = int(input())

friends = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
    
invite = []
sang = friends[1]

for i in sang:
    invite.append(i)
    temp = friends[i]
    for j in temp:
        if j not in invite and j != 1:
          invite.append(j)
            
print(len(list(set(invite))))