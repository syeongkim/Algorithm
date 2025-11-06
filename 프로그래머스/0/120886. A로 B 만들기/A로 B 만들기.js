function solution(before, after) {
    var answer = 0;
    
    n = before.length
    
    for (i = 0; i< n; i++) {
        if (after.includes(before[i])) {
            idx = after.indexOf(before[i])
            after = after.replace(before[i], "")
        }
    }
    
    if (after.length == 0) {
        answer = 1
    }
    return answer;
}