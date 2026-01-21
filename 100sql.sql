-- SCHEMA & SAMPLE DATA (keeps your original structure for context)
CREATE TABLE customer_master (
    customer_id     INT PRIMARY KEY,
    customer_name   VARCHAR(100),
    email           VARCHAR(100),
    phone_number    VARCHAR(20),
    join_date       DATE
);

CREATE TABLE product_master (
    product_id      INT PRIMARY KEY,
    product_name    VARCHAR(100),
    brand_name      VARCHAR(50),
    category        VARCHAR(50),
    mrp_price       DECIMAL(10,2),
    selling_price   DECIMAL(10,2)
);

CREATE TABLE store_master (
    store_id        INT PRIMARY KEY,
    store_name      VARCHAR(100),
    city            VARCHAR(50),
    region          VARCHAR(50)
);

CREATE TABLE sales_transaction_header (
    transaction_id      INT PRIMARY KEY,
    transaction_date    DATE NOT NULL,
    customer_id         INT,
    store_id            INT,
    total_amount        DECIMAL(10,2),
    total_tax_amount    DECIMAL(10,2),
    discount_amount     DECIMAL(10,2),
    net_payable_amount  DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customer_master(customer_id),
    FOREIGN KEY (store_id) REFERENCES store_master(store_id)
);

CREATE TABLE sales_transaction_items (
    transaction_item_id INT PRIMARY KEY,
    transaction_id      INT,
    product_id          INT,
    quantity            INT,
    unit_price          DECIMAL(10,2),
    discount_amount     DECIMAL(10,2),
    tax_amount          DECIMAL(10,2),
    line_total_amount   DECIMAL(10,2),
    FOREIGN KEY (transaction_id) REFERENCES sales_transaction_header(transaction_id),
    FOREIGN KEY (product_id) REFERENCES product_master(product_id)
);

CREATE TABLE sales_payments (
    payment_id      INT PRIMARY KEY,
    transaction_id  INT,
    payment_mode    VARCHAR(20),
    amount_paid     DECIMAL(10,2),
    FOREIGN KEY (transaction_id) REFERENCES sales_transaction_header(transaction_id)
);

CREATE TABLE sales_returns (
    return_id       INT PRIMARY KEY,
    transaction_id  INT,
    product_id      INT,
    return_date     DATE,
    return_quantity INT,
    refund_amount   DECIMAL(10,2),
    FOREIGN KEY (transaction_id) REFERENCES sales_transaction_header(transaction_id),
    FOREIGN KEY (product_id) REFERENCES product_master(product_id)
);


-- (your INSERTs omitted here for brevity — assume your sample data is already loaded)

--------------------------------------------------------------------------------
-- Q1. List all customers.
SELECT * FROM customer_master

--------------------------------------------------------------------------------
-- Q2. Display all products with brand and category.
SELECT brand_name, category FROM product_master

--------------------------------------------------------------------------------
-- Q3. Show all transactions with customer names.
SELECT c.customer_name, s.transaction_id
FROM customer_master c
JOIN sales_transaction_header s
ON c.customer_id = s.customer_id

--------------------------------------------------------------------------------
-- Q4. List items with product names and prices.
SELECT product_name, mrp_price, selling_price
FROM product_master

--------------------------------------------------------------------------------
-- Q5. Find total quantity sold per product.
-- (your verified query)
SELECT p.product_id, p.product_name, p.brand_name,
       SUM(s.quantity) AS total_quantity_sold
FROM product_master p
LEFT JOIN sales_transaction_items s
  ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name, p.brand_name

--------------------------------------------------------------------------------
-- Q6. Find total revenue per store.
SELECT s1.store_id, SUM(s2.net_payable_amount) AS total_revenue
FROM store_master s1
JOIN sales_transaction_header s2
  ON s1.store_id = s2.store_id
GROUP BY s1.store_id

--------------------------------------------------------------------------------
-- Q7. Display transaction count per customer.
SELECT customer_id, COUNT(customer_id) AS total_transaction
FROM sales_transaction_header
GROUP BY customer_id

--------------------------------------------------------------------------------
-- Q8. Find products sold in each store.
-- 


