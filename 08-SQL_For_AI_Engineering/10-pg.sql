#Creating Views in PostgreSQL

create table users (
    id serial primary key,
    username varchar(255),
    email varchar(255) 
);

create table posts (
    pid serial primary key,
    user_id integer references users(id),
    posturl varchar(255)
);

insert into users (username, email) values (1,'Alice', 'alice@example.com');
insert into posts (user_id, posturl) values (1, 'https://example.com/post1');
insert into users (username, email) values (3,'Bob', 'bob@example.com');
insert into posts (user_id, posturl) values (4, 'https://example.com/post2');
 
insert into users (username, email) values (2,'Charlie', 'charlie@example.com');
insert into users (username, email) values (4,'David', 'david@example.com');

select * from users;

--Below query will return all users who do not have any posts. It uses a LEFT JOIN to combine the users and posts tables, and then filters for rows where the post's user_id is null, indicating that there is no corresponding post for that user.
create view user_no_posts as
select * from users left join posts on users.id = posts.user_id where posts.user_id is null;
limit 10;

--output: 
-- id | username |      email       | pid | user_id | posturl
----+----------+------------------+-----+---------+----------------------------
--  2 | Charlie  |  

-- update view 

create or replace view user_no_posts as
select * from users left join posts on users.id = posts.user_id where posts.user_id is null
limit 10;

select * from user_no_posts;

-- output:
-- id | username |      email       | pid | user_id | posturl
----+----------+------------------+-----+---------+----------------------------
--  2 | Charlie  |
--  4 | David    |

--Materialized Views in PostgreSQL

--Materialized views are similar to regular views, but they store the result of the query physically on disk.
--This can improve performance for complex queries, as the data is precomputed and can be accessed quickly. 
--However, materialized views need to be refreshed manually to reflect changes in the underlying tables.
create materialized view user_no_posts as
select * from users left join posts on users.id = posts.user_id where posts.user_id is null
limit 10;
select * from user_no_posts;

-- output:
-- id | username |      email       | pid | user_id | posturl
----+----------+------------------+-----+---------+----------------------------
--  2 | Charlie  |
--  4 | David    |
