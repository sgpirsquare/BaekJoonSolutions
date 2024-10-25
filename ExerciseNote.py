"""
# 10811 바구니 뒤집기 지피티 도음을 받았음
box_num, ball_try = map(int, input().split())
boxes = [i + 1 for i in range(box_num)]
for _ in range(ball_try):
    start, end = map(int, input().split())
    # 슬라이싱 개념 일부만 떼어내어 다시 리스트를 만드는 것임
    # 따라서 중첩연산?이 가능하다 [][][]도 가능
    # 역순배열 [::-1]
    # [start:end:step]
    boxes[start - 1 : end] = boxes[start - 1 : end][::-1]
print(*boxes)

# 10811 반복문 사용버전 범용성이 좋음 다른 언어에도 적용가능
box_num, ball_try = map(int, input().split())
boxes = [i + 1 for i in range(box_num)]
for _ in range(ball_try):
    start, end = map(int, input().split())
    left, right = start - 1, end - 1
    while left < right:
        boxes[left], boxes[right] = boxes[right], boxes[left]
        left += 1
        right -= 1
print(*boxes)

# 10813 내 시도
box_num, ball_try = map(int, input().split())
boxes = [i + 1 for i in range(box_num)]
for _ in range(ball_try):
    first, second = map(int, input().split())
    temp = boxes[second - 1]
    boxes[second - 1] = boxes[first - 1]
    boxes[first - 1] = temp
print(*boxes)

# 10813 지피티 첨삭 수정
box_num, ball_try = map(int, input().split())
boxes = [i + 1 for i in range(box_num)]
for _ in range(ball_try):
    index1, index2 = map(int, input().split())
    boxes[index1 - 1], boxex[index2 - 1]=boxes[index2 - 1], boxex[index1 - 1]
print(*boxes)
# 10810 내 생각
box_num, ball_try = map(int, input().split())

boxes = [0 for _ in range(box_num)]
for _ in range(ball_try):
    box_start, box_end, ball_number = map(int, input().split())
    for i in range(box_start - 1, box_end):
        boxes[i] = ball_number

print(*boxes)

# boxes = [0 for _ in range(5)]
# print(boxes)

# 10810 지피티 첨삭
box_number, ball_try = map(int, input().split())
boxes = [0] * box_number
for _ in range(ball_try):
    start, end, ball = map(int, input().split())
    boxes[start - 1 : end] = [ball] * (end - start + 1)
print(*boxes)
# 25304
money = int(input())
shopping = int(input())
# sum = 0 sum은 예약어이다.
total_spent = 0
for i in range(shopping):
    # mon, shop = map(int, input().split())
    price, quantity = map(int, input().split())
    total_spent += price * quantity
if money == total_spent:
    print("Yes")
else:
    print("No")

# 25304 다른 사람꺼 보고 개선 complehension
money = int(input())
shopping = int(input())
sum = 0
for i in range(shopping):
    mon, shop = map(int, input().split())
    sum += mon * shop
print("Yes" if money == sum else "No")

# 24900 풀었음 예능 문제인거 같은데?

# 2440
n = int(input())
for i in range(n):
    print("*" * (n - i))



# # 2577 보류

# a = int(input())
# b = int(input())
# c = int(input())
# digit = [x for x in range(10)]
# digit_num =[]
# print(digit)
# d = a * b * c
# for i in range(10):
#     for j in digit:
#         if d


# 11720 첫
length = int(input())
number = str(input())
sum = 0
for i in range(length):
    sum += int(number[i])
print(sum)

# 11720 첨삭받은 버전
length = int(input())
number = input()
print(sum(int(number[i]) for i in range(length)))
# a = str(54321)
# print(int(a[0])+int(a[1]))
# 10818 4년 전에 코딩 개선
n=int(input())
numbers=list(map(int,input().split()))
if not numbers:
    pass
else:
    min_val = max_val = numbers[0]
for num in numbers[1:]:
    if num > max_val:
        max_val=num
    if num < min_val:
        min_val=num
print(min_val,max_val)

# 10818 맞췄다!
n = int(input()) # 파이썬에선 사실 필요없지만 배열 길이를 정해야하는 언어가 있어서 필요함.
numbers = list(map(int, input().split()))
print(min(numbers) , max(numbers))

# 10818 4년 전에 코딩한게 있네?? 내 사고방식 맞나? 헐..
n=int(input())
a=list(map(int,input().split()))

max=min= a[0]
for i in range(1,n):
    if a[i] > max:
        max=a[i]
for i in range(1,n):
    if a[i]< min:
        min=a[i]
print(min,max)


# 1152
print(len(list(input().split())))
# cnt_blank = 1
# for i in text:
#     if i==' ':
#         cnt_blank+=1
# print(cnt_blank)

# 4101 첫 시도 이 문제가 직각삼각형문제보다 먼저 풀었어야 한 거였네
while True:
    a,b = map(int, input().split())
    if (a,b)==(0,0):
        break
    if a>b:
        print("Yes")
    else:   
        print('No')

# 4101 첨삭 개선된 버전
while True:
    a,b = map(int, input().split())
    if a==0 and b==0:
        break
    print("Yes" if a>b else "No")
# 4153

# while True:
#     a, b, c = map(int, input().split())
#     if (a, b, c) == (0, 0, 0):
#         break
# # 아니 이 정렬 한 줄 빠졌다고...헉...
# # 예시 입력만 믿었던 게 낭패로군
# # 세 번의 길이만 준다고 했지 오름차순으로 준다고는 안 했으니 할 말은 없네
#     sides = sorted([a, b, c])
#     if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
#         print("right")
#     else:
#         print("wrong")

# 4153 개선시키기


def is_right_triangle(a, b, c):
    max_side = max(a, b, c)
    other_sides = [x for x in [a, b, c] if x != max_side]

    return other_sides[0] ** 2 + other_sides[1] ** 2 == max_side**2


while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break
    if is_right_triangle(a, b, c):
        print("right")
    else:
        print("wrong")


# 2675 문자열 반복
n = int(input())
for i in range(n):
    repeat_count, text = input().split()
    arr = []
    for j in range(len(text)):
        arr.append(int(repeat_count) * text[j])
    print(*arr, sep="")

python documentation
print(*objects, sep=' ', end='\n', file=None, flush=False)
result = ''.join(map(str, numbers))

# 2675 개선해보자
n = int(input())
for _ in range(n):
    repeat_count, text = input().split()
    repeat_count = int(repeat_count)
    result = "".join(char * repeat_count for char in text)

    print(result)

# 2738 행렬 덧셈
n, m = map(int, input().split())
mat_1 = []
mat_2 = []
for i in range(n):
    mat_1.append(list(map(int, input().split())))
for i in range(n):
    mat_2.append(list(map(int, input().split())))
for i in range(n):
    add_mat = []
    for j in range(m):
        add_mat.append(mat_1[i][j] + mat_2[i][j])
    print(*add_mat)

# 2738 개선된 버전 list complehension
n, m = map(int, input().split())
mat_1 = [list(map(int, input().split())) for _ in range(n)]
mat_2 = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    add_mat = [mat_1[i][j] + mat_2[i][j] for j in range(m)]
    print(*add_mat)

# 2738 개선된 버전 zip() 내장함수 활용
n, m = map(int, input().split())
mat_1 = [list(map(int, input().split())) for _ in range(n)]
mat_2 = [list(map(int, input().split())) for _ in range(n)]

for row_1, row_2 in zip(mat_1, mat_2):
    add_rows = [a + b for a, b in zip(row_1, row_2)]
    print(*add_rows)

# 10871 첫 시도
arr = []
n, a = map(int, input().split())
numbers = list(map(int, input().split()))
for i in numbers:
    if a > i:
        arr.append(i)
print(*arr)

# 10871 4년 전에 푼 소스가 있네
n, x = map(int, input().split())
a = map(int, input().split())
b = []
for i in a:
    if x > i:
        b.append(i)
for i in b:
    print(i, end=" ")

# 10871 챗지피티 개선시키기
n, a = map(int, input().split())
numbers = list(map(int, input().split()))
arr = [i for i in numbers if i < a]
print(*arr)
# 같은 효과인 것
print(' '.join(map(str, arr)))

# 10807 첫 시도
n = int(input()) #이 단계는 파이썬에선 불필요 동적 라스트이기 때문
m = map(int, input().split())
l = int(input())
cnt = 0
for i in m:
    if l == i:
        cnt += 1
print(cnt)

# 10807 첨삭 1
n = int(input())  
numbers = list(map(int, input().split()))  
target = int(input())  
count = 0  
for num in numbers:
    if num == target:
        count += 1  # 같으면 count를 1 증가
print(count)

# 10807 첨삭 2
n = int(input())  
numbers = list(map(int, input().split()))  
target = int(input())  
print(numbers.count(target))

# 5597 첫 시도? 와~시간 좀 걸리네 많이도 아이고;;
set_1 = [x for x in range(1, 31)]
set_2 = []
for i in range(28):
    set_2.append(int(input()))
diff = sorted(list(set(set_1) - set(set_2)))
print(diff[0])
print(diff[1])

# 5597 첨삭받은 것
set_1 = set(range(1, 31))
set_2 = set()
print("28개의 숫자를 하나씩 입력하세요:")
for _ in range(28):
    num = int(input())  # 숫자를 한 줄씩 입력받음
    set_2.add(num)  # 입력받은 숫자를 집합에 추가
missing_numbers = sorted(set_1 - set_2)
print(missing_numbers[0])
print(missing_numbers[1])

# 5597 첨삭받은 것 두 번째꺼
set_1 = set(range(1, 31))
set_2 = set()
print("28개의 숫자를 하나씩 입력하세요:")
for _ in range(28):
    num = int(input())  # 숫자를 한 줄씩 입력받음
    set_2.add(num)  # 입력받은 숫자를 집합에 추가
missing_numbers = set_1 - set_2
print(min(missing_numbers))
print(max(missing_numbers))

# 5597 숏코드를 가독성있는 코드로 바꾼 버전
all_numbers = set(range(1, 31))
input_numbers = set(map(int, open(0)))
missing_numbers = all_numbers ^ input_numbers
print(*missing_numbers)



# 9086 첫 시도
# n = int(input())
# for i in range(n):
#     s = list(input())
# ㅇㅇ 굳이 이럴 필요가 없는거네 음! -1 문법을 알았었는데도 적용을 못...
#     print(s[0] + s[len(s) - 1])

# 9086 개선된 코드 입력받자마자 바로 출력하기
# n = int(input())
# for _ in range(n):
#     s = input()
#     print(s[0] + s[-1])

# 9086 개선된 코드 리스트에 저장 후 출력하기
# T = int(input())
# arr = []

# for i in range(T):
#     S = input()
#     se = S[0] + S[-1]
#     arr.append(se)

# for j in arr:
#     print(j)


# 9086 더 개선된 코드
n = int(input())
arr = [s[0] + s[-1] for s in [input() for _ in range(n)]]

print("\n".join(arr))



# 5086
while True:
    a, b = map(int, input().split())
    # 이게 관문인것이여 이게 제일 먼저와야혀

    if a == 0 and b == 0:
        break

    if a % b == 0:
        print("multiple")
    elif b % a == 0:
        print("factor")
    else:
        print("neither")


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

a, b = map(int, input().split())
c = int(input())

print((a + (b+c)//60) % 24, (b + c) % 60)


# restart 20241015


# 1271 //와 /의 차이를 제대로 알고 있니?

# 4153
import sys
a,b,c = map(int, sys.stdin.readline())
if a**2 + b**2 == c**2:
    print("right")
else:
    print("wrong")


# 2754 학점계산

d1={
    "A+": 4.3, "A0": 4.0, "A-": 3.7, "B+": 3.3, "B0": 3.0, "B-": 2.7, "C+": 2.3, "C0": 2.0, "C-": 1.7, "D+": 1.3, "D0": 1.0, "D-": 0.7,"F": 0.0
    }
grade = input()

print(d1[grade])



# since 2020

# 백준 코드 연습 및 기록 남겨놓기 
# 다른 사람것도 참고하기

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
print('\n'.join(map(str, range(1, int(sys.stdin.read())))))
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
