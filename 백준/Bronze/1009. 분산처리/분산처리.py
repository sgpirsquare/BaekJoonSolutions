N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    a = a % 10
    if a == 0:
        print(10)
    if a == 1 or a == 5 or a == 6:
        print(a)
    if a == 2 or a == 3 or a == 7 or a == 8:
        print((a ** ((b - 1) % 4 + 1)) % 10)
    if a == 4 or a == 9:
        print((a ** ((b - 1) % 2 + 1)) % 10)