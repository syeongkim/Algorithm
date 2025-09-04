N, A, B = map(int, input().split())
onePretty = list(map(int, input().split()))
twoPretty = list(map(int, input().split()))
onePretty.sort(reverse=True)
twoPretty.sort(reverse=True)

answer = 0
if N % 2 == 1:
    answer += onePretty[0]
    onePretty.pop(0)
    N -= 1
    
while N > 0:
    if N == 1:
        answer += onePretty[0]
        onePretty.pop(0)
        N -= 1
    else:
        t1, t2 = 0, 0
        if len(onePretty) >= 2:
            t1 = onePretty[0] + onePretty[1]
        if len(twoPretty) >= 1:
            t2 = twoPretty[0]
        
        if t1 > t2:
            answer += t1
            onePretty.pop(0)
            onePretty.pop(0)
        else:
            answer += t2
            twoPretty.pop(0)

        N -= 2
        
print(answer)