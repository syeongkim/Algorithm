function solution(number, k) {
    var answer = '';
    var numberList = number.split('');
    
    const stack = [];
    for (let num of numberList) {
        while (k > 0 && stack[stack.length - 1] < num) {
            stack.pop();
            k--;
        }
        stack.push(num);
    }
    stack.splice(stack.length - k, k);
    answer = stack.join('');
    return answer;
}