def solution(n, control):
    for wasd in control:
        if wasd=='w':
            n+=1
        elif wasd=='s':
            n-=1
        elif wasd=='d':
            n+=10
        elif wasd=='a':
            n-=10
                                
    answer = n
    return n