s = "Ppoooyy"

def solution(s):
    answer = True # 초기 answer 값을 True로 초기화
    s = s.lower() # 문자열 s를 소문자로 변환
    p_cnt = 0 # p의 개수를 저장할 변수
    y_cnt = 0 # y의 개수를 저장할 변수
    for i in s: # 문자열 s를 위한 반복문
        if i == 'p': # i가 p일 때
            p_cnt += 1 # p_cnt에 1을 더함
        elif i == 'y': # i가 y일 때
            y_cnt += 1 # y_cnt에 1을 더함
    if p_cnt == y_cnt: # p_cnt와 y_cnt가 같을 때
        answer = True # answer를 True로 변경
    else: # 그렇지 않을 때
        answer = False # answer를 False로 변경
    return answer

print(solution(s)) # 출력
    
