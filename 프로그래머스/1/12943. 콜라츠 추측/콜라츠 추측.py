def solution(num):
    answer = 0
    if (num == 1):
        answer = 0
    else:
        count = 0
        while((num != 1) & (count < 500)):
            if (num % 2 == 0):
                num = num / 2
            else:
                num = num * 3 + 1
            count += 1
        if (count == 500):
            answer = -1
        else:
            answer = count
    return answer