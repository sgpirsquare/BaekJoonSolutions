def solution(a, b):
    answer = 0
    if a<b:
        for num in range(a,b+1):
            answer+=num
    elif a>b:
        for num in range(b,a+1):
            answer+=num
    else:
        return a
    return answer