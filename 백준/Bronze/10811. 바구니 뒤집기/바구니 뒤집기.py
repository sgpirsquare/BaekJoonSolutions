box_num, ball_try = map(int, input().split())
boxes = [i + 1 for i in range(box_num)]
for _ in range(ball_try):
    start, end = map(int, input().split())
    boxes[start - 1 : end] = boxes[start - 1 : end][::-1]
print(*boxes)