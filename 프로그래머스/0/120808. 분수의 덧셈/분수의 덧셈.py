from math import gcd

def solution(numer1, denom1, numer2, denom2):
    lcm_denom=denom1*denom2//gcd(denom1, denom2)
    numer=numer1 *(lcm_denom//denom1) +numer2 *(lcm_denom//denom2)
    gcd_numer_denom=gcd(numer, lcm_denom)
    answer = [numer//gcd_numer_denom,lcm_denom//gcd_numer_denom ]
    return answer
    
