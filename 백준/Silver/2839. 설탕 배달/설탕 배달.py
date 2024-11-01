n = int(input())
boxes = []
for x in range(5000 // 3 + 1):
    for y in range(5000 // 5 + 1):
        if n == 3 * x + 5 * y:
            boxes += [x + y]
if boxes == []:
    print(-1)
else:
    print(min(boxes))