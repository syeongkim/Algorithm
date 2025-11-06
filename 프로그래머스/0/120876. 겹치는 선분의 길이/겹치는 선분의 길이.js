function solution(lines) {
    var answer = 0;
    let line = Array(200).fill(0)
    
    lines.forEach(([a, b]) => {
        for (; a < b; a++) {
            line[a+100] += 1;
        }
    })
    
    duplicatedLine = line.filter((num) => num > 1)

    answer = duplicatedLine.length
    return answer;
}