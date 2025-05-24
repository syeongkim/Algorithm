T = int(input())

for _ in range(T):
    N, X, Y = map(int, input().split())
    V = list(map(int, input().split()))
    
    min_time = min(X/V[i] for i in range(len(V) - 1))
              
    if (V[-1] == max(V)):
        print(0)
        continue

    low = 0
    high = Y
    answer = 0
    while (low <= high):
        Z = (low + high) // 2
        time = 1 + ((X - Z) / V[-1])
            
        if time < min_time:
            high = Z - 1
            answer = Z
        else:
            low = Z + 1
            
    if (low > Y):
        print(-1)
    else:
        print(answer)