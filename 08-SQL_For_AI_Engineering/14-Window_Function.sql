-- Window Functions (PostgreSQL) — Simple Notes + Simple Examples
-- Date: 2026-05-01
--
-- Window function = performs a calculation across a set of rows related to the current row,
-- WITHOUT collapsing rows like GROUP BY.
--
-- General form:
--   <window_function>(...) OVER (
--       PARTITION BY ...   -- optional: groups for the window
--       ORDER BY ...       -- optional: ordering inside each partition
--       frame_clause       -- optional: which rows around current row are included
--   )


/*
============================================================
SETUP (run once)
============================================================
*/

DROP SCHEMA IF EXISTS window_lab CASCADE;
CREATE SCHEMA window_lab;
SET search_path = window_lab;

CREATE TABLE sales (
	sale_id     BIGSERIAL PRIMARY KEY,
	sale_date   DATE NOT NULL,
	region      TEXT NOT NULL,
	salesperson TEXT NOT NULL,
	amount      INT NOT NULL CHECK (amount >= 0)
);

INSERT INTO sales (sale_date, region, salesperson, amount) VALUES
('2026-01-01','West','Asha',  100),
('2026-01-02','West','Asha',  150),
('2026-01-03','West','Vik',    80),
('2026-01-04','West','Vik',   120),
('2026-01-01','East','Neha',  200),
('2026-01-03','East','Neha',   50),
('2026-01-02','East','Ravi',  200),
('2026-01-04','East','Ravi',  180);

SELECT * FROM sales ORDER BY region, sale_date, salesperson, sale_id;


/*
============================================================
1) ROW_NUMBER / RANK / DENSE_RANK
============================================================
*/

-- ROW_NUMBER: unique row number inside each partition (no ties)
SELECT
	region,
	salesperson,
	amount,
	ROW_NUMBER() OVER (PARTITION BY region ORDER BY amount DESC) AS rn
FROM sales
ORDER BY region, rn;

-- RANK: ties get same rank; gaps can appear (1,1,3,...)
SELECT
	region,
	salesperson,
	amount,
	RANK() OVER (PARTITION BY region ORDER BY amount DESC) AS rnk
FROM sales
ORDER BY region, rnk, salesperson;

-- DENSE_RANK: ties get same rank; no gaps (1,1,2,...)
SELECT
	region,
	salesperson,
	amount,
	DENSE_RANK() OVER (PARTITION BY region ORDER BY amount DESC) AS dense_rnk
FROM sales
ORDER BY region, dense_rnk, salesperson;


/*
============================================================
2) Top-N per group (very common)
============================================================
*/

-- Example: top 2 sales amounts per region
WITH ranked AS (
	SELECT
		s.*,
		ROW_NUMBER() OVER (PARTITION BY region ORDER BY amount DESC, sale_id) AS rn
	FROM sales s
)
SELECT *
FROM ranked
WHERE rn <= 2
ORDER BY region, rn;


/*
============================================================
3) Aggregates as window functions (running totals)
============================================================
*/

-- Sum by region for each row (same total repeated per row in region)
SELECT
	region,
	sale_date,
	salesperson,
	amount,
	SUM(amount) OVER (PARTITION BY region) AS region_total
FROM sales
ORDER BY region, sale_date, sale_id;

-- Running total (cumulative sum) by region ordered by date
-- Frame explained:
--   ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
-- means: from first row in partition up to this row.
SELECT
	region,
	sale_date,
	amount,
	SUM(amount) OVER (
		PARTITION BY region
		ORDER BY sale_date, sale_id
		ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
	) AS running_total
FROM sales
ORDER BY region, sale_date, sale_id;


/*
============================================================
4) Moving average (window frame)
============================================================
*/

-- 3-row moving average per region (previous row, current row, next row)
SELECT
	region,
	sale_date,
	amount,
	ROUND(
		AVG(amount) OVER (
			PARTITION BY region
			ORDER BY sale_date, sale_id
			ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
		)::numeric,
		2
	) AS mov_avg_3_rows
FROM sales
ORDER BY region, sale_date, sale_id;


/*
============================================================
5) LAG / LEAD (compare with previous/next row)
============================================================
*/

-- Previous sale amount within same region
SELECT
	region,
	sale_date,
	amount,
	LAG(amount) OVER (PARTITION BY region ORDER BY sale_date, sale_id) AS prev_amount,
	amount - COALESCE(LAG(amount) OVER (PARTITION BY region ORDER BY sale_date, sale_id), 0) AS diff_from_prev
FROM sales
ORDER BY region, sale_date, sale_id;

-- Next sale amount within same region
SELECT
	region,
	sale_date,
	amount,
	LEAD(amount) OVER (PARTITION BY region ORDER BY sale_date, sale_id) AS next_amount
FROM sales
ORDER BY region, sale_date, sale_id;


/*
============================================================
6) Window function vs GROUP BY (key idea)
============================================================
*/

-- GROUP BY reduces rows (one row per region)
SELECT region, SUM(amount) AS region_total
FROM sales
GROUP BY region
ORDER BY region;

-- Window keeps rows (each sale row stays, plus region_total)
SELECT
	sale_id,
	region,
	amount,
	SUM(amount) OVER (PARTITION BY region) AS region_total
FROM sales
ORDER BY sale_id;


/*
============================================================
Quick cheatsheet
============================================================
*/

-- Common patterns
-- 1) Top-N per group: ROW_NUMBER() OVER (PARTITION BY group ORDER BY metric DESC)
-- 2) Running total: SUM(x) OVER (PARTITION BY group ORDER BY t ROWS UNBOUNDED PRECEDING)
-- 3) Change vs previous: x - LAG(x) OVER (PARTITION BY group ORDER BY t)
-- 4) Moving average: AVG(x) OVER (PARTITION BY group ORDER BY t ROWS BETWEEN k PRECEDING AND k FOLLOWING)
