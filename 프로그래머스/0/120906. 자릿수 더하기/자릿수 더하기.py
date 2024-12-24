def solution(n):
    n=str(n)
    answer = 0
    for digit in n:
        answer+=int(digit)
    return answer