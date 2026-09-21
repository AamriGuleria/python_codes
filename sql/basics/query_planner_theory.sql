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