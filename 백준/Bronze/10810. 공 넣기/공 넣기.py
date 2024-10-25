box_num, ball_try = map(int, input().split())

boxes = [0 for _ in range(box_num)]
for _ in range(ball_try):
    box_start, box_end, ball_number = map(int, input().split())
    for i in range(box_start - 1, box_end):
        boxes[i] = ball_number

print(*boxes)