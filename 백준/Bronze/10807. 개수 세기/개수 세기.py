n = int(input())
m = map(int, input().split())
l = int(input())
cnt = 0
for i in m:
    if l == i:
        cnt += 1
print(cnt)