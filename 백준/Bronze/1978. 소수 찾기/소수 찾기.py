N = int(input())
numlist = map(int, input().split())

primes = 0

for number in numlist:
    if number <= 1:
        pass
    else:
        for i in range(2, int((number**0.5) + 1)):
            if number % i == 0:
                break
        else:
            primes += 1

print(primes)