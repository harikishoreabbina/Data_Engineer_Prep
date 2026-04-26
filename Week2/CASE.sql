/* CASE is used as a If-Else condition in SQL */
SELECT name,
CASE WHEN age > 18 THEN 'Adult' ELSE 'Minor'
END AS category
FROM customers