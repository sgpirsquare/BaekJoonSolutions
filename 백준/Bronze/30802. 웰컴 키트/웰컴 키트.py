N = int(input())
S, M, L, XL, XXL, XXXL = map(int, input().split())
T_shirts = [S, M, L, XL, XXL, XXXL]
T, P = map(int, input().split())
result = 0
for shirts in T_shirts:

    result += (shirts - 1) // T + 1


print(result)

print(N // P, N % P)