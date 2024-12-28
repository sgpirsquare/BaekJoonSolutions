N = int(input())
for _ in range(N):
    p, t = map(int, input().split())
    print(p - t // 7 + t // 4)