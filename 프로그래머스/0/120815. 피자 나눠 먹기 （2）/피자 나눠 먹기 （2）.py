def GCD(a,b):
    while b:
        a,b=b, a%b
    return a

def LCM(a,b):
    return a*b// GCD(a,b)

def solution(n):
    answer = LCM(n,6)//6
    return answer