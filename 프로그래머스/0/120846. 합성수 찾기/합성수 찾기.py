def isprime(n):
    for i in range(2, int(pow(n,0.5)+1)):
        if n%i ==0:
            return False
    return True

def solution(n):
    answer=0
    for i in range(1,n+1):
        if isprime(i):
            answer+=1
    
    return n - answer