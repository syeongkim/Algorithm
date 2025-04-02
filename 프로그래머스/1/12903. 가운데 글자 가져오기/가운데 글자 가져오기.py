def solution(s):
    answer = ''
    if (len(s) % 2 == 0):
        mid = int(len(s) / 2 - 1)
        answer = s[mid] + s[mid+1]
    else:
        mid = int(len(s) / 2)
        answer = s[mid]
    return answer