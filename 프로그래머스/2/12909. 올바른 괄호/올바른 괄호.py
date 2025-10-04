def solution(s):
    answer = True
    signList = []
    
    for sign in s:
        if sign == '(':
            signList.append(sign)
        else:
            if len(signList) > 0:
                signList.pop()
            else:
                answer = False
                return answer

    if len(signList) > 0:
        answer = False
        
    return answer