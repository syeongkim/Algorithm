def solution(sizes):
    widthList = []
    heightList = []
    
    for size in sizes:
        a, b = size[0], size[1]
        if a > b:
            widthList.append(a)
            heightList.append(b)
        elif a == b:
            widthList.append(a)
            heightList.append(b)
        else:
            widthList.append(b)
            heightList.append(a)
            
    answer = max(widthList) * max(heightList)
    return answer