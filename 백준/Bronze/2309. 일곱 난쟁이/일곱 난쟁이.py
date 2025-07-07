arr = []

for i in range(9):
    arr.append(int(input()))
    
arr = sorted(arr)

arrsum = sum(arr)
diff = arrsum - 100

find = False

for i in range(9):
    for j in range(i+1, 9, 1):
        if arr[i] + arr[j] == diff:
            arr.remove(arr[j])
            arr.remove(arr[i])
            find = True
            break
    if find:
        break
        
for i in range(7):
    print(arr[i])
    