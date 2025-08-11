H, W = map(int, input().split())
N = int(input())
stickers = []

for _ in range(N):
    sticker = list(map(int, input().split()))
    stickers.append(sticker)
    
def checkAvailable(comb):
    sticker1 = comb[0]
    sticker2 = comb[1]
    if (sticker1[0] + sticker2[0] <= H) and (max(sticker1[1], sticker2[1]) <= W) or (max(sticker1[0], sticker2[0]) <= H) and (sticker1[1] + sticker2[1] <= W):
        return True
    
    return False
    
answer = 0
for i in range(0, N-1, 1):
    for j in range(i+1, N, 1):
        sticker1 = stickers[i]
        sticker2 = stickers[j]
        temp = [[sticker1, sticker2], [[sticker1[1], sticker1[0]], sticker2], [sticker1, [sticker2[1], sticker2[0]]], [[sticker1[1], sticker1[0]], [sticker2[1], sticker2[0]]]]
        for comb in temp:
            isAvailable = checkAvailable(comb)
            if (isAvailable):
                if answer < sticker1[0]*sticker1[1] + sticker2[0]*sticker2[1]:
                    answer = sticker1[0]*sticker1[1] + sticker2[0]*sticker2[1]
                break

print(answer)