function solution(A, B) {
    var answer = -1;
    let n = A.length;
    if (A == B) {
        answer = 0;
    } else {
        for (i = 1; i < n; i++) {
            console.log("1:", A.slice(n-i, n), "2:", A.slice(0, n-i));
            var newA = A.slice(n-i, n) + A.slice(0, n-i);
            console.log(newA);
            if (newA == B) {
                answer = i;
                break;
            }
        }   
    }
    return answer;
}