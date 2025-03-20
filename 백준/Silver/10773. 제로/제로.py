k = int(input())
stack = []
sum = 0

for i in range (k):
    num = int(input())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

for i in range (len(stack)):
    sum += stack[i]
    
print(sum)