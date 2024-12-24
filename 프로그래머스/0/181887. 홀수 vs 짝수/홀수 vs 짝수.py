def solution(num_list):
    even_sum=0
    odd_sum=0
    answer = 0
    for i in range(0, len(num_list),2):
        odd_sum+=num_list[i]
    for i in range(1, len(num_list),2):
        even_sum+=num_list[i]
    if even_sum>=odd_sum:
        answer=even_sum
    else:
        answer=odd_sum
    return answer