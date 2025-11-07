function solution(num, total) {
    var answer = [];
    // num이 짝수
    if (num % 2 == 0) {
        let middleNumber = parseInt(total / num);
        // middle 전으로 num / 2 - 1개의 숫자
        for (i = 0; i < num/2 - 1; i++) {
            answer.push(middleNumber - num/2 + 1 + i);
        }
        answer.push(middleNumber);
        // middle 후로 num / 2 개의 숫자
        for (i = 0; i < num/2; i++) {
            answer.push(middleNumber + i + 1);
        }
    } else { // num이 홀수
        let middleNumber = total / num;
        let n = (num - 1) / 2;
        for (i = 0; i < n; i++) {
            answer.push(middleNumber - n + i);
        }
        answer.push(middleNumber);
        for (i = 0; i < n; i++) {
            answer.push(middleNumber + i + 1);
        }
    }
    
    return answer;
}