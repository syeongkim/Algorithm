import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        if len(scoville) < 2:
            break
        if scoville[0] >= K:
            return answer
        minScoville = heapq.heappop(scoville)
        secondMinScoville = heapq.heappop(scoville)
        heapq.heappush(scoville, minScoville + secondMinScoville * 2)
        answer += 1
            
    if len(scoville) < 2:
        if scoville[0] < K:
            return -1
        
    return answer