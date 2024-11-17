UPDATE road_data
SET is_frozen = TRUE
WHERE link_id LIKE '%3010139600%'
   OR link_id LIKE '%3010141100%'
   OR link_id LIKE '%3010205600%'
   OR link_id LIKE '%3010154400%';