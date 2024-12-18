N = int(input())
sum = []
for _ in range(N):
    scores = list(map(int, input().split()))
    score_of_run = sorted(scores[:2])
    score_of_trick = sorted(scores[2:])
    sum.append(score_of_run[1] + score_of_trick[-1] + score_of_trick[-2])
sum.sort()
print(sum[-1])