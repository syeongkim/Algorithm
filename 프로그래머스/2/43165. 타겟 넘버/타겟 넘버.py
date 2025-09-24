def dfs(numbers, depth, target, temp):
    if (depth == len(numbers)):
        return temp.count(target)
    newTemp = []
    for t in temp:
        newTemp.append(t + numbers[depth])
        newTemp.append(t - numbers[depth])
    return dfs(numbers, depth + 1, target, newTemp)

def solution(numbers, target):
    answer = dfs(numbers, 0, target, [0])
    return answer