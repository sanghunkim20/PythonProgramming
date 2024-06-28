n = 118372

def solution(n):
    n = int(n)
    temp = map(str, str(n)) # n을 문자열로 변환 후 각 자리수를 temp 리스트에 저장
    return int(''.join(sorted(temp, reverse=True))) # temp 리스트를 내림차순으로 정렬하여 join한 후 정수형으로 변환하여 반환

print(solution(n))
