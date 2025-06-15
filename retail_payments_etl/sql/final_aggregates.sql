SELECT
    c.product_id,
    p.product_name,
    SUM(c.amount) as total_revenue,
    COUNT(*) as transaction_count
FROM cleansed_transactions c
JOIN product_catalog p ON c.product_id = p.product_id
GROUP BY c.product_id, p.product_name
ORDER BY total_revenue DESC;
