n = int(input())

pinaryNumberLists = [[] for i in range(n+1)]
pinaryNumberLists[0] = 0
pinaryNumberLists[1] = 1

if (n == 1):
    pass
else:
    for i in range(2, n+1):
        pinaryNumberLists[i] = pinaryNumberLists[i-2] + pinaryNumberLists[i-1]
                
print(pinaryNumberLists[n])