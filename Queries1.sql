/*---Creating orders table---*/
/*
CREATE TABLE orders (
	order_id INT,
    customer_id INT,
    amount INT
);

INSERT INTO orders VALUES
(101, 1, 500),
(102, 2, 700),
(103, 1, 300);
*/


/*--- SELECT is used to retrive the dharidbata from database*----/
/*SELECT name, age FROM customers;*/
SELECT * FROM customers;
Select city FROM customers;

/* ---WHERE is used to filter rows based on condition and show them ---*/

/*SELECT * FROM customers WHERE age> 25;*/
/*SELECT * FROM customers WHERE age< 30;*/
/*SELECT * FROM customers WHERE city = 'Chennai'*/


/*--- ORDER BY is used to sort our querys---*/

/*SELECT * FROM customers ORDER BY age DESC;     with this query we are printing values in Decending order*/
/*SELECT * FROM customers ORDER BY age ASC;*/

SELECT * FROM customers ORDER BY name ASC; 