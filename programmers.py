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
