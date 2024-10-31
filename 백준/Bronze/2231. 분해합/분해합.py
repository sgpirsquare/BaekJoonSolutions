def digits_sum(x):
    digit_sum = 0
    for k in range(len(str(x))):
        digit_sum += int(str(x)[k])
    return digit_sum


n = int(input())
generator_numbers = []

for i in range(1, n):
    if int(n) == i + digits_sum(i):
        generator_numbers += [i]

if generator_numbers:
    print(int(min(generator_numbers)))
else:
    print(0)