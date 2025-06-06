import sys

N = int(sys.stdin.readline())
sticks = []

for _ in range (N):
    sticks.append(int(sys.stdin.readline()))
    
sticks.reverse()
count = 1
max_height = sticks[0]

for i in range(1, N):
    if (sticks[i] > max_height):
        count += 1
        max_height = sticks[i]
        
print(count)