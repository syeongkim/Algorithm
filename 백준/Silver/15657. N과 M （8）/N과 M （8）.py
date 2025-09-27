N, M = map(int, input().split())
nList = list(map(int, input().split()))

def dfs(depth, array):
    newArray = []
    if depth == M:
        return array
    for item in array:
        for n in nList:
            newItem = item + [n]
            sortedNewItem = sorted(newItem)
            if sortedNewItem not in newArray:
                newArray.append(sortedNewItem)
    return dfs(depth + 1, newArray)

result = dfs(0, [[]])
sortedResult = sorted(result)

for nums in sortedResult:
    for num in nums:
        print(num, end = ' ')
    print()