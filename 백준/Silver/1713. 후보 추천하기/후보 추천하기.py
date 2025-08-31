import sys

N = int(sys.stdin.readline())
numberOfRecommendations = int(sys.stdin.readline())
studentsOfRecommendations = list(map(int, sys.stdin.readline().split()))

pictures = []
countOfRecommendations = [0 for _ in range(101)]
orderOfRecommendations = [-1 for _ in range(101)]

for i in range(0, numberOfRecommendations):
    student = studentsOfRecommendations[i]
    if student in pictures:
        countOfRecommendations[student] += 1
    else:
        if len(pictures) == N:
            recommendationCountOfExistedStudents = [countOfRecommendations[j] for j in pictures]
            minCountOfRecommendation = min(recommendationCountOfExistedStudents)
            countOfMinRecommendation = recommendationCountOfExistedStudents.count(minCountOfRecommendation)
            if countOfMinRecommendation == 1:
                removeStudent = countOfRecommendations.index(min([countOfRecommendations[j] for j in pictures]))
            else:
                idx = []
                for k in range(len(countOfRecommendations)):
                    if countOfRecommendations[k] == minCountOfRecommendation:
                        idx.append(k)
                removeStudent = orderOfRecommendations.index(min([orderOfRecommendations[k] for k in idx]))

            pictures.remove(removeStudent)
            countOfRecommendations[removeStudent] = 0
            orderOfRecommendations[removeStudent] = -1
            
        pictures.append(student)
        countOfRecommendations[student] += 1
        orderOfRecommendations[student] = i
            
pictures.sort()
for i in pictures:
    print(i, end = " ")