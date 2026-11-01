-- Financial Performance | Table: financials
SELECT business_unit, SUM(revenue) AS revenue, SUM(expenses) AS expenses,
 SUM(revenue-expenses) AS operating_profit,
 SUM(revenue-budget_revenue) AS budget_variance
FROM financials GROUP BY business_unit ORDER BY revenue DESC;
SELECT month, SUM(revenue) AS revenue, SUM(expenses) AS expenses
FROM financials GROUP BY month ORDER BY month;