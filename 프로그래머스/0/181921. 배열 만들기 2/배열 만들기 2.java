import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        List<Integer> answerList = new ArrayList<>();
        for (int i = l; i <= r; i++) {
            String number = Integer.toString(i);
            boolean isValid = true;
            for (int j = 0; j < number.length(); j++) {
                if (number.charAt(j) != '0' && number.charAt(j) != '5') {
                    isValid = false;
                    break;
                }
            }
            if (isValid) {
                answerList.add(i);
            }
        }
        
        if (answerList.size() == 0) {
            answerList.add(-1);
        }
        int[] answer = answerList.stream().mapToInt(n -> n).toArray();
        return answer;
    }
}