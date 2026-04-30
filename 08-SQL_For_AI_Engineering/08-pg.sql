-- Subqueries in SQL

CREATE TABLE mobile_records(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    manufacturer VARCHAR(50),
    price INTEGER,
    units_sold INTEGER
);
INSERT INTO mobile_records (name, manufacturer, price, units_sold) VALUES 
('iPhone 12', 'Apple', 999, 1000000),
('Galaxy S21', 'Samsung', 799, 800000),
('Pixel 5', 'Google', 699, 500000),
('OnePlus 9', 'OnePlus', 729, 300000)
('Xperia 1 II', 'Sony', 1199, 200000)
('Mi 11', 'Xiaomi', 749, 400000);

-- Calculate the average price of phones for each manufacturer and then get the highest average price.
select manufacturer, avg(price) as avg_price from mobile_records group by manufacturer;
--output:
--manufacturer | avg_price
--Apple        | 999
--Samsung      | 799
--Google       | 699
--OnePlus      | 729
--Sony         | 1199
--Xiaomi       | 749

-- Now we will use a subquery to get the maximum average price from the above result.
select max(p.avg_price) as max_avg_price from (select manufacturer, avg(price) as avg_price from mobile_records group by manufacturer) p;
--output:
--max_avg_price
--1199
