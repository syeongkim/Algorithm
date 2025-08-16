class Solution {
    public String solution(String my_string, int[][] queries) {
        StringBuilder sb = new StringBuilder(my_string);
        for (int[] query: queries) {
            int s = query[0];
            int e = query[1];
            for (int j = 0; j <= (e - s) / 2; j++) {
                int idx1 = s + j;
                int idx2 = e - j;
                char temp = sb.charAt(idx2);
                sb.setCharAt(idx2, sb.charAt(idx1));
                sb.setCharAt(idx1, temp);
            }
        }
        String answer = sb.toString();
        return answer;
    }
}