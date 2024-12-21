def solution(hp):    
    ant_5=hp//5
    ant_3=(hp- (hp//5) *5)//3
    ant_1=hp- ant_5 * 5 - ant_3 *3
    answer =ant_5 + ant_3 + ant_1
    return answer