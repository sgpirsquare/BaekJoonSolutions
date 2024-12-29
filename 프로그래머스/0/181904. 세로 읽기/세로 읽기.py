def solution(my_string, m, c):
    
    answer = []
    lth=len(my_string)
    for i in range(c-1,m):
        result=''
        for j in range(0,lth,m):
            result+=my_string[i+j]
        answer.append(result)
    return answer[0]