function solution(score) {
    var answer = [];
    let averageScore = score.map((item) => (item[0] + item[1]) / 2);
    let sortedAverageScore = averageScore.slice().sort((a, b) => b - a);
    for (i = 0; i < averageScore.length; i++) {
        answer.push(sortedAverageScore.indexOf(averageScore[i]) + 1);
    }
    return answer;
}