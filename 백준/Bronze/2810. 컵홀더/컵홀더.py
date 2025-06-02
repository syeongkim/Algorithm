N = int(input())
seats = input()
cupholder = 1

idx = 0
while (idx != len(seats)):
    if (seats[idx] == 'S'):
        cupholder += 1
    else:
        cupholder += 0.5
    idx += 1
    
if (cupholder >= N):
    print(N)
else:
    print(int(cupholder))