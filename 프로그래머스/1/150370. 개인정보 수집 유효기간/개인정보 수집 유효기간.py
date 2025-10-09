def addMonth(startDate, monthToAdd):
    year, month, day = map(int, startDate.split('.'))
    monthToAdd = int(monthToAdd)

    # 개월 더하기
    month += monthToAdd
    # 12개월 넘으면 년도 증가
    year += (month - 1) // 12
    month = (month - 1) % 12 + 1

    # 하루 빼기
    day -= 1
    if day == 0:
        day = 28
        month -= 1
        if month == 0:
            month = 12
            year -= 1

    return f"{year:04d}.{month:02d}.{day:02d}"

def checkPassed(date, today):
    # 문자열 비교 대신 튜플 비교로!
    todayY, todayM, todayD = map(int, today.split('.'))
    y, m, d = map(int, date.split('.'))
    return (y, m, d) < (todayY, todayM, todayD)

def solution(today, terms, privacies):
    answer = []
    termHash = {}
    for term in terms:
        sign, month = term.split()
        termHash[sign] = month
        
    for i, privacy in enumerate(privacies, 1):
        startDate, sign = privacy.split()
        expireDate = addMonth(startDate, termHash[sign])
        if checkPassed(expireDate, today):
            answer.append(i)
    return answer