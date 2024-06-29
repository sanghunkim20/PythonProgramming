n = 3

def solution(n):
    answer = ''

    if n % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    
    return answer

print(solution(n))