n = int(input())
for i in range(n):
    repeat_count, text = input().split()
    arr = []
    for j in range(len(text)):
        arr.append(int(repeat_count) * text[j])
    print(*arr, sep="")