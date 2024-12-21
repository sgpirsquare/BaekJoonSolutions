def solution(my_string, n):
    answer = ''
    for character in my_string:
        answer+=n*character
    return answer