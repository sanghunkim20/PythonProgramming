arr = [5,5]

def solution(arr):
    answer = 0
    cnt = 0
    for i in arr:
        cnt += 1
        answer += i
    return answer/cnt

print(solution(arr))
    
    