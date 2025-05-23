import sys

switch_num = int(input())
switch = list(map(int, input().split()))
student_num = int(input())

for _ in range(student_num):
    gender, switch_no = map(int, input().split())
    if (gender == 1):
        for j in range(switch_num):
            if ((j+1) % switch_no == 0):
                switch[j] = abs(switch[j] - 1)
    else:
        idx = switch_no - 1
        switch[switch_no-1] = abs(switch[switch_no-1] - 1)
        idx_left = idx - 1
        idx_right = idx + 1
        while idx_left >= 0 and idx_right < switch_num and switch[idx_left] == switch[idx_right]:
            switch[idx_left] = abs(switch[idx_left] - 1)
            switch[idx_right] = abs(switch[idx_right] - 1)
            idx_left -= 1
            idx_right += 1
            
for i in range(switch_num):
    print(switch[i], end='')
    if (i+1) % 20 == 0:
        print()
    else:
        print(' ', end='')