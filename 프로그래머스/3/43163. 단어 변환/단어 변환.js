function solution(begin, target, words) {
    var answer = Infinity;
    var candidates = [];
    candidates.push([begin]);
    if (words.includes(target) == false) {
        return 0;
    }
    
    while(candidates.length > 0) {
        let currPath = candidates.pop();
        let lastWord = currPath[currPath.length - 1];
        if (lastWord == target) {
            if (currPath.length < answer) {
                answer = currPath.length - 1;
            }
        } else {
            for (let nextWord of words) {
                if (currPath.includes(nextWord) == false) {
                    var cnt = 0
                    for (i = 0; i < nextWord.length; i++) {
                        if (lastWord[i] != nextWord[i]) {
                            cnt += 1;
                        }
                    }
                    if (cnt == 1) {
                        var newPath = [...currPath];
                        newPath.push(nextWord);
                        candidates.push(newPath);
                    }
                }
            }
        }
    }
    return answer;
}