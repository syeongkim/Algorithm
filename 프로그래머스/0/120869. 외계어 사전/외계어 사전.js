function solution(spell, dic) {
    var answer = 2;
    
    for (i = 0; i < dic.length; i++) {
        word = dic[i]
        isExist = true
        for (s = 0; s < spell.length; s++) {
            alphabet = spell[s]
            if (word.includes(alphabet) == false) {
                isExist = false
                break
            }
        }
        if (isExist) {
            answer = 1
            break
        }
    }
    
    return answer;
}