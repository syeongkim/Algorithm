def solution(numbers, k):
    answer = 0
    index = 0
    while (k > 1):
        index += 2
        person = numbers[index % len(numbers)]
        k -= 1
    answer = person
    return answer