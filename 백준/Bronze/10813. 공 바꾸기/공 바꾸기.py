box_num, ball_try = map(int, input().split())
boxes = [i + 1 for i in range(box_num)]
for _ in range(ball_try):
    first, second = map(int, input().split())
    temp = boxes[second - 1]
    boxes[second - 1] = boxes[first - 1]
    boxes[first - 1] = temp
print(*boxes)