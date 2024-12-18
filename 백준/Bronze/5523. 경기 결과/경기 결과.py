N = int(input())
score_A, score_B = 0, 0
for _ in range(N):
    A, B = map(int, input().split())
    if A > B:
        score_A += 1
    elif A < B:
        score_B += 1
    else:
        pass
print(score_A, score_B)