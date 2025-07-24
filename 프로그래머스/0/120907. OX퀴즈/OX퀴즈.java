class Solution {
    public char[] solution(String[] quiz) {
        char[] answer = new char[quiz.length];
        for (int i = 0; i < quiz.length; i++) {
            String[] exp = quiz[i].split(" ");
            int left = Integer.parseInt(exp[0]);
            int right = Integer.parseInt(exp[2]);
            int result = Integer.parseInt(exp[4]);
            if (exp[1].equals("+")) {
                if (left + right == result) {
                    answer[i] = 'O';
                } else {
                    answer[i] = 'X';
                }
            } else {
                if (left - right == result) {
                    answer[i] = 'O';
                } else {
                    answer[i] = 'X';
                }
            }
        }
        return answer;
    }
}