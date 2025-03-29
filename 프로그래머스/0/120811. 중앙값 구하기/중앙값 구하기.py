def solution(array):
    answer = 0
    array.sort()
    mid = int(len(array) / 2)
    answer = array[mid]
    return answer