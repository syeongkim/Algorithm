function solution(common) {
    var answer = 0;
    let A = common[0];
    let B = common[1];
    let C = common[2];
    let lastNum = common[common.length - 1];
    
    // 등차수열인지 확인
    if (A - B == B - C) {
        let diff = B - A;
        answer = lastNum + diff;
    } else {
        let diff = B / A;
        answer = lastNum * diff;
    }
    return answer;
}