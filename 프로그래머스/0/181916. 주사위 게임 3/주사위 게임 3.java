import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        int[] numbers = {a, b, c, d};
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < 4; i++) {
            int number = numbers[i];
            if (map.containsKey(number)) {
                int value = map.get(number);
                map.put(number, value + 1);
            } else {
                map.put(number, 1);
            }
        }
        
        switch (map.size()) {
            case 1:
                answer = 1111 * a;
                break;
            case 2:
                List<Integer> keys = new ArrayList<>(map.keySet());
                int k1 = keys.get(0);
                int k2 = keys.get(1);
                int v1 = map.get(k1);
                int v2 = map.get(k2);
                int p = 0;
                int q = 0;
                if (v1 == 3 || v2 == 3) {
                    if (v1 == 3) {
                        p = k1;
                        q = k2;
                    } else {
                        p = k2;
                        q = k1;
                    }
                    answer = (int) Math.pow(10 * p + q, 2);
                } else {
                    answer = (k1 + k2) * Math.abs(k1 - k2);
                }
                break;
            case 3:
                List<Integer> singles = new ArrayList<>();
                int pair = 0;
                for (Map.Entry<Integer, Integer> e: map.entrySet()) {
                    if (e.getValue() == 2) {
                        pair = e.getKey();
                    } else {
                        singles.add(e.getKey());
                    }
                }
                answer = singles.get(0) * singles.get(1);
                break;
            case 4:
                answer = Arrays.stream(numbers).min().getAsInt();
        }
        return answer;
    }
}