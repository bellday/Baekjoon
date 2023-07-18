-- 코드를 입력하세요
SELECT ANIMAL_TYPE,count(ANIMAL_TYPE) as count
from ANIMAL_INS
group by ANIMAL_TYPE
 having animal_type in ('cat', 'dog')
order by 1