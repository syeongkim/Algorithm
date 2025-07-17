T = int(input())

def factorial(n):
    mul = 1
    for i in range(1, n+1, 1):
        mul *= i
    return mul


for _ in range(T):
    n, m = input().split()
    n = int(n)
    m = int(m)
    result = factorial(m) / (factorial(n) * factorial(m-n))
    print(int(result))
