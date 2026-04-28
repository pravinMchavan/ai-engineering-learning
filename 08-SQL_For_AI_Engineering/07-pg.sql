--Joints in SQL 

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(50)
);

CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    posturl VARCHAR(100),
    user_id INTEGER REFERENCES users(id)
);

INSERT INTO users (username, email) VALUES 
('abc','abc@gmail.com'),
('def','def@gmail.com'), 
('ghi','ghi@gmail.com'),
('jkl','jkl@gmail.com');

INSERT INTO posts (posturl, user_id) VALUES 
('https://images.com',1),
('https://videos.com',2),
('https://documents.com',3),
('https://audio.com',4);

select * from users left join posts on users.id = posts.user_id;
--Here we are using left join to get all the records from users table and matching records from posts table. 
--If there is no match in posts table, it will return NULL for those columns.

select * from users right join posts on users.id = posts.user_id;
--Here we are using right join to get all the records from posts table and matching records from

select * from users full join posts on users.id = posts.user_id;
--Here we are using full join to get all the records from both tables.

select * from users inner join posts on users.id = posts.user_id;
--Here we are using inner join to get only the matching records from both tables.

--find the users who have not posted anything.
select * from users left join posts on users.id = posts.user_id where posts.id is null;
--find the users who have posted something.
select * from users inner join posts on users.id = posts.user_id;
--find the users who have posted something and the posturl is 'https://images.com'.
select * from users inner join posts on users.id = posts.user_id where posts.posturl = 'https://images.com';


--to access the perticular columns and rows from the tables, we can use the table name or alias.
select u.username, u.email, from users u left join posts p on u.id = p.user_id where p.posturl = 'https://images.com';

-- Aggregation (Group by) clause in SQL
insert into posts (posturl, user_id) values 
('https://images.com',1),
('https://images.com',1),
('https://videos.com',2),
('https://documents.com',3),
('https://audio.com',1),
('https://audio.com',4),
('https://audio.com',1);



