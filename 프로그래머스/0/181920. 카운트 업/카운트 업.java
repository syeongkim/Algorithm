import java.util.*;

class Solution {
    public List<Integer> solution(int start_num, int end_num) {
        List<Integer> answerList = new ArrayList<>();
        for (int i = start_num; i <= end_num; i++) {
            answerList.add(i);
        }
        return answerList;
    }
}