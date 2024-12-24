def solution(myString):
    answer=list(myString)
    for i in range(len(answer)):
        if answer[i]=='a' or answer[i]=='A':
            answer[i]='A'
        else:
            answer[i]=answer[i].lower()
            
    answer = ''.join(answer)
    return answer