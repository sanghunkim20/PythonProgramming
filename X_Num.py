def solution(x, n):
    answer = []
    num = 0
    for i in range(n):
        num += x
        answer.append(num)

    return answer
x = -12
n = 5
print(solution(x, n))