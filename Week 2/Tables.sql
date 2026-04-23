CREATE TABLE customers (
    id INT,
    name VARCHAR(50),
    age INT,
    city VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    amount INT
);

INSERT INTO customers VALUES
(1, 'Ravi', 25, 'Hyderabad'),
(2, 'Asha', 30, 'Chennai'),
(3, 'Imran', 22, 'Bangalore');

INSERT INTO orders VALUES
(101, 1, 500),
(102, 2, 700),
(103, 3, 300);