--------------------------------------------------------------------------------
-- Q9. Show customers who made purchases.
SELECT *
FROM customer_master
WHERE customer_id IN (
    SELECT DISTINCT customer_id FROM sales_transaction_header
);

--------------------------------------------------------------------------------
-- Q10. List customers who have returns (customers with at least one return).
SELECT DISTINCT c.customer_id, c.customer_name
FROM customer_master c
JOIN sales_transaction_header s ON c.customer_id = s.customer_id
JOIN sales_returns r ON s.transaction_id = r.transaction_id

--------------------------------------------------------------------------------
-- Q11. Products that were both sold and returned.
SELECT *
FROM product_master
WHERE product_id IN (SELECT product_id FROM sales_transaction_items)
  AND product_id IN (SELECT product_id FROM sales_returns)

--------------------------------------------------------------------------------
-- Q12. Total spend of each customer.
SELECT c.customer_id, c.customer_name,
       SUM(s.net_payable_amount) AS total_spent
FROM customer_master c
JOIN sales_transaction_header s
  ON c.customer_id = s.customer_id
GROUP BY c.customer_id, c.customer_name

--------------------------------------------------------------------------------
-- Q13. Highest spending customer.
SELECT c.customer_id, c.customer_name, SUM(s.net_payable_amount) AS total_spent
FROM customer_master c
JOIN sales_transaction_header s
  ON c.customer_id = s.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_spent DESC
LIMIT 1;

--------------------------------------------------------------------------------
-- Q14. Store with highest revenue.
SELECT s1.store_id, s1.store_name, SUM(s2.net_payable_amount) AS total_amount
FROM store_master s1
JOIN sales_transaction_header s2
  ON s1.store_id = s2.store_id
GROUP BY s1.store_id, s1.store_name
ORDER BY total_amount DESC
LIMIT 1;

--------------------------------------------------------------------------------
-- Q15. Count distinct products sold (distinct brands shown in your sample).
SELECT DISTINCT p.brand_name
FROM product_master p
JOIN sales_transaction_items s ON p.product_id = s.product_id;

--------------------------------------------------------------------------------
-- Q16. Total returned products per store.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q17. Count transactions per payment mode.
SELECT payment_mode, COUNT(payment_mode) AS payment_mode_count
FROM sales_payments
GROUP BY payment_mode;

--------------------------------------------------------------------------------
-- Q18. Revenue by brand.
select brand_name,sum(quantity * selling_price) from product_master p
join sales_transaction_items s
on p.product_id = s.product_id group by brand_name

--------------------------------------------------------------------------------
-- Q19. Revenue per customer per store.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q20. Product revenue contribution %.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q21. Customers who made at least one purchase.
SELECT customer_id, customer_name
FROM customer_master
WHERE customer_id IN (
    SELECT DISTINCT customer_id FROM sales_transaction_header
);

--------------------------------------------------------------------------------
-- Q22. Customers who never purchased.
SELECT customer_id, customer_name
FROM customer_master
WHERE customer_id NOT IN (
    SELECT DISTINCT customer_id FROM sales_transaction_header
);

--------------------------------------------------------------------------------
-- Q23. Products never sold.
SELECT *
FROM product_master
WHERE product_id NOT IN (
    SELECT DISTINCT product_id FROM sales_transaction_items
);

--------------------------------------------------------------------------------
-- Q24. Stores having sales > average store revenue.
-- (write your answer here)


--------------------------------------------------------------------------------
-- Q25. Customers whose spend > global avg spend.
-- (verified CTE version you provided — using total_amount)
WITH cte_name AS (
    SELECT customer_id, SUM(total_amount) AS total_spent
    FROM sales_transaction_header
    GROUP BY customer_id
)
SELECT c.customer_id, c.customer_name
FROM customer_master c
WHERE c.customer_id IN (
    SELECT customer_id
    FROM cte_name
    WHERE total_spent > (SELECT AVG(total_amount) FROM sales_transaction_header)
);

--------------------------------------------------------------------------------
-- Q26. Products priced above avg selling price.
SELECT *
FROM product_master
WHERE selling_price > (SELECT AVG(selling_price) FROM product_master);

