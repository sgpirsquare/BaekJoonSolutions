def solution(num_list):
    answer = -1
    for num in num_list:
        if int(num)<0:
            answer=num_list.index(num)
            break
   
    return answer