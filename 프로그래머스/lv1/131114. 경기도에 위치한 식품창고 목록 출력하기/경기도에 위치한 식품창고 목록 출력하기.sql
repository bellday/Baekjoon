SELECT 
    warehouse_id ,
    warehouse_name ,
    address ,
    CASE 
        WHEN freezer_yn = 'Y' THEN 'Y'
        WHEN freezer_yn = 'N' THEN 'N'
        WHEN freezer_yn is null THEN 'N'
    END
FROM food_warehouse
WHERE warehouse_name LIKE '%경기%'    
ORDER BY warehouse_id asc