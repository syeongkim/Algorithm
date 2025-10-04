import heapq

def solution(operations):
    answer = []
    minHeap = []
    maxHeap = []
    value = []
    
    for operation in operations:
        op, num = operation.split(' ')
        num = int(num)
        if op == 'I':
            heapq.heappush(minHeap, num)
            heapq.heappush(maxHeap, num * (-1))
            value.append(num)
        else:
            if len(value) == 0:
                pass
            else:
                if num == 1:
                    while True:
                        maxValue = heapq.heappop(maxHeap)
                        if maxValue * (-1) in value:                        
                            value.remove(maxValue * (-1))
                            break
                        else:
                            pass
                else:
                    while True:
                        minValue = heapq.heappop(minHeap)
                        if minValue in value:                        
                            value.remove(minValue)
                            break
                        else:
                            pass
                
    if len(value) == 0:
        answer = [0, 0]
    else:
        answer = [max(value), min(value)]
        
    return answer