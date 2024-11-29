x_0, N = map(int, input().split())
for _ in range(N):
    if x_0 % 2 == 0:
        x_0 = int(x_0 / 2) ^ 6
    else:
        x_0 = int(x_0 * 2) ^ 6

print(x_0)