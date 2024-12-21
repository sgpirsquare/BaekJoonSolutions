def solution(array, height):
    answer =0
    for man in array:
        if man>height:
            answer += 1
    return answer