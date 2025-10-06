from collections import deque

def solution(word):
    dictionary = []
    vowelList = ['A', 'E', 'I', 'O', 'U']
    q = deque()
    q.append('')
    while q:
        item = q.popleft()
        if len(item) == 5:
            pass
        else:
            for vowel in vowelList:
                newItem = item + vowel
                q.append(newItem)
                dictionary.append(newItem)
            
    dictionary.sort()
    answer = dictionary.index(word) + 1
    return answer