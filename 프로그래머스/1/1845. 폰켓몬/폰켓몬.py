from collections import Counter

def solution(nums):
    answer = 0
    numsDictionary = Counter(nums)
    
    if len(numsDictionary) >= len(nums) / 2:
        answer = len(nums) / 2
    else:
        answer = len(numsDictionary)
        
    return answer