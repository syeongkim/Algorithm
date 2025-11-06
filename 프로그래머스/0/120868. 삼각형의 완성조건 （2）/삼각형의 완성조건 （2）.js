function solution(sides) {
    var answer = 0;
    candidates = [];
    // 가장 긴 변이 sides에 있는 경우
    let maxLength = Math.max(...sides)
    let minLength = Math.min(...sides)
    let minNumber = maxLength - minLength + 1
    for (i = minNumber; i <= maxLength; i++) {
        if (candidates.includes(i) == false) {
            candidates.push(i)
        }
    }
    
    // 가장 긴 변을 구하는 경우
    for (i = maxLength + 1; i < minLength + maxLength; i++) {
        if (candidates.includes(i) == false) {
            candidates.push(i)
        }
    }
    
    answer = candidates.length
    return answer;
}