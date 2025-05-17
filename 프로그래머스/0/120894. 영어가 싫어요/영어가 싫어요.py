def solution(numbers):
    answer = 0
    numlist = ['zero', 'one', 'two', 'three', 'four',
              'five', 'six', 'seven', 'eight', 'nine']
    
    for i, eng in enumerate(numlist):
        numbers = numbers.replace(eng, str(i))
    
    answer = int(numbers)
    return answer