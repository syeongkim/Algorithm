def solution(lottos, win_nums):
    answer = []
    correct = 0
    zero = 0
    for i in lottos:
        if (i == 0):
            zero += 1
        else:
            if (i in win_nums):
                correct += 1
                
    maxCorrect = correct + zero
    minCorrect = correct
    
    prize = { 6:1, 5:2, 4:3, 3:4, 2:5 }
    
    try:
        answer.append(prize[maxCorrect])
    except:
        answer.append(6)
    
    try:
        answer.append(prize[minCorrect])
    except:
        answer.append(6)
    
    return answer