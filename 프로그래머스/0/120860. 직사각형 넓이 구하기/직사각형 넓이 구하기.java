import java.util.*;

class Solution {
    public int solution(int[][] dots) {
        int answer = 0;
        ArrayList<Integer> xList = new ArrayList<Integer>();
        ArrayList<Integer> yList = new ArrayList<Integer>();
        
        for (int[] dot: dots) {
            xList.add(dot[0]);
            yList.add(dot[1]);
        }
        
        int xmax = Collections.max(xList);
        int xmin = Collections.min(xList);
        int ymax = Collections.max(yList);
        int ymin = Collections.min(yList);
        
        answer = (xmax - xmin) * (ymax - ymin);
        return answer;
    }
}