def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


N = int(input())

i = 1
while factorial(N) % 10**i == 0:
    i += 1
print(i - 1)
