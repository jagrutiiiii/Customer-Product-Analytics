-- ============================================================
-- CUSTOMER & PRODUCT ANALYTICS
-- SQL BUSINESS ANALYSIS
-- ============================================================

USE customer_product_analysis;


-- ============================================================
-- 1. OVERALL BUSINESS PERFORMANCE
-- ============================================================

SELECT
    COUNT(*) AS total_sessions,
    COUNT(DISTINCT customer_id) AS unique_customers,
    SUM(purchased) AS total_purchases,
    SUM(revenue) AS total_revenue,
    SUM(quantity) AS total_quantity_sold,
    ROUND(SUM(revenue) / NULLIF(SUM(purchased), 0), 2) AS average_order_value
FROM ecommerce;


-- ============================================================
-- 2. MONTHLY REVENUE
-- ============================================================

SELECT
    `month`,
    month_name,
    ROUND(SUM(revenue), 2) AS monthly_revenue
FROM ecommerce
GROUP BY `month`, month_name
ORDER BY `month`;


-- ============================================================
-- 3. TOP 10 CUSTOMERS BY REVENUE
-- ============================================================

SELECT
    customer_id,
    ROUND(SUM(revenue), 2) AS total_revenue,
    SUM(purchased) AS purchases,
    COUNT(*) AS sessions
FROM ecommerce
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT 10;


-- ============================================================
-- 4. REPEAT VS ONE-TIME CUSTOMERS
-- ============================================================

SELECT
    customer_type,
    COUNT(*) AS customers,
    ROUND(SUM(total_revenue), 2) AS total_revenue,
    ROUND(AVG(total_revenue), 2) AS average_revenue_per_customer
FROM (
    SELECT
        customer_id,
        MAX(customer_type) AS customer_type,
        SUM(revenue) AS total_revenue
    FROM ecommerce
    GROUP BY customer_id
) AS customer_summary
GROUP BY customer_type
ORDER BY total_revenue DESC;


-- ============================================================
-- 5. CUSTOMER SEGMENT PERFORMANCE
-- ============================================================

SELECT
    customer_segment,
    COUNT(*) AS customers,
    ROUND(SUM(total_revenue), 2) AS total_revenue,
    ROUND(AVG(total_revenue), 2) AS average_revenue_per_customer
FROM (
    SELECT
        customer_id,
        MAX(customer_segment) AS customer_segment,
        SUM(revenue) AS total_revenue
    FROM ecommerce
    GROUP BY customer_id
) AS customer_summary
GROUP BY customer_segment
ORDER BY total_revenue DESC;


-- ============================================================
-- 6. REVENUE BY PRODUCT CATEGORY
-- ============================================================

SELECT
    product_category,
    ROUND(SUM(revenue), 2) AS total_revenue,
    SUM(quantity) AS total_quantity_sold,
    SUM(purchased) AS purchases
FROM ecommerce
GROUP BY product_category
ORDER BY total_revenue DESC;


-- ============================================================
-- 7. TOP 10 PRODUCTS BY REVENUE
-- ============================================================

SELECT
    product_id,
    ROUND(SUM(revenue), 2) AS total_revenue,
    SUM(quantity) AS quantity_sold,
    SUM(purchased) AS purchases
FROM ecommerce
GROUP BY product_id
ORDER BY total_revenue DESC
LIMIT 10;


-- ============================================================
-- 8. QUANTITY SOLD BY PRODUCT CATEGORY
-- ============================================================

SELECT
    product_category,
    SUM(quantity) AS total_quantity_sold,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM ecommerce
GROUP BY product_category
ORDER BY total_quantity_sold DESC;


-- ============================================================
-- 9. CONVERSION RATE BY MARKETING CHANNEL
-- ============================================================

SELECT
    marketing_channel,
    COUNT(*) AS total_sessions,
    SUM(purchased) AS purchases,
    ROUND(
        SUM(purchased) * 100.0 / NULLIF(COUNT(*), 0),
        2
    ) AS conversion_rate_percent,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM ecommerce
GROUP BY marketing_channel
ORDER BY conversion_rate_percent DESC;


-- ============================================================
-- 10. CONVERSION RATE BY DEVICE
-- ============================================================

SELECT
    device_type,
    COUNT(*) AS total_sessions,
    SUM(purchased) AS purchases,
    ROUND(
        SUM(purchased) * 100.0 / NULLIF(COUNT(*), 0),
        2
    ) AS conversion_rate_percent,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM ecommerce
GROUP BY device_type
ORDER BY conversion_rate_percent DESC;


-- ============================================================
-- 11. CART ABANDONMENT
-- ============================================================

SELECT
    SUM(added_to_cart) AS cart_additions,
    SUM(cart_abandoned) AS abandoned_carts,
    ROUND(
        SUM(cart_abandoned) * 100.0 /
        NULLIF(SUM(added_to_cart), 0),
        2
    ) AS cart_abandonment_rate_percent
FROM ecommerce;


-- ============================================================
-- 12. REVENUE BY DISCOUNT CATEGORY
-- ============================================================

SELECT
    discount_category,
    COUNT(*) AS sessions,
    SUM(purchased) AS purchases,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(
        SUM(purchased) * 100.0 /
        NULLIF(COUNT(*), 0),
        2
    ) AS conversion_rate_percent
FROM ecommerce
GROUP BY discount_category
ORDER BY total_revenue DESC;


-- ============================================================
-- 13. PAYMENT METHOD PERFORMANCE
-- ============================================================

SELECT
    payment_method,
    COUNT(*) AS transactions,
    SUM(purchased) AS purchases,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM ecommerce
GROUP BY payment_method
ORDER BY total_revenue DESC;


-- ============================================================
-- 14. REVENUE PER SESSION
-- ============================================================

SELECT
    ROUND(SUM(revenue) / COUNT(*), 2) AS revenue_per_session
FROM ecommerce;


-- ============================================================
-- 15. MONTHLY PURCHASE PERFORMANCE
-- ============================================================

SELECT
    `month`,
    month_name,
    COUNT(*) AS total_sessions,
    SUM(purchased) AS purchases,
    ROUND(
        SUM(purchased) * 100.0 /
        NULLIF(COUNT(*), 0),
        2
    ) AS conversion_rate_percent,
    ROUND(SUM(revenue), 2) AS revenue
FROM ecommerce
GROUP BY `month`, month_name
ORDER BY `month`;

