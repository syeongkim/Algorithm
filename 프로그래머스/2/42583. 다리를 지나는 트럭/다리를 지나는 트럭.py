def solution(bridge_length, weight, truck_weights):
    answer = 0
    done = 0
    totalNumberOfTrucks = len(truck_weights)
    bridge = [0 for _ in range(bridge_length)]
    truckInProgress = []
    
    while done < totalNumberOfTrucks:
        answer += 1
        bridge.insert(0, 0)
        arrived = bridge.pop()
        if arrived != 0:
            done += 1
            truckInProgress.remove(arrived)
        if len(truck_weights) > 0:
            if sum(truckInProgress) + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                bridge[0] = truck
                truckInProgress.append(truck)
            else:
                pass
    return answer