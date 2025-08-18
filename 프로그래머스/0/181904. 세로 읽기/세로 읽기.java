import java.util.*;

class Solution {
    public String solution(String my_string, int m, int c) {
        String answer = "";
        ArrayList<String> stringList = new ArrayList<String>();
        for (int i = 0; i < my_string.length() / m; i++) {
            stringList.add(my_string.substring(i*m, (i+1)*m));
        }
        for (String string: stringList) {
            answer += string.charAt(c-1);
        }
        return answer;
    }
}