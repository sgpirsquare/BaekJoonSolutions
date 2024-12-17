def solution(a, b):
    text=str(a) + str(b)
    integer=2*int(a)*int(b)
    if int(text)>=integer:
        answer=int(text)
    else:
        answer=integer
    
    return answer