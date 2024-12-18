N = int(input())
for _ in range(N):
    scores = list(map(int, input().split()))
    scores.sort()
    if scores[1] - scores[3] >= 4 or scores[3] - scores[1] >= 4:
        print("KIN")
    else:
        print(sum(scores) - min(scores) - max(scores))