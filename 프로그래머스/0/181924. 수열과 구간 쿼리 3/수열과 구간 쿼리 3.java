class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};
        for (int i = 0; i < queries.length; i++) {
            int[] query = queries[i];
            int num1 = arr[query[0]];
            int num2 = arr[query[1]];
            arr[query[1]] = num1;
            arr[query[0]] = num2;
        }
        answer = arr;
        return answer;
    }
}