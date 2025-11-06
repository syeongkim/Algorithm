function solution(bin1, bin2) {
    var answer = '';
    bin1Arr = bin1.split('')
    bin1Arr.reverse()
    bin2Arr = bin2.split('')
    bin2Arr.reverse()
    
    let n = Math.max(bin1.length, bin2.length);
    cin = 0
    for (i = 0; i < n; i++) {
        var a = bin1Arr[i];
        var b = bin2Arr[i];
        if (isNaN(a)) {
            a = "0";
        }
        if (isNaN(b)) {
            b = "0";
        }
        sum = parseInt(a) + parseInt(b) + cin
        if (sum > 1) {
            answer += (sum - 2).toString()
            cin = 1
        } else {
            answer += sum.toString()
            cin = 0
        }
    }
    answer += cin.toString()
    answer = answer.split('').reverse()
    if (answer[0] == '0') {
        answer = answer.slice(1, answer.length)
    }
        
    answer = answer.join('')
    return answer;
}