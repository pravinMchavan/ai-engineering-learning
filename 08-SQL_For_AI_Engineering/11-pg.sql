-- Concurrency in PostgreSQL: Locks, Isolation & Transactions
-- Date: 2026-05-01
--
-- How to use this file
-- 1) Run the SETUP section once (single session).
-- 2) For each lab, open TWO psql sessions connected to the same database.
-- 3) Follow the "Session 1" and "Session 2" blocks exactly.
--
-- Notes
-- - PostgreSQL uses MVCC (Multi-Version Concurrency Control) so reads usually do NOT block writes.
-- - Locks primarily matter when multiple transactions touch the same rows/tables or explicitly request locks.

/*
============================================================
SETUP (run once)
============================================================
*/

-- Optional psql helpers:
-- \set ON_ERROR_STOP on
-- \timing on

DROP SCHEMA IF EXISTS concurrency_lab CASCADE;
CREATE SCHEMA concurrency_lab;
SET search_path = concurrency_lab;

CREATE TABLE accounts (
	id          INT PRIMARY KEY,
	owner       TEXT NOT NULL,
	balance     INT  NOT NULL CHECK (balance >= 0),
	updated_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

INSERT INTO accounts (id, owner, balance) VALUES
	(1, 'Alice', 100),
	(2, 'Bob',   100),
	(3, 'Cara',  100);

-- A simple "queue" table to demonstrate SKIP LOCKED patterns
CREATE TABLE jobs (
	id          BIGSERIAL PRIMARY KEY,
	payload     TEXT NOT NULL,
	status      TEXT NOT NULL DEFAULT 'ready' CHECK (status IN ('ready', 'processing', 'done')),
	created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

INSERT INTO jobs (payload) VALUES
	('job-1'), ('job-2'), ('job-3'), ('job-4');

-- Useful baseline
SELECT * FROM accounts ORDER BY id;
SELECT * FROM jobs ORDER BY id;


/*
============================================================
LAB 0 — Transaction basics (COMMIT / ROLLBACK / SAVEPOINT)
============================================================
*/

-- Session 1
-- BEGIN;
-- UPDATE accounts SET balance = balance + 10, updated_at = now() WHERE id = 1;
-- SELECT * FROM accounts WHERE id = 1;
-- ROLLBACK;
-- SELECT * FROM accounts WHERE id = 1;

-- Session 1 (savepoint)
-- BEGIN;
-- UPDATE accounts SET balance = balance + 10, updated_at = now() WHERE id = 1;
-- SAVEPOINT s1;
-- UPDATE accounts SET balance = balance + 10, updated_at = now() WHERE id = 1;
-- ROLLBACK TO SAVEPOINT s1;
-- COMMIT;
-- SELECT * FROM accounts WHERE id = 1;


/*
============================================================
LAB 1 — MVCC visibility (reads don't block writes)
============================================================
*/

-- Goal: see how each statement sees committed data at statement start (READ COMMITTED).
--
-- Session 1
-- BEGIN;
-- SELECT balance FROM accounts WHERE id = 1;  -- expect 100
-- (do not commit)
--
-- Session 2
-- UPDATE accounts SET balance = balance + 50, updated_at = now() WHERE id = 1;
-- COMMIT;  -- implicit commit if autocommit
--
-- Session 1
-- SELECT balance FROM accounts WHERE id = 1;  -- in READ COMMITTED, now sees 150
-- COMMIT;


/*
============================================================
LAB 2 — Row locks with SELECT ... FOR UPDATE
============================================================
*/

-- Session 1
-- BEGIN;
-- SELECT * FROM accounts WHERE id = 2 FOR UPDATE; -- row lock on id=2
-- (keep transaction open)
--
-- Session 2 (this will block until Session 1 commits/rolls back)
-- BEGIN;
-- UPDATE accounts SET balance = balance + 1, updated_at = now() WHERE id = 2;
--
-- Session 2 (avoid waiting)
-- UPDATE accounts SET balance = balance + 1, updated_at = now() WHERE id = 2;
-- -- If you want NOWAIT explicitly:
-- SELECT * FROM accounts WHERE id = 2 FOR UPDATE NOWAIT;
--
-- Session 1
-- COMMIT;
--
-- Session 2
-- COMMIT;

-- Variants (brief):
-- FOR NO KEY UPDATE: weaker than FOR UPDATE, allows some concurrent FK operations
-- FOR SHARE / FOR KEY SHARE: shared row locks (commonly used by FK checks)


/*
============================================================
LAB 3 — SKIP LOCKED for queue consumers
============================================================
*/

-- This is a common pattern for job queues: each worker locks one "ready" job.
--
-- Session 1 (worker A)
-- BEGIN;
-- WITH next_job AS (
--     SELECT id
--     FROM jobs
--     WHERE status = 'ready'
--     ORDER BY id
--     FOR UPDATE SKIP LOCKED
--     LIMIT 1
-- )
-- UPDATE jobs j
-- SET status = 'processing'
-- FROM next_job
-- WHERE j.id = next_job.id
-- RETURNING j.*;
--
-- (keep transaction open to keep the lock)
--
-- Session 2 (worker B) - should pick a different row, not block
-- BEGIN;
-- WITH next_job AS (
--     SELECT id
--     FROM jobs
--     WHERE status = 'ready'
--     ORDER BY id
--     FOR UPDATE SKIP LOCKED
--     LIMIT 1
-- )
-- UPDATE jobs j
-- SET status = 'processing'
-- FROM next_job
-- WHERE j.id = next_job.id
-- RETURNING j.*;
--
-- Session 1
-- COMMIT;
-- Session 2
-- COMMIT;


/*
============================================================
LAB 4 — Table locks (LOCK TABLE)
============================================================
*/

-- Table locks are stronger and conflict more easily than row locks.
--
-- Session 1
-- BEGIN;
-- LOCK TABLE accounts IN SHARE MODE;
-- (keep open)
--
-- Session 2 (may block depending on lock mode)
-- BEGIN;
-- ALTER TABLE accounts ADD COLUMN note TEXT; -- needs ACCESS EXCLUSIVE, will block
--
-- Session 1
-- COMMIT;


/*
============================================================
LAB 5 — Debug blocking: pg_stat_activity + pg_locks
============================================================
*/

-- Run this in ANY session to see who is blocking whom.
-- Tip: run it while a statement is "stuck".

SELECT
	a.pid,
	a.usename,
	a.state,
	a.wait_event_type,
	a.wait_event,
	a.query_start,
	now() - a.query_start AS running_for,
	a.query
FROM pg_stat_activity a
WHERE a.datname = current_database()
ORDER BY a.query_start NULLS LAST;

-- Locks summary
SELECT
	l.pid,
	l.locktype,
	l.mode,
	l.granted,
	l.relation::regclass AS relation,
	a.state,
	a.wait_event_type,
	a.wait_event,
	a.query
FROM pg_locks l
JOIN pg_stat_activity a ON a.pid = l.pid
WHERE a.datname = current_database()
ORDER BY l.granted, l.pid;

-- Identify blockers for blocked backends
SELECT
	blocked.pid AS blocked_pid,
	blocked.query AS blocked_query,
	blocker.pid AS blocker_pid,
	blocker.query AS blocker_query
FROM pg_stat_activity blocked
JOIN pg_stat_activity blocker
  ON blocker.pid = ANY (pg_blocking_pids(blocked.pid))
WHERE blocked.datname = current_database();


/*
============================================================
LAB 6 — Isolation levels: READ COMMITTED vs REPEATABLE READ
============================================================
*/

-- READ COMMITTED (default): each statement sees a fresh snapshot of committed data.
--
-- Session 1
-- BEGIN;
-- SHOW transaction_isolation; -- read committed
-- SELECT SUM(balance) AS total FROM accounts; -- suppose 300
--
-- Session 2
-- UPDATE accounts SET balance = balance + 100, updated_at = now() WHERE id = 3;
--
-- Session 1
-- SELECT SUM(balance) AS total FROM accounts; -- sees changed total in same transaction
-- COMMIT;

-- REPEATABLE READ: one snapshot for the whole transaction.
--
-- Session 1
-- BEGIN ISOLATION LEVEL REPEATABLE READ;
-- SHOW transaction_isolation; -- repeatable read
-- SELECT SUM(balance) AS total FROM accounts;
--
-- Session 2
-- UPDATE accounts SET balance = balance + 100, updated_at = now() WHERE id = 1;
--
-- Session 1
-- SELECT SUM(balance) AS total FROM accounts; -- unchanged within this transaction
--
-- If Session 1 tries to UPDATE a row changed after its snapshot,
-- PostgreSQL can raise: "could not serialize access due to concurrent update".
-- Example in Session 1:
-- UPDATE accounts SET balance = balance + 1, updated_at = now() WHERE id = 1;
-- COMMIT;


/*
============================================================
LAB 7 — SERIALIZABLE and write skew (one will fail)
============================================================
*/

-- Setup a classic write-skew example: at least one doctor must be "on_call".
DROP TABLE IF EXISTS on_call;
CREATE TABLE on_call (
	doctor TEXT PRIMARY KEY,
	on_call BOOLEAN NOT NULL
);

INSERT INTO on_call (doctor, on_call) VALUES
	('DrA', TRUE),
	('DrB', TRUE);

-- Session 1
-- BEGIN ISOLATION LEVEL SERIALIZABLE;
-- SELECT COUNT(*) FROM on_call WHERE on_call = TRUE; -- returns 2
-- UPDATE on_call SET on_call = FALSE WHERE doctor = 'DrA';
-- (do not commit yet)
--
-- Session 2
-- BEGIN ISOLATION LEVEL SERIALIZABLE;
-- SELECT COUNT(*) FROM on_call WHERE on_call = TRUE; -- also returns 2
-- UPDATE on_call SET on_call = FALSE WHERE doctor = 'DrB';
-- COMMIT; -- one of the commits (S1 or S2) should fail with serialization_failure
--
-- Session 1
-- COMMIT;
--
-- If a transaction fails under SERIALIZABLE, the correct app behavior is: ROLLBACK and retry.


/*
============================================================
LAB 8 — Deadlocks (PostgreSQL detects & aborts one)
============================================================
*/

-- Session 1
-- BEGIN;
-- SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
-- (keep open)
--
-- Session 2
-- BEGIN;
-- SELECT * FROM accounts WHERE id = 2 FOR UPDATE;
--
-- Session 1
-- SELECT * FROM accounts WHERE id = 2 FOR UPDATE; -- waits
--
-- Session 2
-- SELECT * FROM accounts WHERE id = 1 FOR UPDATE; -- causes deadlock; PostgreSQL aborts one txn
--
-- After the deadlock error, the aborted session must ROLLBACK.


/*
============================================================
LAB 9 — Advisory locks (application-level locking)
============================================================
*/

-- Advisory locks are not tied to a table row; you pick a key.
-- Common use: ensure only one worker runs a critical job.
--
-- Session 1
-- SELECT pg_advisory_lock(42); -- holds until session ends or unlock
--
-- Session 2 (blocks)
-- SELECT pg_advisory_lock(42);
--
-- Session 1
-- SELECT pg_advisory_unlock(42);

-- Non-blocking attempt
-- SELECT pg_try_advisory_lock(42); -- returns true/false


/*
============================================================
Practical guidelines (quick)
============================================================
*/

-- 1) Keep transactions short.
-- 2) Lock rows in a consistent order to avoid deadlocks.
-- 3) Prefer row locks (SELECT ... FOR UPDATE) over table locks.
-- 4) For job queues, use SKIP LOCKED.
-- 5) Under REPEATABLE READ / SERIALIZABLE, be prepared to retry on serialization failures.