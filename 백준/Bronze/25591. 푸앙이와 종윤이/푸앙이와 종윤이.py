N1, N2 = map(int, input().split())
a = 100 - N1
b = 100 - N2
c = 100 - a - b
d = a * b
q = d // 100
r = d % 100
print(a, b, c, d, q, r)
print(c + q, r)
