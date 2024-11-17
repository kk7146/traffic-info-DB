# traffic-info-DB

## build
mysql.server start
mysql -u root

pip install pandas
pip install mysql-connector-python
pip install openpyxl

mysql 내에서
SOURCE <init.sql 경로>;

python3 road_data_insert.py
python3 average_speed_data_insert.py

mysql 내에서
SOURCE <freeze_update.sql 경로>;

## 빙결 구간 ITS 노드 변환 결과
타 레포지토리에 변환기 만든 것으로 추출.
거리는 m 단위. 오차 범위는 그리 크지 않음.

가장 가까운 링크 ID: 3010139600
거리: 4.819970629035268

가장 가까운 링크 ID: 3010141100
거리: 5.547761272597961

가장 가까운 링크 ID: 3010171800
거리: 4.131284070267039

가장 가까운 링크 ID: 3010205600
거리: 12.02818681710007

가장 가까운 링크 ID: 3010062700
거리: 2.8543292932943523

가장 가까운 링크 ID: 3010062700
거리: 3.939212524993539

가장 가까운 링크 ID: 3020477100
거리: 4.9824248141109315

가장 가까운 링크 ID: 3020469200
거리: 5.526759670055211

가장 가까운 링크 ID: 3010154400
거리: 5.231009085189197

가장 가까운 링크 ID: 3010163400
거리: 6.727761099001822

## 오픈데이터 무결성 조사
road_data에는 있지만 road_average_speed_data 없는 id 찾기
SELECT rd.id AS missing_in_speed_data
FROM road_data rd
LEFT JOIN road_average_speed_data rasd ON rd.id = rasd.id
WHERE rasd.id IS NULL;

road_average_speed_data에는 있지만 road_data에는 없는 id 찾기
SELECT rasd.id AS missing_in_road_data
FROM road_average_speed_data rasd
RIGHT JOIN road_data rd ON rasd.id = rd.id
WHERE rd.id IS NULL;

결과적으로 2개의 데이터가 비어있다고 뜸.

+-----------------------+
| missing_in_speed_data |
+-----------------------+
|               1029472 |
|               1029504 |
+-----------------------+