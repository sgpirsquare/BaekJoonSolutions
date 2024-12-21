def solution(my_string):
    
    answer = ''
    for character in my_string:
        if character=='a' or character=='e' or character=='i' or character=='o' or character=='u':
            pass
        else:
            answer+=character
        
    return answer