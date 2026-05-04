/* DEDUPLICATION , it the identification and removing the duplicate records*/
WITH ranked_customers AS (		
    SELECT customer_id, name, city, age, updated_at,
           ROW_NUMBER() OVER (
               PARTITION BY customer_id
               ORDER BY updated_at DESC
           ) AS rn
    FROM week3_customers
)
SELECT customer_id,
    name,
    city,
    age,
    updated_at
FROM ranked_customers
WHERE rn = 1;

/* if we have the bad data in latest record, then among valid records, keep the latest one */