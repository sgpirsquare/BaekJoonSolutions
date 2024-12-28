def solution(n):
    answer = ""
    for i in list(map(str, sorted(str(n), reverse=True))):
        answer += i
    return int(answer)