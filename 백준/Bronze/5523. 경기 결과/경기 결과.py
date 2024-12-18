from sys import stdin

score_A, score_B = 0, 0
for _ in range(int(stdin.readline())):
    A, B = map(int, stdin.readline().split())
    if A > B:
        score_A += 1
    elif A < B:
        score_B += 1
    else:
        pass
print(score_A, score_B)