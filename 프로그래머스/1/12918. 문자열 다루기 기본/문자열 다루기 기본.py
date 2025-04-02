def solution(s):
    answer = False
    if ((len(s) == 4) | (len(s) == 6)):
        try:        
            s = int(s)
            answer = True
        except:
            pass
    return answer