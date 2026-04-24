
# Types of SQL Commands (4)

SQL commands are commonly grouped into these 4 categories:

| Type | Full Form | Purpose | Common Commands |
|------|-----------|---------|-----------------|
| DDL | Data Definition Language | Defines/changes database structure (schema) | `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `RENAME` |
| DML | Data Manipulation Language | Inserts/updates/deletes data in tables | `INSERT`, `UPDATE`, `DELETE`, `MERGE` |
| DOL* | (Often written as **DQL**: Data Query Language) | Reads/queries data from tables | `SELECT` (+ `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`) |
| DCL | Data Control Language | Manages permissions and access | `GRANT`, `REVOKE` |

> *Note:* Many books use **DQL** instead of “DOL”. The meaning is the same here: **querying/reading data**.

---

## 1) DDL (Data Definition Language)

Used to create or modify database objects like tables, views, indexes, schemas.

Examples:

```sql
CREATE TABLE cities (
	name VARCHAR(50),
	country VARCHAR(50),
	population INTEGER,
	area INTEGER
);

ALTER TABLE cities ADD COLUMN state VARCHAR(50);
DROP TABLE cities;
```

---

## 2) DML (Data Manipulation Language)

Used to change the data stored in tables.

Examples:

```sql
INSERT INTO cities (name, country, population, area)
VALUES ('Delhi', 'India', 10, 10000);

UPDATE cities
SET population = 11
WHERE name = 'Delhi';

DELETE FROM cities
WHERE name = 'Delhi';
```

---

## 3) DOL / DQL (Data Query Language)

Used to read/retrieve data.

Examples:

```sql
SELECT name, country
FROM cities
WHERE population > 5
ORDER BY population DESC;

SELECT country, COUNT(*) AS city_count
FROM cities
GROUP BY country;
```

---

## 4) DCL (Data Control Language)

Used to control access and privileges.

Examples:

```sql
GRANT SELECT, INSERT ON TABLE cities TO some_user;
REVOKE INSERT ON TABLE cities FROM some_user;
```

---

### Quick Reminder (optional)

Some references also mention **TCL (Transaction Control Language)** for transactions:

```sql
BEGIN;
-- DML statements here
COMMIT;  -- or ROLLBACK;
```
