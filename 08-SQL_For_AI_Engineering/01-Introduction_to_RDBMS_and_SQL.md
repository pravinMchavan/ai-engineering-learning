# Introduction to RDBMS and SQL

This note introduces relational databases (RDBMS) and SQL with a focus on the main practical goal in data science: gathering the right data from an RDBMS and turning it into an analysis-ready dataset.

## What is a Database?

A **database** is an organized collection of data designed for efficient storage, retrieval, and updates.

Common database types:

- **Relational (SQL)**: data stored in tables with rows and columns (PostgreSQL, MySQL, SQL Server, SQLite, Oracle)
- **NoSQL**: document, key-value, wide-column, graph (MongoDB, DynamoDB, Cassandra, Neo4j)

## What is an RDBMS?

An **RDBMS (Relational Database Management System)** stores data in **tables** and enforces relationships between tables using **keys**.

Core ideas:

- **Table**: a set of rows (records) and columns (fields)
- **Schema**: the structure/definition of tables and constraints
- **Primary key (PK)**: uniquely identifies a row
- **Foreign key (FK)**: references a PK in another table (creates a relationship)
- **Constraints**: rules such as NOT NULL, UNIQUE, CHECK, DEFAULT

### Relationships

- **One-to-one**: one row relates to one row
- **One-to-many**: one row relates to many rows (very common)
- **Many-to-many**: implemented using a **junction/bridge** table

## Why SQL?

**SQL (Structured Query Language)** is used to:

- Read data (filter, aggregate, join)
- Insert/update/delete records
- Define schemas and constraints
- Control permissions

SQL is often the fastest path from "data stored somewhere" to "a dataset ready for analysis/modeling".

## Main Goal: Gathering Data from an RDBMS for Data Science

In most organizations, the RDBMS is the system of record for business events (orders, payments, app activity, support tickets). A data scientist uses SQL to translate a question into a well-defined dataset.

### What “gathering data” really means

Gathering data is not just exporting rows. It usually includes:

- Choosing the right source tables (system of record vs derived tables)
- Combining tables using relationships (keys)
- Filtering to the correct population and time window
- Aggregating to the correct level of detail
- Handling missingness and duplicates thoughtfully
- Making the result reproducible and easy to validate

### The concept of dataset grain (level of detail)

Before extracting, decide the dataset grain. Examples of grain:

- One row per customer
- One row per order
- One row per customer per day

Getting grain wrong is one of the most common causes of incorrect results (double counting, inflated totals, inconsistent labels).

### A typical data science extraction workflow (conceptual)

- Clarify the objective: What decision/model/analysis will use this dataset?
- Define the population: Who/what is included, and what is excluded?
- Define time logic: event time vs processing time, timezone, and what “last 30 days” is anchored to.
- Identify entities and relationships: which tables represent the main entity (customer/order/session) and which are supporting.
- Design the dataset grain and features/targets at that grain.
- Validate quality: row counts, uniqueness at the chosen grain, missing values, and reasonableness checks.
- Document definitions: metric logic, assumptions, and known limitations so others can reproduce results.

### Common pitfalls when extracting from RDBMS

- Duplicate rows from joins when relationships are one-to-many
- Filtering after aggregation vs before aggregation (changes meaning)
- Confusing NULL with zero/empty
- Data leakage in labels/features due to incorrect time windows
- Mixing historical snapshots with current state without realizing it
- Slow queries caused by scanning large tables unnecessarily

## SQL Command Categories

- **DQL** (Data Query Language): SELECT (reading data)
- **DML** (Data Manipulation Language): INSERT / UPDATE / DELETE / MERGE (changing data)
- **DDL** (Data Definition Language): CREATE / ALTER / DROP / TRUNCATE (defining structures)
- **DCL** (Data Control Language): GRANT / REVOKE (permissions)
- **TCL** (Transaction Control Language): COMMIT / ROLLBACK / SAVEPOINT (transaction control)

## The Building Blocks of a Query

Key clauses:

- SELECT: which columns/expressions to return
- FROM: which table(s)
- WHERE: row-level filtering (before aggregation)
- GROUP BY: defines the aggregation level
- HAVING: group-level filtering (after aggregation)
- ORDER BY: sorting
- LIMIT / TOP: restrict output rows (dialect dependent)

## Joins (How Tables Combine)

Joins combine rows from two tables using a matching condition (usually PK/FK).

- **INNER JOIN**: only matching rows
- **LEFT JOIN**: all rows from left table + matches from right (else NULLs)
- **RIGHT JOIN**: all rows from right table + matches from left
- **FULL OUTER JOIN**: all rows from both sides, matched where possible

## NULLs (Important in SQL)

NULL means "unknown/missing" and behaves differently from normal values.

- Comparisons like "= NULL" do not behave like normal equality checks
- Use IS NULL / IS NOT NULL when reasoning about missingness

## Aggregations (Summaries)

Common aggregates:

- COUNT(*) (rows)
- COUNT(column) (non-missing values)
- SUM, AVG, MIN, MAX

## Indexes (Performance Basics)

An **index** is a data structure that speeds up reads on certain columns.

- Helps: filtering, joining, and sorting on indexed columns
- Costs: slower writes (because indexes also must be updated) and extra storage

As a data scientist, you don’t always create indexes, but you should understand when a query is slow because of missing indexes or scanning huge tables.

## Transactions and ACID

A **transaction** is a group of operations that should succeed or fail together.

ACID properties:

- **Atomicity**: all or nothing
- **Consistency**: rules/constraints remain valid
- **Isolation**: concurrent transactions don’t corrupt each other
- **Durability**: committed changes persist

## Normalization (Why Multiple Tables Exist)

Normalization reduces duplication and update anomalies.

In practice:

- Store entities separately (e.g., customers, orders, order_items)
- Use keys to connect them
- Denormalize carefully for analytics/performance when needed

## Role of a Data Scientist: Using SQL

SQL is one of the most-used tools in a data scientist’s workflow. Typical responsibilities include:

- **Data extraction for analysis**: build reliable datasets from multiple tables using joins and filters.
- **Defining metrics and KPIs**: implement metric logic (active users, retention, conversion) using consistent SQL.
- **Exploratory Data Analysis (EDA)**: quickly slice/aggregate data to find patterns, anomalies, and distributions.
- **Data quality checks**: validate assumptions (duplicates, missing values, out-of-range values, referential integrity).
- **Feature creation for ML**: create model features with aggregations/windows (e.g., last 7 days activity) and export to notebooks/pipelines.
- **Label generation**: define target labels (churn, fraud, purchase) with time-aware logic to avoid leakage.
- **Experiment and cohort analysis**: analyze A/B tests, cohorts, funnels, and time series.
- **Collaboration with data engineering**: communicate data needs, propose schema changes, review tables, and translate analysis requirements into pipeline specs.
- **Performance-aware querying**: write efficient queries (limit scanned data, avoid unnecessary DISTINCTs, use appropriate filters, understand partitions/indexes).
- **Governance and privacy**: follow access controls, handle PII carefully, and document logic so results are reproducible.

### A practical mindset for SQL in data science

- Prefer building a **clean, documented query** that others can re-run.
- Treat SQL as production code when it powers dashboards, features, or decision-making.
- Be explicit about time windows and definitions ("last 30 days" from what date/timezone?).
