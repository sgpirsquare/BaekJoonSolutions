# pylint 오류메시지 끄기
# 학습용 파일이다보니 아래 세 개 경고는 잠시 꺼둬야겠다.
# pylint: disable=W1401  # anomalous backslash in string
# pylint: disable=C0302  # too many lines in module
# pylint: disable=C0301  # line too long
########################################################
# 에라토스테네스의 체
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


number = int(input())
print(is_prime(number))

"""
# 30328 개선하기
n = print(4000 * int(input()))

# 30328 예능용 문제인듯
n = int(input())
print(4000 * n)
# 1934 개선하기
from math import lcm

n = int(input())
results = []

for _ in range(n):
    try:
        num1, num2 = map(int, input().split())
        results.append(str(lcm(num1, num2)))
    except ValueError:
        print("Invalid input. Please enter two integers.")

print("\n".join(results))

# 1934
from math import gcd, lcm

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b))

# 2609 개선하기
import math

a, b = map(int, input().split())
gcd = math.gcd(a, b)
lcm = math.lcm(a, b)
# lcm = (a * b) // gcd
print(gcd)
print(lcm)

# 2609
a, b = map(int, input().split())
gcd = 0
for i in range(1, max(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print(gcd)
print(int(a // gcd) * b)

# 10828 딕셔너리를 사용하자 당장은 보류. 챗지피티에 너무 의존하는 경향성때문에 이건 스포를 봐버렸다.
# 물론 코드를 스쳐봐서 아예 짤 수 있는 상태는 아니지만....
# 그 정도만으론 체화되지 않기 때문에 절대 천재가 아닌 이상 그렇게는 되살려 짜지 못 한다는 걸 이 글을 읽는 사람 누구나 공감할거다.
# 답 안볼래
n = int(input())
for _ in range(n):
    command = list(map(str, input().split()))

print(command)


push x top size empty pop 
14
n=int(input())

stack=[]

push 1
stack.append(1)

push 2
stack.append(2)

top
stack[-1]

size
len(stack)

empty
if stack:
    print(1)
    else:
        print(0)

pop
if stack:
    stack.pop()
else:
    print(-1)

stack.pop if stack else print(-1)

pop
if stack:
    stack.pop()
else:
    print(-1)

pop
if stack:
    stack.pop()
else:
    print(-1)

size
len(stack)

empty
if stack:
    print(1)
    else:
        print(0)

pop
if stack:
    stack.pop()
else:
    print(-1)

push 3

empty
top

# 21598 예능용문제인가;
N = int(input())
for _ in range(N):
    print("SciComLove", end="\n")
# 16170 개선하기
from datetime import datetime, timedelta

utc_now = datetime.utcnow()
seoul_time = utc_now + timedelta(hours=9)

print(seoul_time.year)
print(seoul_time.month)
print(seoul_time.day)

# 16170 시간다루기 공식문서를 읽고 해석하려 노력했지만 코드 튜터의 도움으로 그걸 알게 되었다.
# datetime objects에서 class datetime.datetime() 이렇게 사용하는게 기본이고
# object>class>(class)method의 위계가 있기때문에 사용할때 주의해야한다.
from datetime import datetime

utc_now = datetime.utcnow()
seoul_time = utc_now.replace(hour=(utc_now.hour + 9) % 24)

print(seoul_time.year)
print(seoul_time.month)
print(seoul_time.day)

# 16170 다른 사람 코드
import datetime

time = datetime.datetime.now() - datetime.timedelta(hours = 9)

print(time.year)
print(time.month)
print(time.day)

# 1978 개선하기
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


N = int(input())
numlist = map(int, input().split())

primes = sum(1 for number in numlist if is_prime(number))

print(primes)

# 1978 이렇게 짠 코드도 있음 헉! 소수개수 세는걸 따로 안 하고 그냥 n으로 퉁침.
n = int(input())
nums = list(map(int, input().split()))

for num in nums:
  if num < 2:
    n -= 1
    continue
  
  for i in range(2, num):
    if num % i == 0:
      n -= 1
      break

print(n)

# 1978 소수 찾기 N<-=100 N개의 수 <=1000 잠시 보류
# 챗지피티 code tutor의 도움을 받았다
# 도움받고 나니 나혼자 생각해서 끝까지 풀었어야 했다는 찜찜한 생각을 지울 수 없다.으으!!
N = int(input())
numlist = map(int, input().split())

primes = 0

for number in numlist:
    if number <= 1:
        pass
    else:
        for i in range(2, int((number**0.5) + 1)):
            if number % i == 0:
                break
        else:
            primes += 1

print(primes)


# 10989 계수 정렬 counting sort 코드 개선 => 이건 안 됨. 메모리 제한이 빡빡한 경우는 하나씩 출력하는게 더 나음.
import sys

input = sys.stdin.readline
# output은 생각보다 메모리를 상대적으로 더 잡아먹음 print가 차라리 나음
output = sys.stdout.write

n = int(input())
num_list = [0] * 10001
for i in range(n):
    num_list[int(input())] += 1
for i in range(10001):
    if num_list[i] != 0:
        output((str(i) + "\n") * num_list[i])
        # 이렇게 개선해야 함
        # for _ in range(num_list[i]):
        #     output("f{i}\n")
        # 위 코드도 사실 메모리를 상대적으로 더 잡아먹음
        # 차라리 아래처럼 해야 함.
        # print(i)
# 10989 계수 정렬 counting sort 연습 입출력 추가!!!?
# 이걸로 제출했는데 통과했다!?!!!와우!!!
# 14트만에!휴!!!와..자료구조와 알고리즘의 중요성....
# 하드웨어의 제한으로 인해 구현만으로 끝내선 안된다는 것도 알게 됨.

import sys

input = sys.stdin.readline
n = int(input())
num_list = [0] * 10001
for i in range(n):
    num_list[int(input())] += 1
for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)

# 10989 문제해결을 위한 계수 정렬 연습 counting sort
import sys

input = sys.stdin.readline
n = int(input())

arr = [4, 2, 2, 8, 3, 9, 10, 5, 3, 5, 3, 1]
cnt = [0] * max(arr)
# print(cnt)
for i in arr:
    cnt[i - 1] += 1
# print(cnt)
# [1,2,2,1,0,0,0,1]
# 1이 1개,2가 2개,3이 2개,4가 1개,...,8이 1개 출력

# 아래 코드를 직관적으로 짰다. 논리적 이해 필요함.
for i in range(max(arr)):  # 정렬하고자 하는 수열의 항 중 자연수 최댓값 개수까지
    for j in range(cnt[i]):  # 정렬대상 수열의 각 항의 반복횟수(cnt)만큼 순회함
        print(
            i + 1, end=" "
        )  # cnt 인덱스 자체가 정렬하고자 하는 수열의 항 그 자체의 값이다

# 10989 수 정렬하기 3 최대 난제다. 벌써 몇 번째 시도냐..;;;
# 1<=N<=10^7개의 수를 입력하는데 이때 입력되는 수는 10000보다 작거나 같은 수이다. 질문게시판 글 읽다가 계수 정렬(counting sort)에 대한 키워드를 얻었다.
# 와. 지금까지는 챗지피티가 찾아준 글로 어느 정도 학습이 되었는데
# 지금 이 문제를 해결하기 위한 계수정렬은 아주 극단적인 자주 쓰이지 않는 알고리즘이라
# 그런지 왠만한 알고리즘 책에도 잘 등장하지 않다. 적어도 내가 가진 알고리즘 책엔 없다.
# 챗지피티에게서 왠만한 문답으로 뚫고 나갔지만 정렬부터는, 특히 계수 정렬은 구글링을 결국 하게 만들고 있으며 여러 블로그 글을 읽게 만든다. 와우.
# 시작을 이렇게 해야한다. 수열이 아닌 항을 리스트로 잡아야한다.
# number = [0] * 10000
# 또한 입력 출력도 왠만하면 시간을 줄일 수 있는 방법으로 최대한 선택해야한다.
# 잠깐..---수의 범위가 작다면 카운팅 정렬을 사용하여 더욱 빠르게 정렬할 수 있습니다.---라고 설명이 되어있었네?!!!???럴수...
# import sys

# input = sys.stdin.readline
# n = int(input())
# num_list = [0] * 10001
# for i in range(n):
#     num_list[int(input().rstrip())] += 1
# for i in range(10001):
#     if num_list[i] != 0:
#         print(num_list[i])


# 10989 수 정렬하기 3 1<=N<=10,000,000 구현만 한다고 절대 득점하지 못 한다;;;공부가 필요하겠다.
# 퀵정렬?
# sort를 사용하라는 권유가 있었는데 안되네. 다시 시도한다. 휘리릭
import sys

input_stdin = sys.stdin.readline
n = int(input_stdin().strip())

numbers = [int(input_stdin().strip()) for _ in range(n)]

numbers.sort()

for i in range(n):
    print(numbers[i])



# 2751 이렇게 극단적인 경우도 존재함! 속도 input()<sys.stdin.readline() open(0)
print(*sorted(map(int, [*open(0)][1:])))

# 2751 피드백 받음 1<=N<=1,000,000 정도된다면 sys.stdin.readline() 추가처리없는 입력, 반복문으로 한줄씩 출력이 시간, 메모리에서 엄청나게 유리함.
import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    # 여기서도 input을 sys.stdin.readline()으로 해야 시간절약 됨.
    # arr.append(int(input()))
    arr.append(int(sys.stdin.readline()))
arr.sort()
# 이게 메모리를 많이 잡아먹는 방식이라고 함. 언패킹말여.
# print(*arr, sep="\n")
# 반복문으로 하나씩 출력하는게 오히려 시간이 적게 걸린다고 함.
for i in range(n):
    print(arr[i])

# 2751  N(1 ≤ N ≤ 1,000,000) 이대로 짜면 시간 너무 걸린다? 시간복잡도는 O(NlogN)이라서 괜찮은데???
# 입력방법을 바꿔보라고??
# 그래도 시간초과되는데?
# 보류여
# 이건 안 되는데 왜 아래 코드는 되는거지?
import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
# 이게 메모리를 많이 잡아먹는 방식이라고 함. 언패킹말여.
print(*arr, sep="\n")

# 2751 다른 사람 코드임 이건 python3로 제출해서 맞췄던데 차이가 뭐야
import sys

input = sys.stdin.readline

N = int(input())
l = [int(input()) for _ in range(N)]
l.sort()

for i in range(N):
    print(l[i])

# 2751  다시 시도하기 pypy3로 제출하니까 맞췄네? 뭐지??
import heapq

n = int(input())
arr = []
for _ in range(n):
    heapq.heappush(arr, int(input()))
for _ in range(n):
    print(heapq.heappop(arr))


# 24313 구글링으로 답을 봐버리고 말았는데 f와 g의 그래프(직선의 방정식, 일차함수)를 그려보면 기존 내 코드가 왜 틀렸는지 더 수긍이 가게 되어있다.
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

f = a1 * n0 + a0
g = c * n0

if g - f >= 0 and c >= a1:
    print(1)
else:
    print(0)

# n >= n0

# 아래는 필요없다.
# f1 = a1 * (n0 + 1) + a0
# g1 = c * (n0 + 1)

# 24313 if 조건문이 필요한 이유 matplotlib로 그린 것 코드

import matplotlib.pyplot as plt
import numpy as np

# 예시 값을 설정합니다.
a1, a0 = 2, 1  # f(n)의 계수와 상수항
c = 3  # g(n)의 계수
n0 = 1  # 시작점 n0

# n 범위 설정
n = np.linspace(0, 10, 400)  # 0에서 10까지 400개의 점을 생성합니다.

# 함수 정의
f_n = a1 * n + a0
g_n = c * n

# 그래프 그리기
plt.plot(n, f_n, label="f(n) = a1 * n + a0", color="blue")
plt.plot(n, g_n, label="g(n) = c * n", color="red")
plt.axvline(x=n0, color="green", linestyle="--", label="n0")

# 교차점 이후의 조건 영역 표시
plt.fill_between(n, f_n, g_n, where=(n >= n0) & (f_n <= g_n), color="yellow", alpha=0.2)

# 그래프 설명
plt.xlabel("n")
plt.ylabel("Function values")
plt.legend()
plt.title("Graph of f(n) and g(n) with condition f(n) <= g(n) for n >= n0")
plt.grid(True)

plt.show()



# 24313 틀렸다.
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

# n >= n0
f = a1 * n0 + a0
g = c * n0

f1 = a1 * (n0 + 1) + a0
g1 = c * (n0 + 1)


if g - f >= 0 and g1 - f1 >= 0:
    print(1)
else:
    print(0)



# 25305
n, k = map(int, input().split())
score = list(map(int, input().split()))
score.sort()
print(score[-k])

# 2587 문제조건이 제한되어 있어서 그렇지 사실은 퀵, 힙 등을 사용해야하는 엄청난 배경이 담긴 문제ㅣ다
num = [int(input()) for _ in range(5)]
num.sort()
print(sum(num) // 5)
print(num[2])
# 2750 개선시키기
n = int(input())
num = [int(input()) for _ in range(n)]
num.sort()
print(*num, sep="\n")


# 2750
n = int(input())
num = []
for i in range(n):
    m = int(input())
    # 아래 연산이 1+2+3...range(n)이라서 O(n^2) 복잡도를 갖는다. 의외네
    num += [m]
#함수 sorted()는 리스트를 한 개 더 만든다. 리스트는 적게 만들 수 있다면 적게 하는게 좋다. 메소드 sort()는 기존 존재하던 리스트의 원소들을 오름차순으로 정렬한다. 리스트를 더 만들지 않는다.
for number in sorted(num):
    print(number)


# 5622 나중에 하지
dialring = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"],
    ["J", "K", "L"],
    ["M", "N", "O"],
    ["P", "Q", "R", "S"],
    ["T", "U", "V"],
    ["W", "X", "Y", "Z"],
]
sentence= input()
for word in sentence:
    if word in 
print("D" in dialring[0])
# 10809 습득 공부할 거리가 좀 있네

# 10809 다른 각도에서 다시 보기 2 ==> find 함수 찾고자 하는 문자의 첫 위치를 반환함
word_text = input()
result_number = [word_text.find(chr(i)) for i in range(97, 123)]
print(*result_number)

# 10809 다른 각도에서 다시 보자 ==> 문자열 다루기 위해 필요한 함수 enumerate, ord, chr
word_text = input()
result_number = [-1] * 26

for index, char in enumerate(word_text):
    char_index = ord(char) - 97
    if result_number[char_index] == -1:
        result_number[char_index] = index
    # 이 조건문은 -1이 아니면(알파벳이 발견되었으면) 알파벳 처음 발견된 인덱스를 갱신하지 않겠다는 의미. 최초 발견 인덱스만 넣겠다는 뜻.

print(*result_number)


# 10809 다른 방식으로 접근해보자=>겨우 풀긴했는데 상당히 저급;;;수준;;; why? 이중반복문에 리스트도 두 개나 만들어버림.
word_text = list(input())
alphabets_number = [[-1] for _ in range(97, 123)]
for i in range(97, 123):
    for j in range(len(word_text)):
        if chr(i) == word_text[j]:
            alphabets_number[i - 97] += [j]
result_number = [0 for _ in range(97, 123)]

for i in range(len(alphabets_number)):
    if len(alphabets_number[i]) == 1:
        result_number[i] = -1
    else:
        result_number[i] = alphabets_number[i][1]

print(*result_number)


# 10809 보류였는데
word_text = list(input())
alphabets_number = [-1 for _ in range(97, 123)]
for i in range(97, 123):
    for j in range(len(word_text)):
        if word_text[j] != word_text[j + 1]:
            pass
            if chr(i) == word_text[j]:
                alphabets_number[i - 97] = j
print(*alphabets_number)

# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# a b  c  d e  f  g  h  i j k  l  m n o  p  q  r  s  t  u  v  w  x  y  z
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

# 10250 보류 시도
frequency = int(input())
results = []
for _ in range(n):
    h, w, n= map(int, input().split())
    results.append(a + b)
print("\n".join(map(str, results)))

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(a + b)
# 8370 개선시키기
n1, k1, n2, k2 = map(int, input().split())
total_score = n1 * k1 + n2 * k2
print(total_score)

# 8370
n1, k1, n2, k2 = map(int, input().split())
print(n1 * k1 + n2 * k2)

# 7891 개선시키기

n = int(input())
results = []
for _ in range(n):
    a, b = map(int, input().split())
    results.append(a + b)
print("\n".join(map(str, results)))

# 7891
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(a + b)

# 6840 list로 sort한 다음 중간값을 출력하게끔
a = int(input())
b = int(input())
c = int(input())
dishs = [a, b, c]
dishs.sort()
print(dishs[1])
# 6840
a = int(input())
b = int(input())
c = int(input())
dishs = {a, b, c}
for dish in dishs:
    if max(dishs) > dish > min(dishs):
        print(dish)
# 5522 개선하기
total = 0
for i in range(5):
    n = int(input())
    total += n
print(total)

# 5522
sum = 0
for i in range(5):
    n = int(input())
    sum += n
print(sum)


# 5339
print(
    r'''     /~\
    ( oo|
    _\=/_
   /  _  \
  //|/.\|\\
 ||  \ /  ||
============
|          |
|          |
|          |'''
)


# 5338
# print(
#            _.-;;-._
# '-..-'|   ||   |
# '-..-'|_.-;;-._|
# '-..-'|   ||   |
# '-..-'|_.-''-._|
# )

#5337
print(r'''.  .   .
|  | _ | _. _ ._ _  _
|/\|(/.|(_.(_)[ | )(/.
''')

# 4999 개선코드
def compare_strings(a: str, b: str) -> str:
    #두 문자열의 길이를 비교하여 'go' 또는 'no'를 반환합니다.
    if len(a) >= len(b):
        return "go"
    else:
        return "no"


# 사용자에게 입력 안내 메시지 제공
a = input("첫 번째 문자열을 입력하세요: ").strip()
b = input("두 번째 문자열을 입력하세요: ").strip()

# 빈 입력이 있는지 확인
if not a or not b:
    print("입력이 유효하지 않습니다. 문자열을 입력해 주세요.")
else:
    # 비교 함수 호출 및 결과 출력
    result = compare_strings(a, b)
    print(result)


# 4999
a = input()
b = input()
if len(a) >= len(b):
    print("go")
else:
    print("no")

# 3733 개선하고자 한다 표준 입력 
import sys

# 개행되는 입력을 한줄씩 전부다 리스트 문자열 list str 로 처리한 뒤 저장한다.
lines = sys.stdin.readlines()
print(lines)
for line in lines:
    # strip()이 필요없다. split()하면서 공백이 지워짐
    n, s = map(int, line.split())
    print(n, s)
    print(s // (n + 1))

# 3733 #sys.stdin.readlines()는 여러 줄 표준 입력받고 처리하는 방법에 대한 문제. 문제 속 수학문제를 푸는 건 어렵지 않지만, 표준입력방법과 그 처리에 대한 공부를 하게 되는 문제다.
import sys

lines = sys.stdin.readlines()

for line in lines:
    # 나타났던 대표적인 오류 지금은 고쳤지만 'builtin_function_or_method' object is not iterable
    # map 이라던지 함수만 있고 괄호가 닫혀있지 않다던지하면 생기는 오류임
    n, s = map(int, line.strip().split())
    print(s // (n + 1))


# 2393 raw의 r을 붙여도 됨. 문제에 함정이 있었구만 이스케이프 역슬래시 역슬래시 역슬래시 역슬래시
print(
    r'''  ___  ___  ___
  | |__| |__| |
  |           |
   \_________/
    \_______/
     |     |
     |     |
     |     |
     |     |
     |_____|
  __/       \__
 /             \
/_______________\
'''
)
# \<==이거 때문에 문제가 생기는 거였음 \ 이스케이프 문자


# 2393 문제에 함정이 있었구만 이스케이프 역슬래시 역슬래시 역슬래시 역슬래시
print(
   '''  ___  ___  ___
  | |__| |__| |
  |           |
   \_________/
    \_______/
     |     |
     |     |
     |     |
     |     |
     |_____|
  __/       \__
 /             \\
/_______________\\
'''
)
# \<==이거 때문에 문제가 생기는 거였음 \ 이스케이프 문자


# 2393
print("  ___  ___  ___")
print("  | |__| |__| |")
print("  |           |")
print("   \_________/")
print("    \_______/")
print("     |     |")
print("     |     |")
print("     |     |")
print("     |     |")
print("     |_____|")
print("  __/       \__")
print(" /             \\")
print("/_______________\\")


#1436
n=int(input())


# 2839 흑백요리사 챗지피티의 첨삭이 시작된다 같은 브루트포스라도 단순 반복문으로 구현하지 않고 수학적인 해법을 먼저 생각하는 사고방식
# 정수론, 방정식, 연립방정식, 부정방정식을 다양한 각도로 생각하게끔 하네.
n = int(input())
min_boxes = -1

# range(시작,끝,단계(역순인지 두단계 뛸지인지))
for y in range(n // 5, -1, -1):
    reminder = n - 5 * y
    if reminder % 3 == 0:
        x = reminder // 3
        min_boxes = x + y
        break

print(min_boxes)


# 2839 보류 안성재=>코드가 이븐하게 익지 않았네요. 리스트는 왜 들어갔져?
# 나폴리 마피아: ????

n = int(input())
boxes = []
for x in range(5000 // 3 + 1):
    for y in range(5000 // 5 + 1):
        if n == 3 * x + 5 * y:
            boxes += [x + y]
if boxes == []:
    print(-1)
else:
    print(min(boxes))
    # print(boxes)
# print(x + y)


# 10988 반복문으로 개선하기 긴 문자열에선 오히려 효율적=>예전에 풀었던 문제인데도 기억이 안났다. 역시 첨삭해준 코드는 내것이 아니다. 내걸로 만들기 위한 작업은 직접 쳐보는 것이다.
text = input()
is_palindrome = 1
for i in range(len(text) // 2):
    if text[i] != text[-(i + 1)]:
        is_palindrome = 0
        break
print(is_palindrome)

# 10988 1259 연습
# 10989 연습
text = input()
is_palindrome = True
for i in range(len(text)//2):
    if text[i]!=text[len(text)-i-1]:
        is_palindrome=False
        break
print(is_palindrome)
 
# 1259 연습
while True:
    n =input().split()
    if n=='0':
        break
    
    is_palindrome=True:
    for i in range(len(n)//2):
        if n[i]!=n[len(n)-i-1]:
            is_palindrome=False
    
    if is_palindrome:
        print('yes')
    else:
        print('no')


# 1259 개선 리스트 안 쓰기
while True:
    n = input().strip()
    if n == "0":
        break

    is_palindrome = True
    length = len(n)

    for i in range(length // 2):
        if n[i] != n[length - i - 1]:
            is_palindrome = False
            break

    if is_palindrome:
        print("yes")
    else:
        print("no")


# 1259 개선개선개선!!
while True:
    n = input().strip()
    if n == "0":
        break

    if n == n[::-1]:
        print("yes")
    else:
        print("no")


# 1259
while True:
    n = input()
    reverse_n = []

    if int(n) == 0:
        break
    elif n == n[::-1]:
        print("yes")
        # if n[i] != n[-i - 1]:
    else:
        print("no")


# 31403 다시 재개선 하기
a = input()
b = input()
c = input()
print(int(a) + int(b) - int(c))
# 아? 이거 이렇게 바로 하면 되는거였네;;;

# d = a + b 이렇게 하지말고
# print(int(d) - int(c)) 이렇게 하지 말고

print(int(a + b) - int(c))
# 31403 개선하기
a = input().strip()
b = input().strip()
c = input().strip()

num_result = int(a) + int(b) - int(c)
print(num_result)

concat_result = int(a + b) - int(c)
print(concat_result)


# 31403 다시 재개선 하기
a = input()
b = input()
c = input()
print(int(a) + int(b) - int(c))

d = a + b
print(int(d) - int(c))


# 19532 이걸 개선시키기 헉 첨삭 받음
a, b, c, d, e, f = map(int, input().split())
D = a * e - b * d

print(
    int((e * c - b * f) // D),
    int(((-d) * c + a * f) // D),
)

# 19532 첨삭받기 챗지피티가 오히려 더 복잡하게 푸는듯? 첫번째 식을 y= 블라블라 식으로 고친 다음 두번째 식에 대입을 한다는 아이디어인데...
# 시간복잡도가 O(n)이라서 성능면에선 더 효율적인 코드이다.

a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    if b != 0:
        # 첫 번째 방정식을 이용하여 y를 구함
        y = (c - a * x) / b
        if y.is_integer():  # y가 정수일 경우에만
            y = int(y)  # 정수로 변환
            if d * x + e * y == f:  # 두 번째 방정식도 만족하는지 확인
                print(x, y)
                break
    else:
        # b가 0인 경우: 첫 번째 방정식에서 a * x == c로 x 값 결정
        if a != 0 and c % a == 0:
            x = c // a
            # 구한 x 값으로 y 값을 두 번째 방정식을 통해 확인
            if e != 0:
                y = (f - d * x) / e
                if y.is_integer():  # y가 정수일 경우에만
                    y = int(y)  # 정수로 변환
                    print(x, y)
                    break
            elif d * x == f:  # e가 0이면서 두 번째 방정식을 만족할 경우
                print(x, 0)
                break


# 19532 재시도 브루트포스 알고리즘인걸 깜빡했다;;;행렬식을 왜 쓰냐 허허허;;;==>맞췄다. ㅋㅋㅋㅋㅋㅋ야후~!
# 위에 언급한대로 시간복잡도가 O(n^2)인 풀이이긴 하다
a, b, c, d, e, f = map(int, input().split())
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)

# 19532 보류 안성재

a, b, c, d, e, f = map(int, input().split())
determinant = 1 / (a * e - b * d)

print(
    int(determinant * (e * c - b * f)),
    int(determinant * ((-d) * c + a * f)),
)
# 2231 더 개선시키기
def digits_sum(x):
    # return sum(int(digit) for digit in str(x)) 대신 수학적 계산으로 할 수 있다
    # 왠만하면 수학적 방법으로 해결가능하니 먼저 떠올려보자.
    digit_sum = 0
    while x > 0:
        digit_sum += x % 10  # 일의 자리수를 더한다
        x //= 10  # 일의 자리수를 없애고 자리수를 하나 줄인다
    return digit_sum


n = int(input())
for i in range(1, n):
    if i + digits_sum(i) == n:
        print(i)
        # 아..어차피 최솟값이니 이렇게 처리해도 되겠네;;
        break
else:  # for-else 구문
    print(0)

# 2231 개선시키기
def digits_sum(x):
    return sum(int(digit) for digit in str(x))


n = int(input())
generator = 0
for i in range(1, n):
    if i + digits_sum(i) == n:
        generator = i
        # 아..어차피 최솟값이니 이렇게 처리해도 되겠네;;
        break
print(generator)


# 2231

# 우선 입력된 수의 각 자리수를 더하는 것부터 구현하자
def digits_sum(x):
    digit_sum = 0
    for k in range(len(str(x))):
        digit_sum += int(str(x)[k])
    return digit_sum


n = int(input())
#리스트부터 만들어서 해결하려는 사고방식이 생겼네. 수학적해결 가능성이 보이면 그걸 우선 사고하자(예: 자리수 모두 합하기)
generator_numbers = []

for i in range(1, n):
    if int(n) == i + digits_sum(i):
        generator_numbers += [i]

if generator_numbers:
    print(int(min(generator_numbers)))
else:
    # generator_numbers=[]일때 0출력
    print(0)



# if plasticbag_3 * 3 + plasticbag_5 * 5 != n:
# print(-1)
# else:
result = plasticbag_3 + plasticbag_5
print(result)




# 2163 개선하기 가독성강화
n, m = map(int, input().split())

horizontal_cuts = n - 1
vertical_cuts = (m - 1) * n

result = horizontal_cuts + vertical_cuts
print(result)

# 2163
n, m = map(int, input().split())
print((n - 1) + ((m - 1) * n))

# 2163 규칙찾기
# 300 300

# (300-1) + (300-1)*300

# 1 1
# 0=  (1-1) + (1-1)*1

# 1 2
# 1 = 1-1 + 2-1*1

# 1 3
# 1 1 = 1-1 + 3-1 * 1

# 1 4
# 1 1 1

# 1 5
# 1 1 1 1 1-1 5-1*1

# 2 1
# 1

# 2 2
# 1 1 1 (2-1) + (2-1)*2

# 2 3
# 1 1 1 1 1 2-1 + (3-1)*2
# n-1 + (m-1)*n
# 2 4
# 1 1 1 1 1 1 1

# 3 1
# 1 1

# 3 2
# 1 1 1 1 1

# 3 3
# 1 1 1 1 1 1 1 1  (3-1) + (3-1)*3

# 1 5
# 1 1 1 1

# 2 5
# 1 1 1 1 1 1 1 1 1

# 요까지가 2163 규칙찾는 과정

# 2558
a = int(input())
b = int(input())
print(a + b)
# 2941
alphabets = {c=, c-, dz=, d-, lj, nj, s=, z=}

croatia_word = "ljes=njak"
n = 0
for alphabet in alphabets:
    if alphabet in croatia_word:
        n += 1

print(n)


# 11023
print(sum(map(int, input().split())))

# 32384
print(int(input()) * "LoveisKoreaUniversity ")


# 206307 함수화 예외처리 추가하기
 
def minutes_since_9am(h, m):
    # 입력값이 유효한지 체크
    if not (0 <= h < 24 and 0 <= m < 60):
        raise ValueError("Invalid time input")

    # 9시 이전 입력에 대한 처리
    if h < 9:
        print("The time is before 9:00 AM.")
        return

    return (h - 9) * 60 + m

# 사용자 입력
h, m = map(int, input("Enter time (HH MM): ").split())
try:
    result = minutes_since_9am(h, m)
    if result is not None:
        print(f"Minutes since 9:00 AM: {result}")
except ValueError as e:
    print(e)


# 26307
h, m = map(int, input().split())
print((h - 9) * 60 + m)


# 28701 개선하기 빈복문 없애서 O(1)을 추구함
n = int(input())
x = n * (n + 1) // 2
y = x**2

print(x)
print(x**2)
print(y)

# 28701
n = int(input())
(x, y) = (0, 0)
for i in range(1, n + 1):
    x += i
    y += i**3
print(x)
print(x**2)
print(y)

# 15000 개선하기!
# str 필요없음
# int(input())은 가치가 있지만 str(input())은 역전 앞이랑 마찬가지임
print(input()).upper()

# 15000
print(str(input()).upper())


# 25372 개선하기
n = int(input())
for _ in range(n):
    password = input()
    # chained comparison
    if 6 <= len(password) <= 9:
        print("yes")
    else:
        print("no")
# 25372
n = int(input())
for _ in range(n):
    password_9 = input()
    if len(password_9) >= 6 and len(password_9) <= 9:
        print("yes")
    else:
        print("no")


# 27433 챗지피티가 짠 프로그램
# 재귀호출
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {n} is: {factorial(n)}")


# 27433 개선하고 실수했던 거 복기
n = int(input())
fact = 1
if n == 0:
    print(1)
else:
    # range를 빼먹고서는 계속 이상한값이 나와서 이상하게 생각했는데 팩토리얼 1문제를 보고 다시 떠올림
    # 근데 range를 뺐는데도 왜 실행되었을까????!!!
    # =>range를 빼면 (2, n+1) 파이썬에서 튜플형 자료다.
    # 따라서 i가 2와 n+1을 순차적으로 순회함.
    for i in range(2, n + 1):
        #        fact = i * fact
        fact *= i
    print(fact)

# 27433
n = int(input())
fact = 1
if n == 0:
    print(1)
else:
    for i in range(2, n + 1):
        fact = i * fact
    print(fact)

# 2338
a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)

# 5341 개선하기
def sum_of_integers(n):
    return n * (n + 1) // 2


while (n := int(input())) != 0:
    print(sum_of_integers(n))
# 5341
while True:
    n = int(input())
    if n == 0:
        break
    print(n * (n + 1) // 2)
# 5073 개선시키기
while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break
    if a + b <= c or b + c <= a or c + a <= b:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif len({a, b, c}) == 2:
        print("Isosceles")
    else:
        print("Scalene")

# 5073 
while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break
    # isTrigangle 이런 것도 필요 없지 싶은데 음...뭔가 틀렸었다 홀린듯
    isTriangle = a + b > c and b + c > a and c + a > b
    # 굳이 이렇게 안해도 되지 않나 한 번밖에 안 쓰는데 ㅎㅎ;;
    set_Isosceles = {a, b, c}
    # not isTriagle
    if isTriangle is False:
        print("Invalid")
    elif a == b == c and a * b * c != 0:
        print("Equilateral")
    #여기에 set_Isosceles 대신 {a,b,c}라고 간단히 해도 된다는 거지.
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
