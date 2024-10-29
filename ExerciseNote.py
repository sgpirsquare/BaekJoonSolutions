# 5073 개선시키기
while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break
    if a + b <= c or b + c <= a and c + a <= b:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif len({a, b, c}) == 2:
        print("Isosceles")
    else:
        print("Scalene")

"""
# 5073 
while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break
    isTriangle = a + b > c and b + c > a and c + a > b
    set_Isosceles = {a, b, c}
    if isTriangle is False:
        print("Invalid")
    elif a == b == c and a * b * c != 0:
        print("Equilateral")
    elif len(set_Isosceles) == 2:
        print("Isosceles")
    else:
        print("Scalene")


# 15727 개선시키기
l = int(input())
# 헉...뭔데 이 코드...와우..
print((l + 4) // 5)

# 올림을 정수 나눗셈으로 구현하는 방법
# 정수 나눗셈 기반 올림 처리 (Celling Division using Integer Arithmetic)
# Simulating Celling Division
# Integer-based Ceilling Trick
# Rounded-up Integer Division
# 올림을 위한 보정값 추가
# 15727번 문제의 본질은 주어진 수 l을 5로 나눈 값에 대한 올림이다.

# 15727
l = int(input())
print(l // 5 if l % 5 == 0 else l // 5 + 1)

# 2798 개선버전
n, m = map(int, input().split())
cards = list(map(int, input().split()))
max_sum = 0  # m 이하의 최대 합
# 리스트 안 만들어도 되는데 메모리 낭비했었군..
# 리스트부터 만드는 습관이 들었다?
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            total = cards[i] + cards[j] + cards[k]
            if total <= m:  # m 이하일 때만 최대값 갱신
                max_sum = max(max_sum, total)
print(max_sum)
# 2798 # 24267이랑 연결됨
n, m = map(int, input().split())
cards = list(map(int, input().split()))
totals = []
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            totals.append(cards[i] + cards[j] + cards[k])
less_than_m = []
for total in totals:
    if m >= int(total):
        less_than_m += [total]
print(max(less_than_m))
# if m >= max(totals):
# sorted_totals = sorted(totals)



# 24267 시간 복잡도 계산하기
n = int(input())
print(n * (n - 1) * (n - 2) // 6)
print(3)

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 2
#         for j <- i + 1 to n - 1
#             for k <- j + 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }
# n*(n-1)*(n-2)//6
# i: n - 2 - 1 + 1 = n - 2
# j: n - 1 - i - 1 + 1 = n - i - 1
# k: n - j - 1 + 1 = n - j
# 저게 아니고
# i는 n-2까지의 값을 가진다 왜냐
# j는 i보다 1만큼 큰 값부터 선택한다
# j가 i+1부터 시작한다고 했으니 그렇게 해석가능하다.
# 또한 k도 j보다 1만큼 큰 값부터 선택한다.
# 왜냐하면 k<-j+1이라고 되어 있기 때문
# 결국 위 3중첩 반복문은 1<=i<j<k<=n의 구조를 가진다.
# n은 자연수이므로 1부터 n까지의 자연수 중 세 개를 순서없이 중복없이 선택하는 경우의 수 즉 n Combination 3 이 되는 구조이다.
# 따라서 n*(n-1)*(n-2)//6

# 24266
n = int(input())
print(n**3)
print(3)

# 24265 개선시키기
n = int(input())
print(n * (n - 1) // 2)
print(2)

# 24265
n = int(input())
sum = 0
#sum은 예약어 함수명이라 total로 바꾸길 권장함
for i in range(n):
    sum += i
print(sum)
print(2)


# 1157
words = input().upper()
alphabets = "ABCDEFGFIJKLMNOPQRSTUVWXYZ"
list_letter = [0] * len(alphabets)
for i in range(len(alphabets)):
    for j in words:
        if alphabets[i] == j:
            list_letter[i] += 1
print(list_letter)
# for i in alphabets:
#     if
print(words)
print(max(list_letter))

# 24264
n = int(input())
print(n**2)
print(2)

#24263
n=int(input())
print(n)
print(1)

#24262
n=int(input())
print(1)
print(0)

# 9506 개선시키기
while True:
    n = int(input())
    if n == -1:
        break
    div = [i for i in range(1, n) if n % i == 0]
    if sum(div) == n:
        equation = f"{n} = " + " + ".join(map(str, div))
        print(equation)
    else:
        print(f"{n} is NOT perfect.")
    # perfect라고 적었다고 틀리냐 perfect.라고 해야 맞고 허참

# 9506
while True:
    n = int(input())
    if n == -1:
        break
    div = [i for i in range(1, n) if n % i == 0]
    if sum(div) != n:
        print(f"{n} is NOT perfect.")
    # perfect라고 적었다고 틀리냐 perfect.라고 해야 맞고 허참
    else:
        rearr = []
        rearr += [n] + ["="]
        for i in range(len(div) - 1):
            rearr += [div[i]] + ["+"]
        rearr += [div[-1]]
        print(*rearr)


# 2501 list comprehension
n, k = map(int, input().split())
div = [i for i in range(1, int(n**0.5) + 1) if n % i == 0]
# 대칭 약수(paired divisor or symmetric divisor) 개념
div += [n // i for i in div if i != n // i]
div.sort()
print(0 if len(div) < k else div[k - 1])

# 2501
n, k = map(int, input().split())
div = []
for i in range(1, n + 1):
    if n % i == 0:
        div += [i]

print(0 if len(div) < k else div[k - 1])


# 10101 개선하기
ang_1 = int(input())
ang_2 = int(input())
ang_3 = int(input())

sum_ang = ang_1 + ang_2 + ang_3
set_Isosceles = {ang_1, ang_2, ang_3}
if sum_ang != 180:
    print("Error")
elif ang_1 == ang_2 == ang_3 == 60:
    print("Equilateral")
elif len(set_Isosceles) == 2:
    print("Isosceles")
else:
    print("Scalene")

# 10101
ang_1 = int(input())
ang_2 = int(input())
ang_3 = int(input())
sum_ang = ang_1 + ang_2 + ang_3
set_Isosceles = {ang_1, ang_2, ang_3}
if sum_ang != 180:
    print("Error")
if sum_ang == 180 and len(set_Isosceles) == 3:
    print("Scalene")
if ang_1 == ang_2 == ang_3 == 60:
    print("Equilateral")
if sum_ang == 180 and len(set_Isosceles) == 2:
    print("Isosceles")



# 15894
print(4 * int(input()))

# 10988 반복문으로 개선하기 긴 문자열에선 오히려 효율적
text = input()
is_palindrome = 1
for i in range(len(text) // 2):
    if text[i] != text[-(i + 1)]:
        is_palindrome = 0
        break
print(is_palindrome)

# 10988 팰린드롬 회문문자
text = input()
# print(1 if text == text[::-1] else 0)
# reversed_text = "".join(reversed(text))
# print(1 if text == reversed_text else 0)
print(1 if text == "".join(reversed(text)) else 0)


# 2444 다른 사람 코드 참고용
n = int(input())
for i in range(1, n):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# 2444 개선시키기
n = int(input())
for i in range(n):
    spaces = " " * (n - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)
for i in range(n - 2, -1, -1):
    spaces = " " * (n - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)

# 2444
n = int(input())
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
for i in range(n - 1):
    print(" " * (i + 1) + "*" * (2 * (n - i - 1) - 1))

# 3003 개선시키기
pieces = [1, 1, 2, 2, 2, 8]
existing = list(map(int, input().split()))
result = [pieces[i] - existing[i] for i in range(6)]
# zip() 사용하기
# result = [ p - e for p,e in zip(pieces, existing)]
print(*result)

# 3003
pieces = [1, 1, 2, 2, 2, 8]
piece_exist = list(map(int, input().split()))
result = [0] * 6
for i in range(6):
    result[i] = pieces[i] - piece_exist[i]
print(*result)


# 2566 개선시키기
mat = []
max_value = -1
max_row, max_col = 0, 0

for i in range(9):
    row = list(map(int, input().split()))
    mat.append(row)
    for j in range(9):
        if row[j] > max_value:
            max_value = row[j]
            max_row, max_col = i + 1, j + 1
print(max_value)
print(max_row, max_col)

# 2566
mat = []
maxes = []
for i in range(9):
    mat.append(list(map(int, input().split())))
for i in range(9):
    maxes.append(max(x for x in mat[i]))
print(max(maxes))
mat_row = maxes.index(max(maxes)) + 1
mat_column = mat[mat_row - 1].index(max(maxes)) + 1
print(mat_row, mat_column)

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
    print(*add_mat.)


# 3009 개선시키기
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())

list_p = [a1, a2, a3]
list_q = [b1, b2, b3]

x4 = [x for x in list_p if list_p.count(x) == 1][0]
y4 = [y for y in list_q if list_q.count(y) == 1][0]

print(x4, y4)

# 3009
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())

list_point = [[a1, b1], [a2, b2], [a3, b3]]

list_p = [a1, a2, a3]
list_q = [b1, b2, b3]
listset_p = list(set(list_p))
listset_q = list(set(list_q))

list_all = [
    [listset_p[0], listset_q[0]],
    [listset_p[0], listset_q[1]],
    [listset_p[1], listset_q[0]],
    [listset_p[1], listset_q[1]],
]
result = [x for x in list_all if x not in list_point]

print(*result[0])

# 2577
a = int(input())
b = int(input())
c = int(input())
list_abc = list(str(a * b * c))
for i in range(10):
    suma = 0
    for j in range(len(list_abc)):
        if i == int(list_abc[j]):
            suma += 1
    print(suma)


# 2577 개선시키기
from collections import Counter

a = int(input())
b = int(input())
c = int(input())

# 문자열로 변환된 곱셈 결과의 등장 횟수를 카운트
result = str(a * b * c)
counter = Counter(result)

# 0부터 9까지 등장 횟수 출력
for i in range(10):
    print(counter.get(str(i), 0))

# 2577 개선시키기
a = int(input())
b = int(input())
c = int(input())
result = str(a * b * c)
count = [0] * 10
for char in result:
    count[int(char)] += 1

for cnt in count:
    print(cnt)

# 2577 4년 전 코드 2020년 8월 내가 무슨 일들을 해왔던거야?
a = int(input())
b = int(input())
c = int(input())
n = list(map(int, str(a * b * c)))
for i in range(10):
    print(n.count(i))

# a = "1213450"
# list_a = list(a)
# print(list_a)
# print(0 == int(list_a[6]))
# print(list_a[6])

# 1085 개선판
px, py, width, height = map(int, input().split())
print(min(width - px, px, height - py, py))

# 1085
x, y, w, h = map(int, input().split())
print(min(abs(x - w), abs(x - 0), abs(h - y), abs(y - 0)))


# 2745 pythonic
# N, B = input().split()
# print(int(N, int(B)))

# 2745 일반적인 방식 진법변환공식 사용
def base_to_decimal(num_str, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0

    # for i, char in enumerate(reversed(num_str)):
    # enumerate, reversed 사용하지 않고
    length = len(num_str)
    for i in range(length):
        char = num_str[length - 1 - i]
        value = digits.index(char)
        result += value * (base**i)
    return result

N, B = input().split()
print(base_to_decimal(N, int(B)))

# 27323
width = int(input())
length = int(input())
print(width * length)

# 10809
word_text = list(input())
alphabets_number = [-1 for _ in range(97, 123)]
for i in range(97, 123):
    for j in range(len(word_text)):
        if word_text[j - 1] != word_text[j]:
            pass
            if chr(i) == word_text[j]:
                alphabets_number[i - 97] = j
print(*alphabets_number)

# 2908 첨삭받은 후 리코딩
number1, number2 = input().split()
rev1, rev2 = int(number1[::-1]), int(number2[::-1])
print(rev1 if rev1 > rev2 else rev2)
# print(max(rev1,rev2))도 괜찮음 내장함수 활용

# 2908 상수
number1, number2 = input().split()
reverse_n1, reverse_n2 = number1[::-1], number2[::-1]
print(reverse_n1 if reverse_n1 > reverse_n2 else reverse_n2)


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


# 10813 지피티 첨삭 수정
box_num, ball_try = map(int, input().split())
boxes = [i + 1 for i in range(box_num)]
for _ in range(ball_try):
    index1, index2 = map(int, input().split())
    boxes[index1 - 1], boxex[index2 - 1]=boxes[index2 - 1], boxex[index1 - 1]
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


# 10810 지피티 첨삭
box_number, ball_try = map(int, input().split())
boxes = [0] * box_number
for _ in range(ball_try):
    start, end, ball = map(int, input().split())
    boxes[start - 1 : end] = [ball] * (end - start + 1)
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

# 25304 다른 사람꺼 보고 개선 complehension
money = int(input())
shopping = int(input())
sum = 0
for i in range(shopping):
    mon, shop = map(int, input().split())
    sum += mon * shop
print("Yes" if money == sum else "No")
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

# 11720 첨삭받은 버전
length = int(input())
number = input()
print(sum(int(number[i]) for i in range(length)))
# a = str(54321)
# print(int(a[0])+int(a[1]))

# 11720 첫
length = int(input())
number = str(input())
sum = 0
for i in range(length):
    sum += int(number[i])
print(sum)


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

# 4101 첨삭 개선된 버전
while True:
    a,b = map(int, input().split())
    if a==0 and b==0:
        break
    print("Yes" if a>b else "No")
# 4101 첫 시도 이 문제가 직각삼각형문제보다 먼저 풀었어야 한 거였네
while True:
    a,b = map(int, input().split())
    if (a,b)==(0,0):
        break
    if a>b:
        print("Yes")
    else:   
        print('No')


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

# 4153

while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break
# 아니 이 정렬 한 줄 빠졌다고...헉...
# 예시 입력만 믿었던 게 낭패로군
# 세 번의 길이만 준다고 했지 오름차순으로 준다고는 안 했으니 할 말은 없네
    sides = sorted([a, b, c])
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print("right")
    else:
        print("wrong")


# 2675 개선해보자
n = int(input())
for _ in range(n):
    repeat_count, text = input().split()
    repeat_count = int(repeat_count)
    result = "".join(char * repeat_count for char in text)

    print(result)


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



# 10871 챗지피티 개선시키기
n, a = map(int, input().split())
numbers = list(map(int, input().split()))
arr = [i for i in numbers if i < a]
print(*arr)
# 같은 효과인 것
print(' '.join(map(str, arr)))

# 10871 4년 전에 푼 소스가 있네
n, x = map(int, input().split())
a = map(int, input().split())
b = []
for i in a:
    if x > i:
        b.append(i)
for i in b:
    print(i, end=" ")

# 10871 첫 시도
arr = []
n, a = map(int, input().split())
numbers = list(map(int, input().split()))
for i in numbers:
    if a > i:
        arr.append(i)
print(*arr)

# 10807 첨삭 2
n = int(input())  
numbers = list(map(int, input().split()))  
target = int(input())  
print(numbers.count(target))

# 10807 첨삭 1
n = int(input())  
numbers = list(map(int, input().split()))  
target = int(input())  
count = 0  
for num in numbers:
    if num == target:
        count += 1  # 같으면 count를 1 증가
print(count)

# 10807 첫 시도
n = int(input()) #이 단계는 파이썬에선 불필요 동적 라스트이기 때문
m = map(int, input().split())
l = int(input())
cnt = 0
for i in m:
    if l == i:
        cnt += 1
print(cnt)


# 5597 숏코드를 가독성있는 코드로 바꾼 버전
all_numbers = set(range(1, 31))
input_numbers = set(map(int, open(0)))
missing_numbers = all_numbers ^ input_numbers
print(*missing_numbers)

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

# 5597 첫 시도? 와~시간 좀 걸리네 많이도 아이고;;
set_1 = [x for x in range(1, 31)]
set_2 = []
for i in range(28):
    set_2.append(int(input()))
diff = sorted(list(set(set_1) - set(set_2)))
print(diff[0])
print(diff[1])


# 9086 개선된 코드 입력받자마자 바로 출력하기
# n = int(input())
# for _ in range(n):
#     s = input()
#     print(s[0] + s[-1])

# 9086 더 개선된 코드
n = int(input())
arr = [s[0] + s[-1] for s in [input() for _ in range(n)]]

print("\n".join(arr))

# 9086 개선된 코드 리스트에 저장 후 출력하기
# T = int(input())
# arr = []

# for i in range(T):
#     S = input()
#     se = S[0] + S[-1]
#     arr.append(se)

# for j in arr:
#     print(j)

# 9086 첫 시도
# n = int(input())
# for i in range(n):
#     s = list(input())
# ㅇㅇ 굳이 이럴 필요가 없는거네 음! -1 문법을 알았었는데도 적용을 못...
#     print(s[0] + s[len(s) - 1])



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


# 2480 챗지피티가 첨삭해준 것
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
