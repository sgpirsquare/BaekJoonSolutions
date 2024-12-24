def solution(age):
    answer = ''
    for age in list(str(age)):
        answer += chr(97 + int(age))

    return answer