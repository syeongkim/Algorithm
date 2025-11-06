function solution(a, b) {
    var answer = 1;
    
    for (i = 1; i <= a; i++) {
        if ((a % i == 0) && (b % i == 0)) {
            a = a / i;
            b = b / i;
        }
    }
    
    while (true) {
        if (b % 2 > 0) {
            break
        }
        b = b / 2
    }
    
    while (true) {
        if (b % 5 > 0) {
            break
        }
        b = b / 5
    }
    
    if (b > 1) {
        answer = 2
    }
    return answer;
}