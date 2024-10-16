a, b = map(int, input().split())
c = int(input())

print((a + (b+c)//60) % 24, (b + c) % 60)

# 아래처럼 처리하는게 더 pythonic하다고 한다
# import sys

# p, t = sys.stdin.read().splitlines()
# print(f"p: {p}, t: {t}")

# 이것도 좋네. 문제 의도에 맞게 조건문을 쓰기도 했고
# h, m = map(int, input().split())
# c = int(input())

# if m + c >= 60:
#     h += (m + c) // 60
#     m = (m + c) % 60
#     if h >= 23:
#         h %= 24
# else:
# 복합 연산자 m에 c를 +하고 =할당한다 + => = 순서대로. 영미권에서도 마찬가지로 접근하네
#     m += c

# print(h, m)
