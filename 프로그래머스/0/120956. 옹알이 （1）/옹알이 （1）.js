function solution(babbling) {
    var answer = 0;
    let availableWords = ["aya", "ye", "woo", "ma"];
    for (i = 0; i < babbling.length; i++) {
        let word = babbling[i];
        for (j = 0; j < 4;  j++) {
            if (word.includes(availableWords[j])) {
                word = word.replace(availableWords[j], '_');
            }
        }
        word = word.replaceAll('_', '')
        if (word.length == 0) {
            answer += 1;
        }
    }
    return answer;
}