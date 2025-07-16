T = int(input())

for i in range(T):
    floor = int(input())
    room = int(input())
    zero = [x for x in range(1, room+1)]
    for j in range(floor):
        for k in range(1, room):
            zero[k] += zero[k-1]
        
    print(zero[-1])