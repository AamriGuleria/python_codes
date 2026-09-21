
-- Create a table orders with (order id , product name , product_price , payment_model, exp_delivery_date, actual_delivery_date)
CREATE TABLE orders(
    order_id SERIAL PRIMARY KEY ,
    customer_id INT,
    status TEXT,
    product_name VARCHAR(100),
    product_price DECIMAL(10,2),
    payment_mode VARCHAR(100),
    created_at TIMESTAMP
)