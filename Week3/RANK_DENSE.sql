/*RANK*/
/* this is a window function used for ranking the rows*/

SELECT customer_id, amount,
       RANK() OVER (ORDER BY amount DESC) AS amount_rank,
       DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_amount_rank
FROM week3_orders;


SELECT order_id,customer_id,amount,
	row_number() over (ORDER BY amount DESC) AS row_num_amount,
    rank() over (order by amount DESC) AS rank_amount,
    dense_rank() over (order by amount desc) AS desnse_rank_amount
FROM week3_orders;

/* as of now their are no ties, so their is no difference in the outputs*/
/*
INSERT INTO week3_orders (
    order_id,
    customer_id,
    order_date,
    amount,
    status
)
VALUES (
    105,
    5,
    '2024-04-01',
    500,
    'completed'
);
*/

SELECT order_id,customer_id,order_date,amount,status,
	Rank () over(order by amount desc) as rank_amount
FROM week3_orders;
