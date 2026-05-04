/* SUBQUERIES is a query placed inside another query. the inner query gives a result used by the outer query */

/* CORRELATED SUBQUERIES is a query depends on each row from the outer query*/

SELECT name
FROM week3_customers
WHERE customer_id IN (
    SELECT customer_id
    FROM week3_orders
);

/*USING JOIN*/

SELECT c.name
FROM week3_customers c
JOIN week3_orders o
ON c.customer_id = o.customer_id;

/*SUBQUERIES are better when we only need to filter one table*/
/*JOIN is better when you need columns from both tables*/