n, m = map(int, input().split())
list_A = list(map(int, input().split()))
list_A.sort()

def ques1(k):
    low = 0
    high = n - 1
    idx = n
    while (low <= high):
        mid = (low + high) // 2
        if list_A[mid] >= k:
            idx = mid
            high = mid - 1
        else:
            low = mid + 1
    return n - idx

def ques2(k):
    low = 0
    high = n - 1
    idx = n
    while (low <= high):
        mid = (low + high) // 2
        if list_A[mid] > k:
            idx = mid
            high = mid - 1
        else:
            low = mid + 1
    return n - idx  
        
for _ in range(m):
    ques = input()
    if ques[0] == '1':
        k = int(ques.split()[-1])
        print(ques1(k))
    elif ques[0] == '2':
        k = int(ques.split()[-1])
        print(ques2(k))
    else:
        _, i, j = map(int, ques.split())
        print(ques1(i) - ques2(j))