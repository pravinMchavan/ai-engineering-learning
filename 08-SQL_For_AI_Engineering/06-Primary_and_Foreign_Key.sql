#--A Primary key is a column or a set of columns that uniquely identifies each row in a table. It must contain unique values and cannot contain NULL values. 
#--A foreign key is a column or a set of columns in one table that refers to the primary key in another table. It establishes a relationship between the two tables.

CREATE TABLE users9(
    id SERIAL PRIMARY KEY, #-- serial is used to auto genrate sr no. along with primary key
    username VARCHAR(50),
    email VARCHAR(50)
);

CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    posturl VARCHAR(100)
    user_id INTEGER REFERENCES users(id) #-- this is foreign key which is referencing to primary key of users table we have created a relationship between users and posts table
);