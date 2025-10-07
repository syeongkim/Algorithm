def solution(triangle):
    answer = 0
    maxSumList = []
    for i in range(1, len(triangle) + 1):
        maxSumList.append([0 for _ in range(i)])
    
    maxSumList[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(i+1):
            candidates = []
            curr = triangle[i][j]
            
            if 0 <= i-1 < len(triangle) and 0 <= j-1 < i:
                leftSum = curr + maxSumList[i-1][j-1]
                candidates.append(leftSum)
            if 0 <= i-1 < len(triangle) and 0 <= j < i:
                rightSum = curr + maxSumList[i-1][j]
                candidates.append(rightSum)
            maxSumList[i][j] = max(candidates)
            
    answer = max(maxSumList[-1])
    return answer