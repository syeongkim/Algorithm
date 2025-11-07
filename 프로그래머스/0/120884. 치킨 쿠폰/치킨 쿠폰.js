function solution(chicken) {
    var answer = 0;
    while (chicken >= 10) {
        var newChicken = parseInt(chicken / 10);
        answer += newChicken;
        chicken = chicken - newChicken * 9;
    }
    return answer;
}