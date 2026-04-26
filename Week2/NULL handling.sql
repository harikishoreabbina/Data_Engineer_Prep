/* NULL handling is used to represents missing vales*/
INSERT INTO customers VALUES (4, 'hari', NULL, 'Hyderabad');
/* we added a new row in customers table*/
SELECT * from customers where age IS NULL;