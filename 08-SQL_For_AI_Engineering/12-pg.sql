-- Arrays and Json in PostgreSQL

--PostgreSQL supports arrays, which allow you to store multiple values in a single column.
--You can create an array column by specifying the data type followed by square brackets ([]).
create table students (
    sid serial primary key,
    marks integer[],
    address jsonb
);
insert into students (marks, address) values (array[85, 90, 78], '{"street": "123 Main St", "city": "Anytown", "state": "CA"}');
select * from students;
-- output:
-- sid |     marks      |                     address   
-- ---+----------------+-------------------------------------
--   1 | {85,90,78}     | {"street": "123 Main St", "city": "Anytown", "state": "CA"}


