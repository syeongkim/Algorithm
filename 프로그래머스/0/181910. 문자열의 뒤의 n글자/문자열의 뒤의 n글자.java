class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        int s = my_string.length() - n;
        answer = my_string.substring(s, my_string.length());
        return answer;
    }
}