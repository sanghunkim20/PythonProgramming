n = 3
def solution(n):
    answer = 0
    flag = 0
    cnt = 0
    while True:
        cnt += 1
        if cnt*cnt == n:
            flag = 1
            break
        if cnt > n:
            break
    if flag == 1:
        answer = (cnt+1)*(cnt+1)
    else:
        answer = -1
    return answer 

print(solution(n)) # 144