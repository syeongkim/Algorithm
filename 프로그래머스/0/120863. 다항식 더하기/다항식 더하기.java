import java.util.*;

class Solution {
    public String solution(String polynomial) {
        String answer = "";
        String[] polynomialList = polynomial.split(" ");
        int constant = 0;
        int coefficient = 0;
        for (String term: polynomialList) {
            if (!term.equals("+")) {
                if (term.endsWith("x")) {
                    String num = term.replace("x", "");
                    if (num == "") {
                        num = "1";
                    }
                    coefficient += Integer.parseInt(num);
                } else {
                    constant += Integer.parseInt(term);
                }
            }
        }
        if (coefficient != 0) {
            if (coefficient == 1) {
                answer += "x";
            } else {
                answer += Integer.toString(coefficient) + "x";
            }
            if (constant != 0) {
                answer += " + " + Integer.toString(constant);
            }
        } else {
            if (constant != 0) {
                answer += Integer.toString(constant);
            }
        }
        
        return answer;
    }
}