def solution(s):
    answer = []
    dic = {}
    
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    for i in dic:
        if dic[i] == 1:
            answer.append(i)
            
    answer = sorted(answer)
    return ''.join(answer)