def solution(str_list, ex):
    answer = ''
    for character in str_list:
        if ex not in character:
            answer+=character
    return answer