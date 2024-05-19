import pandas as pd
from pymongo import MongoClient
from datetime import datetime

# CSV 파일 경로
csv_file = 'Realestate_data.csv'

# MongoDB 연결 정보
client = MongoClient('mongodb://localhost:27017/')
db = client['Project']
collection = db['real_estate']

# CSV 파일 읽기 (지번구분 열, 본번 열, 부번 열, 층 열의 NaN 값을 0으로 대체)
# 데이터프레임을 읽을 때 DtypeWarning 방지를 위해 dtype 지정
data = pd.read_csv(csv_file, dtype={'지번구분': str, '본번': str, '부번': str})
data['지번구분'] = data['지번구분'].fillna(0).astype(int)
data['본번'] = pd.to_numeric(data['본번'], errors='coerce').fillna(0).astype(int)
data['부번'] = pd.to_numeric(data['부번'], errors='coerce').fillna(0).astype(int)
data['층'] = pd.to_numeric(data['층'], errors='coerce').fillna(0).astype(int)
data['건축년도'] = pd.to_numeric(data['건축년도'], errors='coerce').fillna(0).astype(int)

# 취소일 열의 NaN 값을 None으로 대체
data['취소일'] = pd.to_datetime(data['취소일'], errors='coerce')

# 데이터를 JSON 형식으로 변환하여 MongoDB에 삽입
for _, row in data.iterrows():
    record = {
        '접수연도': int(row['접수연도']),
        '주소': {
            '자치구코드': int(row['자치구코드']),
            '자치구명': row['자치구명'],
            '법정동코드': int(row['법정동코드']),
            '법정동명': row['법정동명'],
            '지번구분': int(row['지번구분']),
            '지번구분명': row['지번구분명'],
            '본번': int(row['본번']),
            '부번': int(row['부번']),
            '건물명': row['건물명']
        },
        '계약일': datetime.strptime(str(row['계약일']), '%Y%m%d'),
        '물건금액(만원)': int(row['물건금액(만원)']),
        '건물면적(㎡)': float(row['건물면적(㎡)']),
        '토지면적(㎡)': float(row['토지면적(㎡)']),
        '층': int(row['층']),
        '권리구분': row['권리구분'],
        '취소일': row['취소일'] if not pd.isnull(row['취소일']) else None,
        '건축년도': int(row['건축년도']),
        '건물용도': row['건물용도'],
        '신고구분': row['신고구분'],
        '신고한_개업공인중개사 시군구명': row['신고한 개업공인중개사 시군구명']
    }
    collection.insert_one(record)

print("Data inserted successfully.")