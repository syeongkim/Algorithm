class Solution {
    public String[] solution(String my_str, int n) {
        int length = (int)Math.ceil((double)my_str.length() / n);
        String[] answer = new String[length];
        for (int i = 0; i < length; i++) {
            String partial = "";
            for (int j = 0; j < n; j++) {
                int idx = i * n + j;
                if (idx < my_str.length()) {
                    partial += my_str.charAt(idx);
                }
            }
            answer[i] = partial;
        }
        return answer;
    }
}