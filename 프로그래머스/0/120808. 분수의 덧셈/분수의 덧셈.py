import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom = denom1 * denom2
    numer = (numer1 * denom2) + (numer2 * denom1)
    gcd = math.gcd(denom, numer)
    answer.append(numer / gcd)
    answer.append(denom / gcd)
    return answer