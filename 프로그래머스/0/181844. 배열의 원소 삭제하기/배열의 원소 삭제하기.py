def solution(arr, delete_list):
    answer = []
    for ar in arr:
        if ar not in delete_list:
            answer.append(ar)
            
    return answer