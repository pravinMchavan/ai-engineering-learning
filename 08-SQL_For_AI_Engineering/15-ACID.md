# ACID in Databases (Theory + Simple Examples)

ACID is a set of guarantees a database tries to provide for a **transaction**.

## What is a transaction?

A **transaction** is a logical unit of work:
- it starts (`BEGIN`)
- it performs one or more reads/writes
- it ends with **success** (`COMMIT`) or **failure** (`ROLLBACK`)

The purpose of ACID is to make transaction outcomes predictable even when:
- multiple users run transactions at the same time (concurrency)
- the system crashes (power failure / process crash)

> Important: ACID is about database state. Effects outside the DB (sending email, charging a payment gateway) need extra patterns (idempotency, outbox, retries).

## A — Atomicity ("all or nothing")

If a transaction has multiple steps, either **all steps succeed** or **none are applied**.

### Theoretical meaning

Atomicity means the database never exposes a “half-applied” transaction as committed state.
- If the transaction commits, all its changes become visible.
- If it aborts (error/deadlock/crash), none of its changes should remain.

### Simple example

```sql
BEGIN;

UPDATE accounts
SET balance = balance - 50
WHERE id = 1;

UPDATE accounts
SET balance = balance + 50
WHERE id = 2;

COMMIT;
```

If something fails in the middle (error, crash, etc.), the transaction is rolled back.

```sql
BEGIN;
UPDATE accounts SET balance = balance - 50 WHERE id = 1;

-- Oops: wrong table/constraint error happens here
UPDATE some_wrong_table SET x = 1;

ROLLBACK; -- balance change is undone
```

**Key idea:** partial updates should not remain.

## C — Consistency ("rules are always true")

Consistency means the database moves from one valid state to another valid state.

### Theoretical meaning

Consistency is about **invariants** (rules) being preserved by every committed transaction.
Examples of invariants:
- balances are never negative
- every order references an existing customer (foreign key)
- an email must be unique

This is usually enforced by:
- **constraints** (PRIMARY KEY, UNIQUE, CHECK, NOT NULL, FOREIGN KEY)
- **triggers** (optional)
- application logic (also important)

### Common confusion: ACID Consistency vs CAP Consistency

"Consistency" in **ACID** means “data respects rules/invariants after each commit.”

"Consistency" in **CAP** means “all replicas see the same value at the same time.”
They are different concepts.

### Simple example (CHECK constraint)

```sql
CREATE TABLE accounts (
	id INT PRIMARY KEY,
	balance INT NOT NULL CHECK (balance >= 0)
);

BEGIN;
UPDATE accounts SET balance = -100 WHERE id = 1; -- fails
ROLLBACK;
```

The constraint prevents invalid data from being committed.

## I — Isolation ("transactions don’t interfere")

Isolation controls how much one transaction can see the effects of another transaction **before it commits**.

### Theoretical meaning

Isolation defines what kind of “concurrent behavior” is allowed.
At the strongest level (**serializable**), the result is as if transactions ran one-by-one in some order.

In practice, databases offer multiple isolation levels to trade off correctness vs concurrency/performance.

PostgreSQL supports multiple isolation levels:
- **READ COMMITTED** (default): each statement sees the latest committed data
- **REPEATABLE READ**: a consistent snapshot for the whole transaction
- **SERIALIZABLE**: strongest; may fail with `serialization_failure` and needs retry

### Anomalies (what isolation is trying to prevent)

- **Dirty read:** read data written by another transaction that has not committed yet.
- **Non-repeatable read:** read the same row twice and get different results because another transaction committed in between.
- **Phantom read:** rerun a range query and see new rows appear/disappear because another transaction committed inserts/deletes.
- **Lost update:** two transactions overwrite each other’s updates.
- **Write skew:** two transactions each make a change that is individually valid, but together violate a rule (common in snapshot-based systems).

### PostgreSQL note (important for theory)

PostgreSQL uses MVCC, so:
- plain `SELECT` usually doesn’t block writes
- dirty reads are not allowed in normal isolation levels
- `SERIALIZABLE` can abort a transaction to maintain correctness; application should **retry**

### Example idea (READ COMMITTED)

Session 1:
```sql
BEGIN;
SELECT balance FROM accounts WHERE id = 1; -- returns 100
```

Session 2:
```sql
UPDATE accounts SET balance = 150 WHERE id = 1;
COMMIT;
```

Session 1 again:
```sql
SELECT balance FROM accounts WHERE id = 1; -- now returns 150
COMMIT;
```

### Prevent lost updates (row lock)

```sql
BEGIN;
SELECT balance FROM accounts WHERE id = 1 FOR UPDATE; -- locks the row
UPDATE accounts SET balance = balance + 10 WHERE id = 1;
COMMIT;
```

Another session trying to update the same row will wait (or error with `NOWAIT`).

## D — Durability ("committed means saved")

Once a transaction is committed, it should not be lost even if the database crashes.

### Theoretical meaning

Durability means a commit is not “just in memory.” A committed transaction should survive restarts.
It is typically implemented using logging + flushing (e.g., write-ahead log).

In PostgreSQL, durability is achieved mainly via:
- **WAL (Write-Ahead Log)**
- flushing to disk on commit (depending on settings)

### Practical note

In production, durability depends on correct configuration + reliable storage.
For example, `synchronous_commit` trades latency vs safety.

## Quick summary

- **Atomicity:** commit everything or rollback everything.
- **Consistency:** constraints/rules stay true.
- **Isolation:** concurrent transactions behave safely.
- **Durability:** committed data survives crashes.

## 1-line exam answers

- **Atomicity:** no partial commits.
- **Consistency:** constraints/invariants always hold after commit.
- **Isolation:** concurrent execution behaves like a safe schedule (ideally serial).
- **Durability:** committed data is permanent across crashes.
