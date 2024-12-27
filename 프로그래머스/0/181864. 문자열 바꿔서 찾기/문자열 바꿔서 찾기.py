def solution(myString, pat):
    myString=list(myString)
    for i in range(len(myString)):
        if myString[i]=='A':
            myString[i]='B'
        elif myString[i]=='B':
            myString[i]='A'
    myString=''.join(i for i in myString)
    if pat in myString:
        return 1
    else:
        return 0