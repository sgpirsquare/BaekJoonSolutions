def solution(my_string):
    answer = 0
    for num in my_string:
        if (
            num == "0"
            or num == "1"
            or num == "2"
            or num == "3"
            or num == "4"
            or num == "5"
            or num == "6"
            or num == "7"
            or num == "8"
            or num == "9"
        ):
            answer += int(num)
    return answer