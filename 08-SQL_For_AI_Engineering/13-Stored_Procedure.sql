create table products(
    pid serial primary key,
    product_name varchar(50),
    price integer,
    quality integer
);

create table sales(
    sid serial primary key,
    order_date varchar(50),
    product_name varchar(50),
    product_id integer references products(pid)
);

insert into products (product_name, price, quality) values ('iphone', 100, 5);
insert into products (product_name, price, quality) values ('ipad', 150, 4);   


-- Stored Procedures in PostgreSQL

create or replace procedure <stored_procedure_name>(IN product_name varchar(50), IN price integer, IN quality integer)
language plpgsql
as $$
-- This procedure inserts a new product into the products table and then creates a corresponding entry in the sales table with the current date.
declare
-- Variable to hold the new product ID after insertion
v_product_id integer;
v_count integer;
begin
    -- Insert the new product into the products table and return the generated product ID
end;
$$;

create or replace procedure product_perchased(p_name varchar, p_quantity int)
language plpgsql
as $$
declare
    v_product_id varchar(50);
begin

    select count(1)
    into v_count
    where product_name = p_name
    and quality >= p_quantity;

    if v_count > 0 then
        

        --1. select the product from prroduct table 
        select pid 
        into v_product_id
        from products
        where product_name = p_name;
        --2. insert the product into sales table with current date
        insert into sales (order_date, product_name, product_id) values ('1st may 2026', v_product_id);

        --3. update the quality of the product in products table by reducing the quantity purchased
        update products set quality = quality - p_quantity where p_id = v_product_id;

        raise notice 'procedure executed successfully';
    else
        raise notice 'product not available in sufficient quantity';
    end if;   
end; 
$$;

-- To call the stored procedure, you can use the CALL statement:
call product_perchased('iphone', 2);
-- output:
-- NOTICE:  procedure executed successfully 
select * from products;
-- output:
-- pid | product_name | price | quality
----+--------------+-------+---------
--  1 | iphone       |   100 |       3
--  2 | ipad         |   150 |       4



i want to purchase 6 iphones but the procedure will check the quality of the product and if it is less than the quantity requested, it will raise a notice that the product is not available in sufficient quantity.
script?
call product_perchased('iphone', 6);
-- output:
-- NOTICE:  product not available in sufficient quantity