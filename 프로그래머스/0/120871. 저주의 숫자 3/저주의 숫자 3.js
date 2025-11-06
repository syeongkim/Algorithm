function solution(n) {
    var answer = 0;
    var cnt = 0;
    
    while (true) {
        if (answer.toString().includes('3') == false) {
            if (answer % 3 > 0) {
                cnt += 1;
            }
        }
        if (cnt == n) {
            break
        }
        answer += 1;
    }
    return answer;
}