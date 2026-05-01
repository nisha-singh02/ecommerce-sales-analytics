-- 1. Monthly Revenue Trend
SELECT 
    DATE_TRUNC('month', order_date) AS month,
    SUM(sales) AS total_revenue,
    SUM(profit) AS total_profit
FROM sales
GROUP BY month
ORDER BY month;


-- 2. Top 10 Customers by Revenue
SELECT 
    customer_name,
    SUM(sales) AS total_spent,
    COUNT(order_id) AS total_orders
FROM sales
GROUP BY customer_name
ORDER BY total_spent DESC
LIMIT 10;


-- 3. Region-wise Performance
SELECT 
    region,
    SUM(sales) AS total_revenue,
    SUM(profit) AS total_profit,
    COUNT(order_id) AS total_orders
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;


-- 4. Category & Sub-Category Profitability
SELECT 
    category,
    sub_category,
    SUM(sales) AS revenue,
    SUM(profit) AS profit
FROM sales
GROUP BY category, sub_category
ORDER BY profit DESC;


-- 5. Top 5 Loss-Making Products (IMPORTANT INSIGHT)
SELECT 
    product_name,
    SUM(profit) AS total_loss
FROM sales
GROUP BY product_name
HAVING SUM(profit) < 0
ORDER BY total_loss ASC
LIMIT 5;


-- 6. Repeat Customers (Customer Retention Insight)
SELECT 
    customer_name,
    COUNT(order_id) AS total_orders,
    SUM(sales) AS total_spent
FROM sales
GROUP BY customer_name
HAVING COUNT(order_id) > 5
ORDER BY total_orders DESC;


-- 7. Discount Impact on Profit
SELECT 
    ROUND(discount, 2) AS discount_rate,
    SUM(sales) AS revenue,
    SUM(profit) AS profit
FROM sales
GROUP BY discount_rate
ORDER BY discount_rate;


-- 8. Sales by Segment
SELECT 
    segment,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY segment
ORDER BY total_sales DESC;


-- 9. Yearly Growth Analysis
SELECT 
    EXTRACT(YEAR FROM order_date) AS year,
    SUM(sales) AS yearly_sales,
    SUM(profit) AS yearly_profit
FROM sales
GROUP BY year
ORDER BY year;


-- 10. Average Order Value (AOV)
SELECT 
    ROUND(SUM(sales) / COUNT(DISTINCT order_id), 2) AS avg_order_value
FROM sales;