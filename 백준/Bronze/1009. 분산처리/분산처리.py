N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    a %= 10
    if a == 0:
        print(10)
    else:
        print(pow(a, b, 10))