a, b, c, d, e, f = map(int, input().split())
D = a * e - b * d

print(
    int((e * c - b * f) // D),
    int(((-d) * c + a * f) // D),
)