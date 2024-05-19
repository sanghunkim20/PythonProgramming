import os
import pandas as pd

# 현재 디렉토리의 파일 목록 가져오기
dirpath = './Subway/'
files = os.listdir(dirpath)
print(files)
# 빈 데이터프레임 생성
raw = pd.DataFrame()

# 각 파일을 읽어와서 데이터프레임에 추가
for file in os.listdir(dirpath):
    fpath = './Subway/' + file  # 파일 경로
    print(fpath)
    temp = pd.read_csv(fpath)  # 파일의 인코딩을 cp949로 지정하여 읽기
    raw = pd.concat([raw, temp], ignore_index=False)  # 데이터프레임 병합

# 데이터프레임 출력
print(raw)

# csv 파일로 저장
raw.to_csv('subway_data.csv', index=False)
