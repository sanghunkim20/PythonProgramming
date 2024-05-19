import pandas as pd
from pymongo import MongoClient
from datetime import datetime

# CSV 파일 경로
csv_file = 'subway_data.csv'

# MongoDB 연결 정보
client = MongoClient('mongodb://localhost:27017/')
db = client['Project']
collection = db['subway']

# CSV 파일 읽기
data = pd.read_csv(csv_file)

# 데이터를 JSON 형식으로 변환하여 MongoDB에 삽입
for _, row in data.iterrows():
    record = {
        'date': datetime.strptime(str(row['사용일자']), '%Y%m%d'),
        'location': {
            'line': row['노선명'],
            'station': row['역명']
        },
        'boarding': row['승차총승객수'],
        'alighting': row['하차총승객수'],
        'registration_date': datetime.strptime(str(row['등록일자']), '%Y%m%d')
    }
    collection.insert_one(record)

print("Data inserted successfully.")
