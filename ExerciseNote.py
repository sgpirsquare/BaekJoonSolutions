# 2480 처음 생각한 것
a, b, c = map(int, input().split())

dice = set({a, b, c})

if len(dice) == 1:
    print(10000 + (a * 1000))
elif len(dice) == 2:
    if a == b:
        print(1000 + (a * 100))
    elif b == c:
        print(1000 + (b * 100))
    elif a == c:
        print(1000 + (c * 100))
elif len(dice) == 3:
    print(list(dice)[2] * 100)

# 챗지피티가 첨삭해준 것
a, b, c = map(int, input().split())
dice = {a, b, c}
if len(dice) == 1:
    print(10000 + 1000 * a)
elif len(dice) == 2:
    # 조건부 표현식 (Conditional Expression) == 삼항 연산자(ternary operator)
    common_value = a if a == b or a == c else b
    print(1000 + common_value * 100)
else:
    print(max(dice) * 100)


# 2525 오븐 시계
# 이게 된다고??

# a, b = map(int, input().split())
# c = int(input())

# print((a + (b+c)//60) % 24, (b + c) % 60)


# restart 20241015


# 1271 //와 /의 차이를 제대로 알고 있니?

# 4153
# import sys
# a,b,c = map(int, sys.stdin.readline())
# if a**2 + b**2 == c**2:
#     print("right")
# else:
#     print("wrong")


# 2754 학점계산

# d1={
#     "A+": 4.3, "A0": 4.0, "A-": 3.7, "B+": 3.3, "B0": 3.0, "B-": 2.7, "C+": 2.3, "C0": 2.0, "C-": 1.7, "D+": 1.3, "D0": 1.0, "D-": 0.7,"F": 0.0
#     }
# grade = input()

# print(d1[grade])

"""

# since 2020

백준 코드 연습 및 기록 남겨놓기 
다른 사람것도 참고하기

# 1546
n = int(input())
a = list(map(int, input().split()))
sum = 0
m = max(a)
for i in a:
    sum += i/max(a)*100
print(sum/n)
n = map(int, input().split())
a = map(int, input().split())
sum = 0

n = int(input())
a = list(map(int,input().split()))
m = max(a)
for i in range(n):
    a[i] = a[i]/m*100
print(sum(a)/n)


# 18044719
numberlist.append(int(input()))

print(numberlist)
print(remainder)
numberlist=[]
remainder=[]
for i in range(10):
    numberlist.append(int(input()))
    remainder.append(numberlist[i] % 42)
print(len(set(remainder)))

c=0;l=[]
for i in range(10):
  a=int(input());r=a%42
  if r in l:
    continue
  else:
    l.append(r);c+=1
print(c)

s = set()
for i in range(10):
    s.add(int(input())%42)
print(len(s))

b = [int(input())%42 for i in range(10)]
print(len(set(b)))

a=int(input())
b=int(input())
c=int(input())
print(list(str('abcde'))
=>['a','b','c','d','e']
n=list(map(int,str(a*b*c)))
print(n)

for i in range(10):
    print(n.count(i))
    
for i in range(10):
    count = 0
    for j in range(len(n)):
        if n[j] == i:
            count += 1
    print(count)


nine=[]
for i in range(9):
    nine.append(int(input()))
for i in range(9):
    if max(nine)==nine[i]:
        print(max(nine))
        print(i+1)

l=[int(input())for i in range(9)]
print(max(l),l.index(max(l))+1)

n=int(input())
a=list(map(int,input().split()))
a=[list(map(int,input().split())) for _ in range(n)]
max=min= a[0]
for i in range(1,n):
    if a[i] > max:
        max=a[i]
for i in range(1,n):
    if a[i]< min:
        min=a[i]
print(min,max)

for i in a:
    if a[i]<=a[j]:
        print(a[j])
import sys
n=map(int,sys.stdin.readline())
a=map(int,sys.stdin.readline())
for i in a:
    if i>

a=int(input())
b=0
n=0
while a==b:
    if a<10:
        b=0 + a
        b=a%10 + b%10
    else:
    b=a//10 + a%10
    b=a%10 + b%10
    n+=1
print(n)

import sys
while 1:
    try:
        a,b= map(int, sys.stdin.readline().split())
        print(a+b)
    except:
        break
try:
    while 1>0:
        a,b=map(int,sys.stdin.readline().split())
        print(a+b)
except:
    exit()

import sys
while 1>0:
    a,b=map(int,sys.stdin.readline().split())
    if a!=0 and b!=0:
        print(a+b)
    else:
        break

import sys
n, x = map(int, sys.stdin.readline().split())
a=[i for i in sys.stdin.readline().split() if int(i)<x]
print(' '.join(a))

a=map(int,sys.stdin.readline().split())
b=[]
for i in a:
    if x>i:
        b.append(i)
for i in b:
    print(i,end=' ')
print(' '.join(map(str,b)))

import sys
n=int(sys.stdin.readline())+1
import sys
print('\n'.join(map(str, range(1, int(sys.stdin.read())))
print(i)

print('\n'.join(map(str, range(1, int(sys.stdin.read()) + 1))))

# 11022 A+B - 8

import sys
n=int(input())
for i in range(n):
    a,b=map(int, input().split())
    print('Case #{0}: {1} + {2} = {3}'.format(i+1,a, b, a+b))

n=int(input())
for i in range(n):
    print(' '*(n-i-1) +'*'*(i+1))

"""
