n = 12345

def solution(n):
    answer = [] # 빈 리스트 answer 생성
    temp = [] # 빈 리스트 temp 생성
    n = str(n) # 정수형을 문자열로 변환

    # tmep 리스트에 n의 각 자리수를 정수형으로 변환하여 추가
    for i in n:
        temp.append(int(i))
    
    # answer 리스트에 temp 리스트의 값을 pop하여 추가 (끝 값부터 값을 넣음)
    for i in range(len(temp)):
        answer.append(temp.pop())

    return answer

print(solution(n)) # 출력
    
