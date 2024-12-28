def solution(s):
    count_p = 0
    count_y = 0
    for i in range(len(s)):
        if "p" == s[i].lower():
            count_p += 1
        if "y" == s[i].lower():
            count_y += 1
    if count_p == count_y:
        return True
    else:
        return False
