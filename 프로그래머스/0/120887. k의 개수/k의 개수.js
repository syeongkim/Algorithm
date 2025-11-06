function solution(i, j, k) {
    var answer = 0;
    
    for (num = i; num <= j; num++) {
        numStr = num.toString()
        for (idx = 0; idx < numStr.length; idx++) {
            if (numStr[idx] == k.toString()) {
                answer += 1;
            }
        }
    }
    return answer;
}