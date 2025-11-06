function solution(dots) {
    var answer = 0;
    let A = dots[0]
    let B = dots[1]
    let C = dots[2]
    let D = dots[3]
    
    // case 1
    if ((B[1] - A[1]) / (B[0] - A[0]) == (D[1] - C[1]) / (D[0] - C[0])) {
        answer = 1
    }
    
    // case 2
    if ((C[1] - A[1]) / (C[0] - A[0]) == (D[1] - B[1]) / (D[0] - B[0])) {
        answer = 1
    }
    
    // case 3
    if ((D[1] - A[1]) / (D[0] - A[0]) == (B[1] - C[1]) / (B[0] - C[0])) {
        answer = 1
    }
    
    return answer;
}