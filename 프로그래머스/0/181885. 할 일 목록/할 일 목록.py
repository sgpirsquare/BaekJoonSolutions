def solution(todo_list, finished):
    answer = []
    for i in range(len(finished)):
        if finished[i] is False:
            answer.append(todo_list[i])
        else:
            pass
    return answer