-- Sequential scan vs Index scan
-- Sequential scan (Seq Scan): read every row in the table, check each against the filter. O(n) — fine for small tables, or when you're going to need most of the rows anyway.
-- Index scan: use an index to jump directly to matching rows, then fetch each from the table. Much faster when you're filtering down to a small fraction of rows.
-- Index-only scan: the index itself contains all the columns you asked for, so Postgres doesn't even need to touch the table. Fastest option, but requires the index to "cover" your query.


EXPLAIN SELECT * FROM orders WHERE status = 'pending';
Seq Scan on orders  (cost=0.00..1834.00 rows=9500 width=48)
  Filter: (status = 'pending'::text)


EXPLAIN ANALYZE SELECT * FROM orders WHERE status = 'pending';
Seq Scan on orders (cost=0.00..1834.00 rows=9500 width=48)
                    (actual time=0.02..15.4 rows=200 loops=1)
  Filter: (status = 'pending'::text)
  Rows Removed by Filter: 49800



-- VACUUM
-- Postgres uses MVCC (multi-version concurrency control) — when you UPDATE or DELETE a row, the old version isn't immediately erased; it's marked dead so other in-progress transactions can still see the old version if needed. Over time, dead rows accumulate as bloat, wasting space and slowing scans (Postgres still has to skip past them).
-- VACUUM reclaims that dead space for reuse (it doesn't usually shrink the file on disk — VACUUM FULL does, but locks the table).
VACUUM orders;


-- Postgres runs this automatically via autovacuum in the background, but heavy-write tables can outpace it, causing bloat and slow queries until it catches up or you tune autovacuum settings.
