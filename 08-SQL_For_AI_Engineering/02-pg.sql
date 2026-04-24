CREATE tABLE products(
name VARCHAR(100),
price INT,
description VARCHAR(200)
);
#--Inserting data into the 'products' table for a product named 'Laptop'.
INSERT INTO products VALUES ('Laptop', 1000, 'A high-performance laptop suitable for gaming');
#--Adding a new column 'brand' to the 'products' table.
ALTER TABLE products ADD Column brand VARCHAR(50);

SELECT * from products;