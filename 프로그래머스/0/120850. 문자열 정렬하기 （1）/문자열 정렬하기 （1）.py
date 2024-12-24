def solution(my_string):
    answer = []
    for character in my_string:
        if character.isdigit():
            answer.append(int(character))
    return list(sorted(answer))