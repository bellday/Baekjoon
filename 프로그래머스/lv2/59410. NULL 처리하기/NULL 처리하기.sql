-- 코드를 입력하세요
SELECT animal_type, COALESCE(name, 'No name') AS name, SEX_UPON_INTAKe
FROM animal_ins
ORDER BY animal_id;