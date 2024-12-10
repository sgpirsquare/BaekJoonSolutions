frequency = int(input())
for _ in range(frequency):
    room_number = []
    h, w, n = map(int, input().split())
    for j in range(1, w + 1):
        for i in range(1, h + 1):
            room_number.append(i * 100 + j)
    print(room_number[n - 1])