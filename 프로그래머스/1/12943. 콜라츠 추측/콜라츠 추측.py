def solution(num):
    count = 0
    while not (num == 1):
        if num % 2 == 0:
            num = num // 2
        elif num % 2 == 1:
            num = 3 * num + 1
        elif num == 1:
            break
        count += 1
    if count >= 500:
        return -1
    return count
