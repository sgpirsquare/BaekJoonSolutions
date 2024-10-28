n, k = map(int, input().split())
div = []
for i in range(1, n + 1):
    if n % i == 0:
        div += [i]

print(0 if len(div) < k else div[k-1])