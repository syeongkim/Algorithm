from collections import deque

def solution(k, dungeons):
    answer = -1
    dungeonsList = [i for i in range(1, len(dungeons) + 1)]
    exploreOrderList = []
    
    q = deque()
    q.append([])
    while q:
        item = q.popleft()
        if len(item) == len(dungeonsList):
            exploreOrderList.append(item)
        else:
            for dungeon in dungeonsList:
                newItem = item.copy()
                if dungeon not in newItem:
                    newItem.append(dungeon)
                    q.append(newItem)
                    
    for exploreOrder in exploreOrderList:
        currentScore = k
        cnt = 0
            
        for order in exploreOrder:
            dungeon = dungeons[order - 1]
            minScore, usingScore = dungeon[0], dungeon[1]
            if currentScore < minScore:
                answer = max(cnt, answer)
                break
            else:
                currentScore -= usingScore
                cnt += 1
        answer = max(cnt, answer)
        if answer == len(dungeons):
            return answer
        
    return answer