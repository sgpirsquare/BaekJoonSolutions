a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

f = a1 * n0 + a0
g = c * n0

if g - f >= 0 and c >= a1:
    print(1)
else:
    print(0)