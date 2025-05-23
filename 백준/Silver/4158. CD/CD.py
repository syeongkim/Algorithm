import sys

while True:
    n, m = map(int, sys.stdin.readline().split(' '))
    
    if (n == 0 and m == 0):
        break
        
    sang = [int(sys.stdin.readline()) for _ in range(n)]
    sun = [int(sys.stdin.readline()) for _ in range(m)]
    
    count = 0
    index_n = 0
    index_m = 0

    while ((index_n < n) and (index_m < m)):
        if (sang[index_n] == sun[index_m]):
            index_n += 1
            index_m += 1
            count += 1
        elif (sang[index_n] > sun[index_m]):
            index_m += 1
        else:
            index_n += 1
        
    print(count)