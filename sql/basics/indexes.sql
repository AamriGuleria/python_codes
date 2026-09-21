-- GIN INDEX
-- Searching inside JSONB
CREATE INDEX idx_orders_metadata ON orders USING GIN (metadata jsonb_path_ops)

-- Full text search
CREATE INDEX idx_full_text ON products USING GIN (to_tsvector('english',description))


-- composite index
CREATE INDEX idx_orders_customer_status ON orders(customer_id, status);

--  partial indexing
CREATE INDEX idx_orders_pending ON orders(created_at) WHERE status = 'pending';