def solution(strArr):
    answer = []
    for text in strArr:
        if 'ad' not in text:
            answer.append(text)
    return answer