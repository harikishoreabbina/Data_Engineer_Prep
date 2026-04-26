/* Having is yes to filter after the group by is done*/

SELECT customer_id, count(*)
FROM orders
Group By customer_id
Having COUNT(*) > 1;