X = int(input())
binaryX = []

while X > 0:
    if X % 2 == 1:
        binaryX.insert(0, 1)
        X = (X-1) / 2
    else:
        binaryX.insert(0, 0)
        X = X / 2
        
print(binaryX.count(1))