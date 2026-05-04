WITH latest_customers AS (
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
        ROW_NUMBER() OVER (
            PARTITION BY transaction_id
            ORDER BY updated_at DESC
        ) AS transaction_rn
        FROM week3_project_orders
    WHERE status IN ('pending', 'completed', 'failed', 'returned')
)

SELECT 
    rt.transaction_id,
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
WHERE rt.transaction_rn = 1
  AND lc.customer_rn = 1
ORDER BY rt.transaction_id;