def solution(arr):
    n=len(arr)
    sum=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]==arr[j][i]:
                sum+=1
    if sum==pow(n,2):
        return 1
    return 0
    