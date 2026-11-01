# Financial Performance: Excel & Power BI Guide

This guide complements the CSV dataset and Python starter script in this repository.

## Excel workflow
Add `Operating Profit = [@revenue]-[@expenses]` and `Budget Variance = [@revenue]-[@budget_revenue]`. Pivot by month and business unit.

## Power BI dashboard
 Measures:
```DAX
Revenue = SUM(financials[revenue])
Expenses = SUM(financials[expenses])
Operating Profit = [Revenue]-[Expenses]
Budget Variance = [Revenue]-SUM(financials[budget_revenue])
Profit Margin = DIVIDE([Operating Profit],[Revenue])
```
Dashboard: revenue, expenses, profit and variance cards; revenue vs expenses trend; profit by business unit; month/unit slicers.

## Import and modelling notes
1. In Power BI Desktop choose **Get Data → Text/CSV** and select `data/dataset.csv`.
2. Rename the imported table to the name used in the DAX measures in this guide.
3. Check data types (dates as Date, counts and amounts as Whole/Decimal Number).
4. Create the measures from **Modeling → New measure**.
5. Add the suggested visuals and slicers; save your work as `dashboard.pbix` in this repository when finished.

**Important:** The supplied datasets are small synthetic practice samples. Validate field names and data types after import. The PBIX dashboard must be created and saved in Power BI Desktop; this guide does not claim a PBIX file is already included.
