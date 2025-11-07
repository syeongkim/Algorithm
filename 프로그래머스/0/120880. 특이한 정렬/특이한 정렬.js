function solution(numlist, n) {
    var answer = [];
    numDiffList = numlist.map((num) => [Math.abs(n - num), num]);
    sortedNumDiffList = numDiffList.sort((a, b) => {
        if (a[0] != b[0]) {
            return a[0] - b[0]
        } else {
            return b[1] - a[1]
        }
    });
    
    for (i = 0; i < sortedNumDiffList.length; i++) {
        answer.push(sortedNumDiffList[i][1]);
    }
    return answer;
}