# + 와 , 의 차이가 한 끝차이치고는 와 정말

n = int(input())

for i in range(n):
    print(" "*(n-i-1)+"*"*(i+1))

'''
# 이건 " "*(n-i-1), "*"*(i+1) ,는 공백 역할을 함
n = int(input())

for i in range(n):
    print(" "*(n-i-1), "*"*(i+1))
    
# 이건 또 뭐여
N=i=int(input())
while 0<i:i-=1;print(" "*i+"*"*(N-i))
'''
