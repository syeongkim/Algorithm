A, B, C, D = input().split()

def getClockNumber(a, b, c, d):
    numbers = []
    numbers.append(int(a + b + c + d))
    numbers.append(int(b + c + d + a))
    numbers.append(int(c + d + a + b))
    numbers.append(int(d + a + b + c))
    return min(numbers)

clockNumber = getClockNumber(A, B, C, D)

cnt = 0
for i in range(1111, clockNumber):
    [a, b, c, d] = list(str(i))
    if (a == 0 or b == 0 or c == 0 or d == 0):
        continue
    if i == getClockNumber(a, b, c, d):
        cnt += 1
        
print(cnt + 1)