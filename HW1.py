import random

# 리스트 생성 함수
def create_list(n):
    # 리스트 선언
    k_score = []
    e_score = []
    m_score = []
    student_num = []

    # 랜덤으로 점수 생성
    for i in range(n):
        student_num.append(i+1)
        k_score.append(random.randint(1, 100))
        e_score.append(random.randint(1, 100))
        m_score.append(random.randint(1, 100))

    # 학생 번호, 국어, 영어, 수학 리스트 반환
    return student_num, k_score, e_score, m_score

# 개인 성적 조회 함수 (1번)
def num1(student_num, k_score, e_score, m_score): 
    # 학생 번호 입력
    num = int(input("학생 번호를 입력하시오.: "))
    
    # 학생 번호가 리스트에 있는지 확인 후 출력
    if num in student_num:
        print("{}번 학생의 국어 성적은 {}점, 영어 성적은 {}점, 수학 성적은 {}점입니다.".format(num, k_score[num-1], e_score[num-1], m_score[num-1]))
    else:
        print("해당 학생 번호가 없습니다.")

# 개인 총점/평균 조회 함수 (2번)
def num2(student_num, k_score, e_score, m_score):
    # 학생 번호 입력
    num = int(input("학생 번호를 입력하시오.: "))

    # 학생 번호가 리스트에 있는지 확인 후 출력
    if num in student_num:
        sum = k_score[num-1] + e_score[num-1] + m_score[num-1]
        avg = sum / 3
        print("{}번 학생의 총점은 {}점, 평균은 {:.2f}점입니다.".format(num, sum, avg))
    else:
        print("해당 학생 번호가 없습니다.")

# 과목별 총점/평균 조회 함수 (3번)
def num3(k_score, e_score, m_score):
    # 과목 선택
    subject = int(input("과목을 선택하시오. (1: 국어, 2: 영어, 3: 수학): "))

    # 과목별 총점/평균 계산
    if subject == 1:
        sum = 0 
        for i in k_score:
            sum += i
        avg = sum / len(k_score)
        print("국어 과목의 총점은 {}점, 평균은 {:.2f}점입니다.".format(sum, avg))
    elif subject == 2:
        sum = 0 
        for i in e_score:
            sum += i
        avg = sum / len(e_score)
        print("영어 과목의 총점은 {}점, 평균은 {:.2f}점입니다.".format(sum, avg))
    elif subject == 3:
        sum = 0
        for i in m_score:
            sum += i
        avg = sum / len(m_score)
        print("수학 과목의 총점은 {}점, 평균은 {:.2f}점입니다.".format(sum, avg))
    else:
        print("해당 과목이 없습니다.")

# 전체 총점/평균 조회 함수 (4번)
def num4(k_score, e_score, m_score):
    # 전체 총점/평균 계산
    sum = 0
    for i in k_score:
        sum += i
    for i in e_score:
        sum += i
    for i in m_score:
        sum += i
    avg = sum / (len(k_score) + len(e_score) + len(m_score))

    print("전체 총점은 {}점, 평균은 {:.2f}점입니다.".format(sum, avg))

# 본인 점수 등록 함수 (5번)
def num5(student_num, k_score, e_score, m_score):
    student_num.append(len(student_num)+1)
    k_score.append(int(input("국어 점수를 입력하시오.: ")))
    e_score.append(int(input("영어 점수를 입력하시오.: ")))
    m_score.append(int(input("수학 점수를 입력하시오.: ")))

# 본인 과목별 등수 확인 함수 (6번)
def num6(k_score, e_score, m_score):
    # 점수가 30개 이상이면 본인 점수가 등록된 것 (맨 마지막 값이 본인 점수로 가정)
    if len(k_score) > 30:
        # 과목 번호 입력
        subject = int(input("과목을 선택하시오. (1: 국어, 2: 영어, 3: 수학): "))
        rank = 1
        # 과목별 등수 생성
        if subject == 1:
            for i in range(len(k_score)-1):
                if k_score[i] > k_score[len(k_score)-1]:
                    rank += 1
            print("국어 과목의 등수는 {}등입니다.".format(rank))
        elif subject == 2:
            for i in range(len(e_score)-1):
                if e_score[i] > e_score[len(e_score)-1]:
                    rank += 1
            print("영어 과목의 등수는 {}등입니다.".format(rank))
        elif subject == 3:
            for i in range(len(m_score)-1):
                if m_score[i] > m_score[len(m_score)-1]:
                    rank += 1
            print("수학 과목의 등수는 {}등입니다.".format(rank))
    # 점수가 30개 미만이면 본인 점수가 등록되지 않은 것 (맨 마지막 값이 본인 점수로 가정)
    else:
        print("본인 점수가 등록되지 않았습니다.")

# 본인 전체 등수 확인 함수 (7번)
def num7(student_num, k_score, e_score, m_score):
    # 점수가 30개 이상이면 본인 점수가 등록된 것 (맨 마지막 값이 본인 점수로 가정)
    if len(k_score) > 30:
        rank = 1
        # 전체 등수 생성
        for i in range(len(k_score)):
            if k_score[i] + e_score[i] + m_score[i] > k_score[len(k_score)-1] + e_score[len(e_score)-1] + m_score[len(m_score)-1]:
                rank += 1
        print("전체 등수는 {}명 중 {}등입니다.".format(len(student_num), rank))
     # 점수가 30개 미만이면 본인 점수가 등록되지 않은 것 (맨 마지막 값이 본인 점수로 가정)
    else:
        print("본인 점수가 등록되지 않았습니다.")

# 전체학생 성적 출력 함수 (8번)
def num8(student_num, k_score, e_score, m_score):
    student_list = [[row[col]for row in [student_num, k_score, e_score, m_score]] for col in range(len(student_num))]

    for row in student_list:
        print(row)

        
n = 30
t= create_list(n)
menu = 1

while(menu != 0):
    print("-------------------------")
    print("-------------------------")
    print("1. 개인 성적 조회")
    print("2. 개인 총점/평균 조회")
    print("3. 과목별 총점/평균 조회")
    print("4. 전체 총점/평균 조회")
    print("5. 본인 점수 등록")
    print("6. 본인 과목별 등수 확인")
    print("7. 본인 전체 등수 확인")
    print("8. 전체 학생 성적 출력")
    print("-------------------------")
    print("0. 종료")
    print("-------------------------")

    menu = int(input("메뉴를 선택하시오.: "))

    if menu == 1:
        num1(t[0], t[1], t[2], t[3])
    elif menu == 2:
        num2(t[0], t[1], t[2], t[3])
    elif menu == 3:
        num3(t[1], t[2], t[3])
    elif menu == 4:
        num4(t[1], t[2], t[3])
    elif menu == 5:
        num5(t[0], t[1], t[2], t[3])
    elif menu == 6:
        num6(t[1], t[2], t[3])
    elif menu == 7:
        num7(t[0], t[1], t[2], t[3])
    elif menu == 8:
        num8(t[0], t[1], t[2], t[3])