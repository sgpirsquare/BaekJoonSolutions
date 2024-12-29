def solution(absolutes, signs):
    answer = 0
    for TorF in range(len(signs)):
        if signs[TorF]:
            answer += absolutes[TorF]
        else:
            answer -= absolutes[TorF]
    
    return answer
