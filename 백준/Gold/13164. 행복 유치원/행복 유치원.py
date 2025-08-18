N, K = map(int, input().split())
heights = list(map(int, input().split()))
diff = []
idxs = []
groups = []

for i in range(N-1):
    diff.append([heights[i+1] - heights[i], i+1])

diff.sort(key=lambda x: x[0], reverse=True)

for i in range(K-1):
    idx = diff[i][1]
    idxs.append(idx)
    
idxs.sort()

start = 0
for idx in idxs:
    group = heights[start:idx]
    groups.append(group)
    start = idx
groups.append(heights[start:])

total = 0
for group in groups:
    total += group[-1] - group[0]
    
print(total)