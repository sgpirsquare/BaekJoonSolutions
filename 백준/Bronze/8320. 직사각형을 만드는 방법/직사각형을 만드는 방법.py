N = int(input())
result = 0
for divisor in range(1, N + 1):
    for i in range(1, N // divisor + 1):
        if divisor <= i:
            result += 1
print(result)