inputStrings = list(input())
bars = 0
answer = 0

i = 0
while i < len(inputStrings):
    if inputStrings[i] == '(':
        if inputStrings[i+1] == ')':
            answer += bars
            i += 2
        else:
            bars += 1
            i += 1
    else:
        answer += 1
        bars -= 1
        i += 1
            
print(answer)