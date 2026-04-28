/* JOIN is use to combine the data from multiple tables */

select c.name, o.amount 
from customers c 
INNER JOIN orders o 
ON c.id = o.customer_id;

/* join customers and orders*/
SELECT * FROM customers c 
INNER JOIN orders o
ON c.id = o.customer_id;


SELECT c.name,o.amount FROM customers c
INNER JOIN orders o
ON c.id = o.customer_id;