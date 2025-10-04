from functools import cmp_to_key

def compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

def solution(numbers):
    answer = ''
    strings = [str(num) for num in numbers]
    sortedStrings = sorted(strings, key=cmp_to_key(compare))
    for s in sortedStrings:
        answer += s
        
    if int(answer) == 0:
        answer = "0"
    return answer