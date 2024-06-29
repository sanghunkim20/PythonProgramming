x = 13

def solution(x):
    answer = True
    str_x = str(x)
    num = 0
    for i in str_x:
        num += int(i)
    
    if x%num != 0:
        answer = False
    return answer

print(solution(x))
