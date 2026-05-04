/*CREATE DATABASE Week3;
*/
CREATE TABLE week3_CUSTOMERS (
	customer_id INT,
    name VARCHAR(50),
    city VARCHAR(50),
    age INT,
    updated_at date
);

INSERT INTO week3_customers VALUES
(1, 'Ravi', 'Hyderabad', 25, '2024-01-10'),
(2, 'Asha', 'Chennai', 30, '2024-01-12'),
(3, 'Imran', 'Hyderabad', 22, '2024-01-11'),
(1, 'Ravi', 'Hyderabad', 26, '2024-02-01');



TABLE week3_orders (
	order_id INT,
    customer_id INT,
    order_date DATE,
    amount INT,
    status VARCHAR(20)
);

INSERT INTO week3_orders VALUES
(101, 1, '2024-01-01', 500, 'completed'),
(102, 2, '2024-02-01', 700, 'completed'),
(103, 3, '2024-03-01', 300, 'return'),
(104, 4, '2024-03-05', 250, 'completed');
