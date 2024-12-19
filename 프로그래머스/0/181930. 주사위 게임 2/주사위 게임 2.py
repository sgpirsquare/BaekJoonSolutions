def solution(a,b,c):
    sum= a+b+c
    set_point={a,b,c}
    if len(set_point)==3:
        answer=sum
    elif len(set_point)==2:
        answer=sum*(pow(a,2)+pow(b,2)+pow(c,2))
    elif len(set_point)==1:
        answer=3*a*3*pow(a,2)*3*pow(a,3)
    
    return answer