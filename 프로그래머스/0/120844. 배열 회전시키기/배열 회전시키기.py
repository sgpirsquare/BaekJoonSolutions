def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer.append(numbers[len(numbers) - 1])
        answer += numbers[:-1]
    if direction == "left":

        answer = numbers[1:]
        answer.append(numbers[0])

    return answer
