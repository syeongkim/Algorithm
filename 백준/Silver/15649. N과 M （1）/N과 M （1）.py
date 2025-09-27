N, M = map(int, input().split())
nList = [i for i in range(1, N+1)]

def dfs(depth, array):
    newArray = []
    if depth == M:
        return array
    for item in array:
        for n in nList:
            if n not in item:
                newItem = item + [n]
                newArray.append(newItem)
    return dfs(depth + 1, newArray)

result = dfs(0, [[]])

for nums in result:
    for num in nums:
        print(num, end = ' ')
    print()