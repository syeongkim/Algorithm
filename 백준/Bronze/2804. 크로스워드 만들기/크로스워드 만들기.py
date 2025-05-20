a, b = input().split(" ")

for i in a:
    for j in b:
        if (i == j):
            n = a.index(i)
            m = b.index(j)
            break
    if (i==j):
        break

            
for i in range(len(b)):
    if (i==m):
        print(a)
    else:
        for j in range(len(a)):
            if (j==n):
                print(b[i], end="")
            else:
                print(".", end="")
        if (i != len(b)-1):
            print("")
    