def solution(balls, share):
    answer = 0
    num1 = 1
    num2 = 1
    for i in range (share):
        num1 *= balls
        num2 *= share
        balls -= 1
        share -= 1
    print(num1, num2)
    answer = num1 / num2
    return answer