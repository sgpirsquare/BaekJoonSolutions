def solution(n):
    answer = []
    for i in range(n):
        answer.append([0 for i in range(n)])
    for i in range(n):
        for j in range(n):
            if i == j:
                answer[i][j] = 1
    return answer
