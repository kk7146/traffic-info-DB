CREATE DATABASE traffic_info;
use traffic_info

CREATE TABLE road_data (
    id INT PRIMARY KEY,					-- 5.5 LINK ID 
    link_id VARCHAR(1000),              -- ITS LINK ID (문자열)
    road_grade VARCHAR(50),             -- 도로등급
    road_name VARCHAR(255),             -- 도로명
    region VARCHAR(100),                -- 권역
    length_km FLOAT,                    -- 연장 (km)
    lane_count INT,                     -- 차선수
    total_traffic INT,                  -- 전체 교통량
    passenger_car_traffic INT,          -- 승용차 교통량
    bus_traffic INT,                    -- 버스 교통량
    truck_traffic INT,                  -- 트럭 교통량
    is_frozen BOOLEAN DEFAULT FALSE     -- 빙결 구간 여부
);

CREATE TABLE road_average_speed_data (
    id INT PRIMARY KEY,					-- 5.5 LINK ID 
    link_id VARCHAR(1000),              -- ITS LINK ID (문자열)
    average_speed INT                   -- 평균속력
);
