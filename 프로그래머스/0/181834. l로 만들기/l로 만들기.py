def solution(myString):
    answer = ''
    myString=list(myString)
    for i in range(len(myString)):
        if ord(myString[i])<ord('l'):
            myString[i]='l'
    answer=''.join(i for i in myString)
    return answer