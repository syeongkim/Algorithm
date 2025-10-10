def solution(cap, n, deliveries, pickups):
    answer = 0
    lastDeliveries = n-1
    lastPickups = n-1
    while lastDeliveries >= 0 or lastPickups >= 0:
        deliveriesCap = cap
        pickupsCap = cap
        
        while lastDeliveries >= 0 and deliveries[lastDeliveries] == 0:
            lastDeliveries -= 1
        while lastPickups >= 0 and pickups[lastPickups] == 0:
            lastPickups -= 1
        if lastDeliveries < 0 and lastPickups < 0:
            break
        
        distance = max(lastDeliveries, lastPickups)
        answer += (distance + 1) * 2
        
        while lastDeliveries >= 0 and deliveriesCap > 0:
            if deliveries[lastDeliveries] > deliveriesCap:
                deliveries[lastDeliveries] -= deliveriesCap
                break
            else:
                deliveriesCap -= deliveries[lastDeliveries]
                deliveries[lastDeliveries] = 0
                lastDeliveries -= 1

        while lastPickups >= 0 and pickupsCap > 0:
            if pickups[lastPickups] > pickupsCap:
                pickups[lastPickups] -= pickupsCap
                break
            else:
                pickupsCap -= pickups[lastPickups]
                pickups[lastPickups] = 0
                lastPickups -= 1
    return answer