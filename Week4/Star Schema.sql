-- =========================================
-- STAR SCHEMA DESIGN


CREATE TABLE dim_customer (

    -- Surrogate Key
    customer_key INT PRIMARY KEY,

    -- Business Key
    customer_id INT,

    -- Customer Attributes
    customer_name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50),
    customer_segment VARCHAR(50),

    -- Type 2 SCD Columns
    effective_start_date DATE,
    effective_end_date DATE,
    is_current VARCHAR(1)
);


CREATE TABLE dim_product (

    -- Surrogate Key
    product_key INT PRIMARY KEY,

    -- Business Key
    product_id INT,

    -- Product Attributes
    product_name VARCHAR(100),
    category VARCHAR(50),
    brand VARCHAR(50),
    price DECIMAL(10,2)
);

CREATE TABLE dim_date (

    -- Primary Key
    date_key INT PRIMARY KEY,

    -- Date Attributes
    full_date DATE,
    day_number INT,
    month_number INT,
    quarter_number INT,
    year_number INT
);


CREATE TABLE dim_promotion (

    -- Surrogate Key
    promotion_key INT PRIMARY KEY,

    -- Business Key
    promotion_id INT,

    -- Promotion Attributes
    promotion_name VARCHAR(100),
    discount_percent DECIMAL(5,2),
    start_date DATE,
    end_date DATE
);


CREATE TABLE fact_sales (

    -- Primary Key
    sales_key INT PRIMARY KEY,

    -- Order Details
    order_id INT,
    order_item_id INT,

    -- Foreign Keys to Dimensions
    date_key INT,
    customer_key INT,
    product_key INT,
    promotion_key INT,

    -- Measurable Metrics
    quantity INT,
    unit_price DECIMAL(10,2),
    discount_amount DECIMAL(10,2),
    sales_amount DECIMAL(10,2),

    -- Foreign Key Relationships
    FOREIGN KEY (date_key)
    REFERENCES dim_date(date_key),

    FOREIGN KEY (customer_key)
    REFERENCES dim_customer(customer_key),

    FOREIGN KEY (product_key)
    REFERENCES dim_product(product_key),

    FOREIGN KEY (promotion_key)
    REFERENCES dim_promotion(promotion_key)
);