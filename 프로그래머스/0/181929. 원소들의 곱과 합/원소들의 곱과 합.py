def solution(num_list):
    product=1
    for number in num_list:
        product*=number
    if pow(sum(num_list),2)>product:
        answer = 1
    else:
        answer = 0
    return answer