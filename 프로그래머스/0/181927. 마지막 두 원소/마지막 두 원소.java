class Solution {
    public int[] solution(int[] num_list) {
        int numLength = num_list.length;
        int[] answer = new int[numLength + 1];
        for (int i = 0; i < numLength; i++) {
            answer[i] = num_list[i];
        }
        int last = num_list[numLength-1];
        int prev = num_list[numLength-2];
        
        if (last > prev) {
            answer[numLength] = last - prev;
        } else {
            answer[numLength] = last * 2;
        }
        return answer;
    }
}