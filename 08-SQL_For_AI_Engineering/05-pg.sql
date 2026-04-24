-- Operations in SQL (PostgreSQL examples)
-- This file focuses on CRUD + query operations.
-- Assumption: a table `cities(name, country, population, area)` already exists.

-- 1) INSERT (add new rows)
-- Tip: specify column names to avoid errors if table changes.
INSERT INTO cities (name, country, population, area)
VALUES
	('Tokyo', 'Japan', 323232, 4234),
	('Delhi', 'India', 234342223, 1221),
	('Shanghai', 'China', 5556554, 3422),
	('Sao', 'Brazil', 665755, 3032);

-- 2) SELECT (read all rows)
SELECT * FROM cities;

-- 3) Calculated column
-- Population density = population / area
-- `::numeric` prevents integer truncation (e.g., 5/2 = 2.5 instead of 2).
-- `NULLIF(area, 0)` prevents divide-by-zero.
SELECT
	name,
	country,
	population,
	area,
	(population::numeric / NULLIF(area, 0)) AS population_density
FROM cities;

-- 4) WHERE filter
-- Get only the cities with population density > 6000.
SELECT
	name,
	(population::numeric / NULLIF(area, 0)) AS population_density
FROM cities
WHERE (population::numeric / NULLIF(area, 0)) > 6000;

-- 5) ORDER BY + LIMIT
-- Top 3 most populated cities.
SELECT name, country, population
FROM cities
ORDER BY population DESC
LIMIT 3;

-- 6) WHERE with IN
SELECT name, country
FROM cities
WHERE country IN ('India', 'Japan');

-- 7) WHERE with BETWEEN
-- Cities with population between 5 lakh and 1 crore.
SELECT name, population
FROM cities
WHERE population BETWEEN 500000 AND 10000000;

-- 8) GROUP BY (aggregation)
-- Count cities per country and total population per country.
SELECT
	country,
	COUNT(*) AS city_count,
	SUM(population) AS total_population
FROM cities
GROUP BY country
ORDER BY total_population DESC;

-- 9) HAVING (filter aggregated results)
-- Only countries whose average city population is > 1,000,000.
SELECT country, AVG(population) AS avg_population
FROM cities
GROUP BY country
HAVING AVG(population) > 1000000;

-- 10) UPDATE (modify existing rows)
-- Increase Tokyo's population by 1000.
UPDATE cities
SET population = population + 1000
WHERE name = 'Tokyo';

-- 11) DELETE (remove rows)
DELETE FROM cities
WHERE name = 'Sao';

-- 12) Transaction example (TCL)
-- Use transactions when you want multiple statements to succeed/fail together.
-- BEGIN;
-- UPDATE cities SET area = area + 10 WHERE name = 'Delhi';
-- ROLLBACK;  -- undo
-- COMMIT;    -- save