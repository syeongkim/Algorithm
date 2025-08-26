import sys

N = int(sys.stdin.readline())
expected = []

for _ in range(N):
    expected.append(int(sys.stdin.readline()))
    
result = [i for i in range(1, N+1)]
expected.sort()

sum = 0
for i in range(N):
    sum += abs(result[i] - expected[i])
    
print(sum)