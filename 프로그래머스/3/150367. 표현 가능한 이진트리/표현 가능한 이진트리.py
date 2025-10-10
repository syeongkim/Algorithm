def intToBinaryTree(number):
    result = []
    while number > 0:
        if number % 2 == 1:
            result.insert(0, 1)
            number = (number - 1) / 2
        else:
            result.insert(0, 0)
            number = number / 2
            
    k = 0
    while True:
        if len(result) <= 2 ** k - 1:
            break
        else:
            k += 1
    
    while True:
        if len(result) == 2 ** k - 1:
            break
        result.insert(0, 0)
    
    return result

def checkBinaryTree(binaryTree, start, end):
    available = True
    mid = (end + start) // 2
    leftTree = binaryTree[start:mid]
    rightTree = binaryTree[mid+1:end+1]
    if sum(leftTree) > 0 or sum(rightTree) > 0:
        if binaryTree[mid] == 0:
            available = False
            return available
        else:
            if start < mid-1:
                leftTreeAvailable = checkBinaryTree(binaryTree, start, mid-1)
                if leftTreeAvailable == False:
                    available = False
                    return available
            if mid+1 < end:
                rightTreeAvailable = checkBinaryTree(binaryTree, mid+1, end)
                if rightTreeAvailable == False:
                    available = False
                    return available
                
    return available
    
def solution(numbers):
    answer = []
    for number in numbers:
        binaryTree = intToBinaryTree(number)
        start = 0
        end = len(binaryTree)
        treeAvailable = checkBinaryTree(binaryTree, start, end)
        if treeAvailable:
            answer.append(1)
        else:
            answer.append(0)

    return answer