n = 987

def solution(n):
    n = str(n) # 정수형을 문자열로 변환
    answer = 0 # answer를 0으로 초기화
    for i in n:
        answer = answer + int(i)   # 문자열 n의 각 자리수를 정수형으로 변환하여 answer에 더함
    return answer

print(solution(n))