def solution(s):
    answer = False
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    num_p = 0
    num_y = 0
    for i in s:
        if (i.lower() == 'p'):
            num_p += 1
        if (i.lower() == 'y'):
            num_y += 1
    if (num_p == num_y):
        answer = True
    return answer