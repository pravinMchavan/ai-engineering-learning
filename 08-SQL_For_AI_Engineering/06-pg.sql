--A Primary key is a column or a set of columns that uniquely identifies each row in a table. It must contain unique values and cannot contain NULL values. 
--A foreign key is a column or a set of columns in one table that refers to the primary key in another table. It establishes a relationship between the two tables.

CREATE TABLE users9(
    id SERIAL PRIMARY KEY, -- serial is used to auto genrate sr no. along with primary key
    username VARCHAR(50),
    email VARCHAR(50)
);

CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    posturl VARCHAR(100)
    user_id INTEGER REFERENCES users(id) -- this is foreign key which is referencing to primary key of users table we have created a relationship between users and posts table
    -- Now searial no will be id of posts 
);

INSERT INTO users (username, email) VALUES ('abc','abc@gmail.com');
-- We have inserted a record in users table and it will automatically generate id for us because we have used serial data type for id column
SELECT * FROM users;

INSERT INTO posts (posturl, user_id) VALUES ('https://images.com',1);

SELECT * FROM posts JOIN users ON posts.user_id = users.id; -- this will join the posts and users table based on the foreign key relationship we have established between them and it will return all the columns from both tables where the user_id in posts table matches the id in users table


--what is data consistency?
-- Data consistency refers to the accuracy and reliability of data across different tables and databases.
-- It ensures that data is the same in all places where it is stored, preventing discrepancies and errors.
-- In the context of primary and foreign keys, data consistency is maintained by ensuring that foreign key values in one table correspond to valid primary key values in another table,
-- thus preserving the integrity of the relationships between tables.

-- Types of data consistency:
-- 1.On Delete Restrict: This means that if there are any records in the child table (posts) that reference a record in the parent table (users), you cannot delete that record from the parent table. It will prevent deletion to maintain data consistency.
-- 2.On Delete Cascade: This means that if you delete a record from the parent table
-- 3.On Delete Set Null: This means that if you delete a record from the parent table, the corresponding foreign key values in the child table will be set to NULL. This allows the child records to remain in the database without referencing a non-existent parent record, thus maintaining data consistency.
-- 4.On Delete No Action: This means that if you try to delete a record from the parent table that has related records in the child table, the database will not allow the deletion and will throw an error. This is similar to "On Delete Restrict" but it checks for the constraint at the end of the statement execution rather than immediately.
-- 5.On Delete Set Default: This means that if you delete a record from the parent table, the corresponding foreign key values in the child table will be set to their default value. This allows the child records to remain in the database without referencing a non-existent parent record, thus maintaining data consistency.

--WILL DELETE POSTS TABLE AND CREATE WITH ON DELETE CASCADE
DROP TABLE posts;

CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    posturl VARCHAR(100),
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE -- this means that if we delete a record from users table then all the corresponding records in posts table will also be deleted automatically to maintain data consistency
);