--------------------------------------------------------------------------------
-- Q27. Products priced below brand avg.
SELECT *
FROM product_master p1
WHERE selling_price < (
    SELECT AVG(selling_price)
    FROM product_master p2
    WHERE p1.brand_name = p2.brand_name
);

--------------------------------------------------------------------------------
-- Q28. Cheapest product.
SELECT *
FROM product_master
WHERE selling_price = (SELECT MIN(selling_price) FROM product_master);

--------------------------------------------------------------------------------
-- Q29. Costliest product.
SELECT *
FROM product_master
WHERE selling_price = (SELECT MAX(selling_price) FROM product_master);

--------------------------------------------------------------------------------
-- Q30. Transactions where items > avg item count.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q31. Products with return > avg returns.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q32. Product appearing in most bills.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q33. Store with highest avg bill.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q34. Customers whose spend > avg spend.
-- (write your answer here)


--------------------------------------------------------------------------------
-- Q35. Only CASH paying customers.
SELECT customer_name
FROM customer_master
WHERE customer_id IN (
    SELECT customer_id
    FROM sales_transaction_header
    WHERE transaction_id IN (
        SELECT transaction_id
        FROM sales_payments
        WHERE payment_mode = 'CASH'
    )
);

--------------------------------------------------------------------------------
-- Q36. Products bought only once.
-- (your verified query using SUM(quantity) = 1)
SELECT *
FROM product_master p
WHERE p.product_id IN (
    SELECT product_id
    FROM sales_transaction_items
    GROUP BY product_id
    HAVING SUM(quantity) = 1
);

--------------------------------------------------------------------------------
-- Q37. Customers who purchased only once.
-- (write your answer here)
select s.customer_id,c.customer_name from customer_master c join sales_transaction_header s
on c.customer_id = s.customer_id group by s.customer_id,c.customer_name
having count(s.customer_id)=1

--------------------------------------------------------------------------------
-- Q38. Transactions with discount > avg discount.
-- (write your answer here)


--------------------------------------------------------------------------------
-- Q39. Brand with highest total sale.
-- (write your answer here)
select brand_name,sum(quantity * selling_price) as amount_sale from product_master p 
join sales_transaction_items s on
p.product_id = s.product_id group by p.brand_name order by amount_sale desc 
limit 1

--------------------------------------------------------------------------------
-- Q40. Products above category avg price.
SELECT *
FROM product_master p1
WHERE p1.selling_price > (
    SELECT AVG(selling_price)
    FROM product_master p2
    WHERE p1.category = p2.category
);

--------------------------------------------------------------------------------
-- Q41. Customers spending > 80% customers.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q42. Product qty sold > avg product qty.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q43. Last purchase > avg last purchase.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q44. Customers whose every bill > avg bill.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q45. Products discounted > avg discount count.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q46. Selling price > category avg.  -- (duplicate of Q40)
SELECT *
FROM product_master p1
WHERE p1.selling_price > (
    SELECT AVG(selling_price)
    FROM product_master p2
    WHERE p1.category = p2.category
);

--------------------------------------------------------------------------------
-- Q47. Tax > avg same-day tax.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q48. Return count > sale count.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q49. Stores having more returns than 50% stores.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q50. Only-UPI customers.
SELECT customer_name
FROM customer_master
WHERE customer_id IN (
    SELECT customer_id
    FROM sales_transaction_header
    WHERE transaction_id IN (
        SELECT transaction_id
        FROM sales_payments
        WHERE payment_mode = 'UPI'
    )
);

--------------------------------------------------------------------------------
-- Q51. UPI > Cash customers.
-- (write your answer here)

select * from sales_payments s join 

--------------------------------------------------------------------------------
-- Q52. Revenue > 70% products.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q53. Sold without discount products.
SELECT product_id, product_name, brand_name
FROM product_master
WHERE product_id IN (
    SELECT product_id
    FROM sales_transaction_items
    WHERE discount_amount = 0
);

--------------------------------------------------------------------------------
-- Q54. Highly discounted products.
SELECT p.product_id, p.product_name, p.brand_name, s.discount_amount
FROM product_master p
JOIN sales_transaction_items s ON p.product_id = s.product_id
ORDER BY s.discount_amount DESC;

