import java.util.*;

class Solution {
    public ArrayList<String> solution(String my_string) {
        ArrayList<String> answer = new ArrayList<String>();
        int length = my_string.length();
        for (int i = 0; i < length; i++) {
            String suffix = my_string.substring(i, length);
            if (!answer.contains(suffix)) {
                answer.add(suffix);
            }
        }
        Collections.sort(answer);
        return answer;
    }
}