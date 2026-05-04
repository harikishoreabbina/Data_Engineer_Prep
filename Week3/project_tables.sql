
CREATE TABLE week3_project_customers (
    customer_id INT,
    name VARCHAR(50),
    city VARCHAR(50),
    age INT,
    updated_at DATE
);

INSERT INTO week3_project_customers VALUES
(1, 'Ravi', 'Hyderabad', 25, '2024-01-10'),
(2, 'Asha', 'Chennai', 30, '2024-01-12'),
(3, 'Imran', 'Hyderabad', 22, '2024-01-11'),
(1, 'Ravi', 'Hyderabad', 26, '2024-02-01');

CREATE TABLE week3_project_orders (
    transaction_id INT,
    customer_id INT,
    status VARCHAR(30),
    amount INT,
    updated_at DATE,
    source_system VARCHAR(50)
);

INSERT INTO week3_project_orders VALUES
(101, 1, 'pending', 500, '2024-01-01', 'Amazon'),
(101, 1, 'completed', 500, '2024-01-02', 'Amazon'),
(102, 2, 'pending', 700, '2024-01-03', 'Walmart'),
(102, 2, 'failed', 700, '2024-01-04', 'Walmart'),
(103, 3, 'pending', 250, '2024-01-05', 'Amazon'),
(103, 3, 'completed', 250, '2024-01-06', 'Amazon'),
(104, 1, 'pending', 900, '2024-01-07', 'Amazon'),
(104, 1, 'returned', 900, '2024-01-08', 'Amazon');