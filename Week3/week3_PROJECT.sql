WITH latest_customers AS (		/*creating a CTE to  produce the temporary results*/
    SELECT 
        customer_id,
        name,
        city,
        age,
        updated_at,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY updated_at DESC
        ) AS customer_rn
    FROM week3_project_customers
),

ranked_transactions AS (
    SELECT 
        transaction_id,
        customer_id,
        status,
        amount,
        updated_at,
        source_system,
        LAG(status) OVER (	/*using LAG to find the status of previous record*/
            PARTITION BY transaction_id
            ORDER BY updated_at
        ) AS previous_status,
        ROW_NUMBER() OVER (	/*using row number() to rank all the rows*/
            PARTITION BY transaction_id
            ORDER BY updated_at DESC		/* arranging them in decending order so the latest values will apper on top*/
        ) AS transaction_rn
        FROM week3_project_orders
    WHERE status IN ('pending', 'completed', 'failed', 'returned')
)

SELECT 
    rt.transaction_id, 	/*Calling the values using aliase*/ 
    rt.customer_id,
    lc.name,
    lc.city,
    rt.previous_status,
    rt.status AS latest_status,
    rt.amount,
    rt.updated_at AS latest_updated_at,
    rt.source_system
FROM ranked_transactions rt
JOIN latest_customers lc
ON rt.customer_id = lc.customer_id
WHERE rt.transaction_rn = 1		/* we set rn =1 so only one value will apper and removes duplicates*/
  AND lc.customer_rn = 1
ORDER BY rt.transaction_id;