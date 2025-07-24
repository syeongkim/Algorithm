import java.util.Arrays;

class Solution {
    public String solution(String my_string) {
        String answer = "";
        String lowerMyString = my_string.toLowerCase();
        char[] charArr = lowerMyString.toCharArray();
        Arrays.sort(charArr);
        answer = new String(charArr);
        return answer;
    }
}