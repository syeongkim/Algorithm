def solution(numbers):
    answer = 1
    answer *= max(numbers)
    numbers.remove(max(numbers))
    answer *= max(numbers)
    return answer