N = int(input())
for _ in range(N):
    cent = int(input())
    quarter = int(cent // 25)
    dime = int((cent - 25 * quarter) // 10)
    nickel = int((cent - 25 * quarter - 10 * dime) // 5)
    penny = int((cent - 25 * quarter - 10 * dime - 5 * nickel) // 1)
    print(quarter, dime, nickel, penny)