n, m = map(int, input().split())
cards = list(map(int, input().split()))
totals = []
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            totals.append(cards[i] + cards[j] + cards[k])
less_than_m = []
for total in totals:
    if m >= int(total):
        less_than_m += [total]
print(max(less_than_m))