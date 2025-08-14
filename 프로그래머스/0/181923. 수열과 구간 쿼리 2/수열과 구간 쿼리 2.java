class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int[] query = queries[i];
            int min = 1000001;
            for (int j = query[0]; j < query[1]+1; j++) {
                if (arr[j] > query[2] && arr[j] < min) {
                    min = arr[j];
                }
            }
            if (min == 1000001) {
                answer[i] = -1;
            } else {
                answer[i] = min;
            }
        }
        return answer;
    }
}