def solution(age):
    answer = ''
    programmer_962 = 'abcdefghij'
    for i in str(age):
        answer += programmer_962[int(i)]
    return answer