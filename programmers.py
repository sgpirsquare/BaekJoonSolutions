########################################################
# pylint 오류메시지 끄기
# 학습용 파일이다보니 아래 세 개 경고는 잠시 끕니다.
# pylint: disable=W1401  # anomalous backslash in string
# pylint: disable=C0302  # too many lines in module
# pylint: disable=C0301  # line too long
# pylint: disable=W0105
########################################################
# pylance 오류메시지 끄기
# pyright: reportInvalidStringEscapeSequence=false
########################################################

"""   
# 문자열 정렬하기 (2) 이렇게 푸는걸 추천하네 다들 ord 함수수

def solution(my_string):
    answer = []
    for i in my_string:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            answer.append(chr(ord(i)+32))
        else:
            answer.append(i)
    return ''.join(sorted(answer))

# 문자열 정렬하기 (2)
def solution(my_string):
    answer = my_string.lower()
    return answer


my_string = "Bcad"
print(solution(my_string))

# 숫자 찾기


def solution(num, k):
    answer = 0
    if "k" in list(str(num)):
        answer = num.index("k")
    return answer


num = 29183
k = 1
# print(list(str(num)))
print(solution(num, k))
# 369게임


def solution(order):
    answer = 0
    order = str(order)
    if "3" in order or "6" in order or "9" in order:
        answer += 1
    return answer


order = 29423
print(solution(order))

# 배열 회전시키기
def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer.append(numbers[len(numbers) - 1])
        answer += numbers[:-1]
    if direction == "left":

        answer = numbers[1:]
        answer.append(numbers[0])

    return answer


numbers = [1, 2, 3]
direction = "left"
print(solution(numbers, direction))

# 인덱스 바꾸기


def solution(my_string, num1, num2):
    answer = ""
    temp = ""
    num1, num2 = int(num1), int(num2)
    temp = my_string[num1]
    my_string[num1] = my_string[num2]
    my_string[num2] = temp
    answer = my_string
    return answer


my_string = "hello"

print(my_string[1])
num1, num2 = 1, 2
print(solution(my_string, num1, num2))

# 문자열 뒤집기
my_string = "jaron"

reversed(my_string)
print(my_string)

# 숨어있는 숫자의 덧셈(1) 더 개선하기 isdigit()

my_string = "aAb1B2cC34oOp"
answer = sum(int(i) for i in my_string if i.isdigit())
print(answer)

# 숨어있는 숫자의 덧셈(1) 개선하기

my_string = "aAb1B2cC34oOp"
answer = 0
for num in my_string:
    try:
        answer += int(num)
    except:
        pass
print(answer)

# 숨어있는 숫자의 덧셈(1)

my_string = "aAb1B2cC34oOp"
answer = 0
for num in my_string:
    if (
        num == "0"
        or num == "1"
        or num == "2"
        or num == "3"
        or num == "4"
        or num == "5"
        or num == "6"
        or num == "7"
        or num == "8"
        or num == "9"
    ):
        answer += int(num)
print(answer)

# 중앙값 구하기
def solution(array):

    answer = sorted(array)[len(array) // 2]
    return answer


array = [9, -1, 0]
print(solution(array))
    
# 분수의 덧셈

# gcm은 math에 있지만 lcm은 python 3.9버전부터 있음.
# 프로그래머스의 python3은 버전이 3.8임
# gcd를 직접 만들어 쓰기도 해야 할 줄 알아야 함.
# 아래는 백준 문제 풀면서 만든 유클리드호제법으로 작성한 gcd
def gcd_custom(a, b):
    while b:
        a, b = b, a % b

    return a

#질문 게시판에 있던 DIY gcd
def GCD(a, b):
    while(b>0):
        a, b = b, a%b
    return a


print(gcd_custom(6, 4))
from math import gcd


def solution(numer1, denom1, numer2, denom2):
    # 분모의 최소공배수==통분
    lcm_denom = denom1 * denom2 // gcd(denom1, denom2)
    # 분자 덧셈 계산
    numer = numer1 * (lcm_denom // denom1) + numer2 * (lcm_denom // denom2)
    # 기약분수를 만들기 위해 분모와 분자에 나눠줄 분모 분자 최대공약수 구하기
    gcd_numer_denom = gcd(numer, lcm_denom)
    # 분모, 분자 최대공약수 실제로 나눠서 결과내기
    answer = [numer // gcd_numer_denom, lcm_denom // gcd_numer_denom]
    return answer

# 수열과 구간 쿼리 2
arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 2], [0, 3, 2], [0, 2, 2]]

# 수열과 구간 쿼리 3
def solution(arr, queries):
    for querie in queries:
        temp=arr[querie[0]]
        arr[querie[0]]=arr[querie[1]]
        arr[querie[1]]=temp
    return arr
# temp = arr[queries[0][0]]
# arr[queries[0][0]] = arr[queries[0][1]]
# arr[queries[0][1]] = temp

# print(arr)
# 등차수열의 특정한 항만 더하기
def solution(a, d, included):
    seq = []
    anwser = 0
    for _ in range(len(included)):
        a += d*i
        seq.append(a)
    for i in range(len(included)):
        if included[i] == "true":
            anwser += seq[i]
    return answer


# solution(3, 4, [true, false, false, true, true])

a = 3
d = 4
included = [True, False, False, True, True]
def solution(a,d,included):
    length = len(included)
    answer=0
    for i in range(length):
        if included[i] == True:
            answer+= a + d * i
    return answer

# 주사위 게임 2


def solution(a, b, c):
    sum = a + b + c
    set_point = {a, b, c}
    if len(set_point) == 3:
        answer = sum
    elif len(set_point) == 2:
        answer = sum * (pow(a, 2) + pow(b, 2) + pow(c, 2))
    elif len(set_point) == 1:
        answer = 3 * a * 3 * pow(a, 2) * 3 * pow(a, 3)

    return answer



# 조건 문자열
def solution(ineq, eq, n, m):
    answer = None
    if ineq == ">" and eq == "=":
        answer = int(n >= m)
    elif ineq == "<" and eq == "=":
        answer = int(n <= m)

    elif ineq == ">" and eq == "!":
        answer = int(n > m)
    elif ineq == "<" and eq == "!":
        answer = int(n < m)

    return answer


print(solution(">", "!", 7, 5))

# A 강조하기


def solution(myString):
    for i in range(len(myString)):
        if myString[i] == "a":
            myString[i] = "A"
        else:
            myString[i] = myString[i].lower()

    answer = myString
    return answer


my_String = "abstract algebra"

print(solution(my_String))

# 공백으로 구분하기 1


def solution(my_string):
    answer = list(my_string.split())
    return answer


my_string = "i love you"

print(solution(my_string))
#  이어 붙인 수
def solution(num_list):
    even, odd = "", ""
    for i in num_list:
        if int(i) % 2 == 0:
            even += str(i)
        else:
            odd += str(i)

    answer = int(even) + int(odd)

    return answer


num_list = [3, 4, 5, 2, 1]
print(solution(num_list))

# 함수작성


def solution(n):
    answer = 0
    if n % 2 == 0:
        for i in range(0, n + 1, 2):
            answer += pow(i, 2)
    else:
        for i in range(1, n + 1, 2):
            answer += i

    return answer



print(solution(int(input())))

# 함수 작성
def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s + len(overwrite_string) :]
    return answer


my_string, overwrite_string, s = input().split()
s = int(s)

print(solution(my_string, overwrite_string, s))
He11oWor1d lloWorl 2
Program29b8UYP merS123 7
ProgrammerS123

#
print("!@#$%^&*(\\'\"<>?:;")
#
str = input()

print(str.swapcase())

"""
