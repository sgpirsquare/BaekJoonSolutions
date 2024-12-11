def factorial(n):
    fact = 1
    for i in range(n, 1, -1):
        fact *= i
    return fact

N = int(input())

if N == 0:
    print(1)
else:
    print(factorial(N))