import heapq

def solution(jobs):
    answer = 0
    
    time = 0
    done = [0 for _ in range(len(jobs))]
    while sum(done) < len(jobs):
        jobsHeap = []
        for j in range(len(jobs)):
            job = jobs[j]
            if job[0] <= time and done[j] == 0:
                heapq.heappush(jobsHeap, [job[1], job[0], j])
                
        if len(jobsHeap) == 0:
            time += 1
        else:
            targetJob = heapq.heappop(jobsHeap)
            time += targetJob[0]
            answer += time - targetJob[1]
            done[targetJob[2]] = 1 
        
    answer = answer // len(jobs)
    return answer