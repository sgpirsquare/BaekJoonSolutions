arr = []
n, a = map(int, input().split())
numbers = list(map(int, input().split()))
for i in numbers:
    if a > i:
        arr.append(i)
print(*arr)