from collections import deque

def checkPrimeNumber(num):
    isPrimeNumber = True
    for i in range(2, num//2 + 1):
        if num % i == 0:
            isPrimeNumber = False
            return isPrimeNumber
    return isPrimeNumber
    
def solution(numbers):
    answer = 0
    numbersList = list(numbers)
    allNumbers = set()
    
    q = deque()
    q.append(('', [0 for _ in range(len(numbersList))]))
    while q:
        item, visited = q.popleft()
        if item:
            allNumbers.add(int(item))
        for i in range(len(numbersList)):
            if visited[i] == 0:
                newVisited = [v for v in visited]
                newVisited[i] = 1
                q.append((item + numbersList[i], newVisited))
                
    print(allNumbers)
    for num in allNumbers:
        if num > 1:
            isPrimeNumber = checkPrimeNumber(num)
            if isPrimeNumber:
                answer += 1

    return answer