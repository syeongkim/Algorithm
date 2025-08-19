import java.util.*;

class Solution {
    public int solution(String my_string) {
        int answer = 0;
        StringBuffer sb = new StringBuffer(my_string);
        for (int i = 0; i < sb.length(); i++) {
            try {
                int a = Integer.parseInt(String.valueOf(sb.charAt(i)));
            } catch (Exception e) {
                sb.setCharAt(i, ' ');
            }
        }
        String[] numbers = sb.toString().split(" ");
        for (int i = 0; i < numbers.length; i++) {
            if (!numbers[i].isEmpty()) {
                answer += Integer.parseInt(numbers[i]);
            }
        }
        return answer;
    }
}