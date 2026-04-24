#--SQL code to create a table named 'cities' with columns for name, country, population, and area.
CREATE TABLE cities( 
name VARCHAR(50),
country VARCHAR(50),
population INTEGER,
area INTEGER
);
#--Inserting data into the 'cities' table for Delhi and Kochi.
INSERT INTO cities VALUES ('Delhi', 'India', 10, 10000);
INSERT INTO cities VALUES ('Delhi', 'India', 10, 10000), ('Kochi', 'India', 4, 10000);
#--Query to select all records from the 'cities' table.
SELECT * from cities;
#--Query to select records from the 'cities' table where the name is 'Kochi'.
SELECT * from cities WHERE name = 'Kochi';