--------------------------------------------------------------------------------
-- Q55. Stores discount > global avg.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q56. Customers whose lowest bill > avg lowest bill.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q57. Customer who bought costliest item.
-- (corrected version)
SELECT c.customer_id, c.customer_name
FROM customer_master c
WHERE c.customer_id = (
    SELECT customer_id
    FROM sales_transaction_header
    ORDER BY net_payable_amount DESC
    LIMIT 1
);

--------------------------------------------------------------------------------
-- Q58. Highest tax-paying customer.
SELECT *
FROM customer_master
WHERE customer_id IN (
    SELECT customer_id
    FROM sales_transaction_header
    ORDER BY total_tax_amount DESC
    LIMIT 1
);

--------------------------------------------------------------------------------
-- Q59. Sold-always-at-MRP products.
SELECT product_id, product_name
FROM product_master
WHERE selling_price = mrp_price;

--------------------------------------------------------------------------------
-- Q60. Products never returned.
-- (write your answer here)


--------------------------------------------------------------------------------
-- Q61. Second highest selling product.
-- (write your answer here)
select product_id,product_name,selling_quantity from (
select p.product_id,p.product_name,sum(s.quantity) as selling_quantity,
ROW_NUMBER() over (order by sum(s.quantity) desc) as rn
from product_master p join
sales_transaction_items s on p.product_id = s.product_id 
group by p.product_id )
where rn = 2

--------------------------------------------------------------------------------
-- Q62. Third highest selling product.
-- (write your answer here)
select product_id,product_name,selling_quantity from
(select p.product_id,p.product_name,sum(s.quantity) as selling_quantity,
ROW_NUMBER() over (order by sum(s.quantity) desc) as rn
from product_master p join sales_transaction_items s
on p.product_id = s.product_id group by p.product_id)
where rn = 3

--------------------------------------------------------------------------------
-- Q63. Top 5 customers by spend (subquery only).
-- (write your answer here)
select customer_id, amount_spent from 
(select customer_id , sum(net_payable_amount) as amount_spent 
from sales_transaction_header group by customer_id) order by amount_spent desc
limit 3



--------------------------------------------------------------------------------
-- Q64. Products sold every month (NOT EXISTS).
-- (write your answer here)


--------------------------------------------------------------------------------
-- Q65. Sold in Jan not in Feb.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q66. Bought X not Y customers.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q67. Bought from all stores customers.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q68. One-store customers only.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q69. Most returned product.
-- (write your answer here)
select product_id,product_name from product_master where product_id in (
select product_id from (
select product_id,count(product_id) as returned_count 
from sales_returns group by product_id order by returned_count desc limit 1))


--------------------------------------------------------------------------------
-- Q70. Highest single-day selling item.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q71. Most discounted category.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q72. Low return products.
-- (write your answer here)
select product_id,product_name from product_master where product_id in (
select product_id from (
select product_id,count(*) as returned_count 
from sales_returns group by product_id order by returned_count asc limit 1))

--------------------------------------------------------------------------------
-- Q73. Increasing sale month by month.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q74. New high demand product.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q75. Discount-only buyers.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q76. Active last month not this month.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q77. High-value transaction detection.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q78. Fake return refund > sale.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q79. Region avg sale > global avg.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q80. High spend + high return customers.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q81. Most common first product.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q82. Products bought together frequently.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q83. Only-discount purchase customers.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q84. Small frequent buyers.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q85. Highest tax revenue product.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q86. Loss-sale products.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q87. UPI% > Cash% store.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q88. Brand highest avg billing.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q89. Category for only top spenders.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q90. Most refunded brand.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q91. Returns after 30+ days.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q92. Stores return% > 40%.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q93. Month-end buyers only.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q94. Repeated low-selling products.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q95. High discount → low revenue.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q96. Loyal customers (10+ bills, 2 stores, no return).
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q97. Refund > Total purchase customers.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q98. Demand spike items.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q99. Customer fall month.
-- (write your answer here)

--------------------------------------------------------------------------------
-- Q100. VIP Filter (Spend > 3×avg, No return, 10+ txn, 2 stores)
-- (write your answer here)
