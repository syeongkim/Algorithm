n, k = map(int, input().split())
people = [i for i in range(1, n+1)]
answer = []

idx = k-1
while len(answer) < n:
    num = people[idx]
    if (num != 0):
        answer.append(num)
        people[idx] = 0
        cnt = 0
        while (cnt < k):
            if (len(answer) == n):
                break
            idx += 1
            if (idx >= n):
                idx = idx % n
            if (people[idx] != 0):
                cnt += 1
                
print("<" + ", ".join(map(str, answer)) + ">")