import os
import pandas as pd

# 현재 디렉토리의 파일 목록 가져오기
dirpath = './Subway/'
files = os.listdir(dirpath)

# 각 CSV 파일에 인덱스 칼럼을 추가하고 덮어쓰기
for file in files:
    fpath = os.path.join(dirpath, file)  # 파일 경로 생성
    try:
        # CSV 파일 읽기
        data = pd.read_csv(fpath)

        # 인덱스 칼럼 추가
        data.insert(0, 'index', range(1, len(data) + 1))

        # 수정된 내용으로 CSV 파일 덮어쓰기
        data.to_csv(fpath, index=False)
        print(f"파일 '{file}'에 인덱스 칼럼이 추가되었습니다.")
    except Exception as e:
        print(f"파일 '{file}'을(를) 처리하는 데 문제가 발생했습니다: {e}")
