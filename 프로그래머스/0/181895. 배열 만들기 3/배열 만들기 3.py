def solution(arr, intervals):
    answer = []
    for i in range(2):
        answer+=arr[intervals[i][0]:intervals[i][1]+1]
    return answer