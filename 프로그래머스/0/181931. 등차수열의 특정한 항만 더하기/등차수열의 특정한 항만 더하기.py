def solution(a,d,included):
    length = len(included)
    answer=0
    for i in range(length):
        if included[i] == True:
            answer+= a + d * i
    return answer