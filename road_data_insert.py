import pandas as pd
import mysql.connector
import numpy as np  # NaN 처리를 위한 라이브러리

def insert_data_to_mysql(excel_file_path, db_config):
    cursor = None  # cursor 초기화 (에러 시 cursor가 참조되지 않도록)
    try:
        # 1. 엑셀 파일 읽기 (첫 번째 행을 컬럼명으로 사용)
        df = pd.read_excel(excel_file_path, header=0)  # header=0으로 설정

        # 2. 실제 컬럼 이름 확인
        print("데이터프레임의 컬럼 이름:", df.columns)

        # 3. 필요한 컬럼만 선택
        df = df[['5.5 LINK ID', 'ITS LINK ID', '도로등급', '도로명', '권역', '연장(km)', '차선수', '전체-평일', '승용차-평일', '버스-평일', '트럭-평일']]

        # 4. NaN 값을 NULL로 대체 (모든 컬럼에서 NaN 처리)
        df = df.apply(lambda col: col.where(pd.notna(col), None))  # NaN을 None으로 변환

        # 5. MySQL에 연결
        connection = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )
        cursor = connection.cursor()

        # 6. 삽입할 SQL 쿼리
        insert_query = """
            INSERT INTO road_data (id, link_id, road_grade, road_name, region, length_km, lane_count, total_traffic, passenger_car_traffic, bus_traffic, truck_traffic)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # 7. 데이터 삽입
        for index, row in df.iterrows():
            values = (
                row['5.5 LINK ID'],        # id
                row['ITS LINK ID'],        # link_id
                row['도로등급'],            # road_grade
                row['도로명'],              # road_name
                row['권역'],                # region
                row['연장(km)'],            # length_km
                row['차선수'],              # lane_count
                row['전체-평일'],           # total_traffic
                row['승용차-평일'],         # 승용차 교통량
                row['버스-평일'],           # 버스 교통량
                row['트럭-평일']            # 트럭 교통량
            )
            cursor.execute(insert_query, values)

        # 8. 변경사항 커밋
        connection.commit()

        print("데이터가 MySQL에 성공적으로 삽입되었습니다.")
    
    except mysql.connector.Error as e:
        print(f"데이터베이스 오류 발생: {e}")
    
    except Exception as e:
        print(f"알 수 없는 오류 발생: {e}")
    
    finally:
        # 9. 커서와 연결 종료
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# DB 설정 (사용자의 데이터베이스 정보로 수정)
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  
    'database': 'traffic_info'   
}

# 엑셀 파일 경로
excel_file_path = 'TrafficVolume(LINK).xlsx'

# 데이터 삽입 함수 호출
insert_data_to_mysql(excel_file_path, db_config)