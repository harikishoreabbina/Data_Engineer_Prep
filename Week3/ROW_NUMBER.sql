/* WINDOW FUNCTION*/
/* ROW_NUMBER() will assign a unique number to each row inside a group, it is used for ranking and deduplication*/

/*SELECT name,city,age,
	row_number() over (
		PARTITION BY city
		ORDER BY age DESC
    )AS city_age_rank
FROM week3_customers*/

SELECT customer_id, name,city,age,
	row_number() over (
		PARTITION BY city
        ORDER BY age DESC
        )AS age_rank_BY_city
FROM week3_customers;

/*Rank orders by amount within each customer_id*/

SELECT order_id,customer_id,order_date,amount,status,
		row_number() over(
		partition by customer_id
        order by amount DESC
        ) AS RANK_amount_per_customer
FROM week3_orders;

Select order_id,customer_id,amount,
	row_number() over(
		partition by customer_id
        order by amount DESC
	) AS ROW_NUM
FROM week3_orders;