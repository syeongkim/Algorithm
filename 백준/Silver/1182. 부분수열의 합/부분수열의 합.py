N, S = map(int, input().split())
NList = list(map(int, input().split()))
subSequenceList = [[]]
answer = 0

while len(NList):
    num = NList[0]
    NList.remove(NList[0])
    temp = []
    for subSequence in subSequenceList:
        listA = subSequence + [num]
        listB = subSequence
        temp.append(listA)
        temp.append(listB)
    subSequenceList = temp

for subSequence in subSequenceList:
    if (len(subSequence)):
        if (sum(subSequence) == S):
            answer += 1
            
print(answer)