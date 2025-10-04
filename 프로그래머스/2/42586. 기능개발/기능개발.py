def solution(progresses, speeds):
    answer = []
    
    while len(progresses) > 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        cnt = 0
        for t in progresses:
            if t >= 100:
                cnt += 1
            else:
                break
        
        if cnt > 0:
            for _ in range(cnt):
                progresses.pop(0)
                speeds.pop(0)
            answer.append(cnt)
            
    return answer