-- 코드를 입력하세요
SELECT LEFT(product_code, 2), COUNT(*) AS PRODUCTs  FROM product
GROUP BY 1;