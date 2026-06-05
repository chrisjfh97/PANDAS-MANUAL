# Complete pandas Manual: Practical Data Analysis, SQL, Statistics, and Plotting

---

## Table of Contents

### [Part I: pandas Fundamentals and Workflow](#part-i-pandas-fundamentals-and-workflow)

1. [How to Use This Manual](#1-how-to-use-this-manual)
2. [What pandas Is and Why It Matters](#2-what-pandas-is-and-why-it-matters)
3. [Installation and Setup](#3-installation-and-setup)
4. [Import Conventions](#4-import-conventions)
5. [Core pandas Objects](#5-core-pandas-objects)
6. [Creating DataFrames](#6-creating-dataframes)
7. [Reading and Writing Files](#7-reading-and-writing-files)
8. [Inspecting Data](#8-inspecting-data)
9. [Selecting Columns and Rows](#9-selecting-columns-and-rows)
10. [Filtering Data](#10-filtering-data)
11. [Creating, Updating, and Removing Columns](#11-creating-updating-and-removing-columns)
12. [Index Basics](#12-index-basics)
13. [Sorting and Ranking](#13-sorting-and-ranking)
14. [Handling Missing Data](#14-handling-missing-data)
15. [Data Types and Type Conversion](#15-data-types-and-type-conversion)
16. [String/Text Operations](#16-stringtext-operations)
17. [Date and Time Operations](#17-date-and-time-operations)
18. [Conditional Logic in pandas](#18-conditional-logic-in-pandas)
19. [Apply, Map, Replace, and Vectorization](#19-apply-map-replace-and-vectorization)
20. [Grouping and Aggregation](#20-grouping-and-aggregation)
21. [Pivot Tables and Cross Tabs](#21-pivot-tables-and-cross-tabs)
22. [Reshaping Data](#22-reshaping-data)
23. [Combining DataFrames](#23-combining-dataframes)
24. [Duplicates and Data Quality Checks](#24-duplicates-and-data-quality-checks)
25. [Working with Excel Reports](#25-working-with-excel-reports)

### [Part II: Statistics](#part-ii-statistics)

26. [Basic Statistics with pandas](#26-basic-statistics-with-pandas)
27. [Statistics Interpretation Guide](#27-statistics-interpretation-guide)

### [Part III: Charts and Plots](#part-iii-charts-and-plots)

28. [Charts for Understanding Statistics](#28-charts-for-understanding-statistics)
29. [Plotting with pandas and Matplotlib](#29-plotting-with-pandas-and-matplotlib)
30. [How to Read Common Plot Types](#30-how-to-read-common-plot-types)

### [Part IV: Applied pandas and Reference](#part-iv-applied-pandas-and-reference)

31. [Practical Orders and Inventory Example](#31-practical-orders-and-inventory-example)
32. [Method Chaining](#32-method-chaining)
33. [Performance Tips](#33-performance-tips)
34. [Additional pandas Operations](#34-additional-pandas-operations)
35. [MultiIndex and Hierarchical Data](#35-multiindex-and-hierarchical-data)
36. [Cumulative, Rolling, and Window Calculations](#36-cumulative-rolling-and-window-calculations)
37. [Binning, Bucketing, and Segmentation](#37-binning-bucketing-and-segmentation)
38. [Working with Many Files and JSON](#38-working-with-many-files-and-json)
39. [SQL for pandas and Python Data Work](#39-sql-for-pandas-and-python-data-work)
40. [Styling Tables and Creating Review Outputs](#40-styling-tables-and-creating-review-outputs)
41. [Common Errors and How to Fix Them](#41-common-errors-and-how-to-fix-them)
42. [Mini Cheat Sheet](#42-mini-cheat-sheet)
43. [References](#43-references)

---

# Part I: pandas Fundamentals and Workflow

This part covers the core pandas workflow: creating tables, reading files, inspecting data, filtering rows, creating columns, grouping, reshaping, merging, cleaning, and exporting reports.

---

# 1. How to Use This Manual

This manual is designed to be both a learning guide and a practical reference.

Each important pandas topic includes:

- What the concept means.
- Why it matters.
- A realistic example.
- How to interpret the result.
- Common mistakes to avoid.

You can read it from top to bottom, or you can jump directly to the section you need.

The manual is split into major parts so pandas skills, statistics concepts, charts/plots, SQL workflows, and applied reference material are easy to find separately.

The examples use small datasets so the logic is easy to understand. In real work, the same code patterns apply to large Excel files, CSV reports, order reports, audit logs, productivity reports, and automation outputs.

## 1.1 Areas of focus

The pandas fundamentals emphasize realistic examples for the areas that usually matter most in day-to-day data manipulation:

- **Reusable masks and complex filters** for combining business rules without creating unreadable one-line expressions, plus guidance on when to create masks, copies, and temporary DataFrames.
- **Custom column creation** that separates raw calculations, Boolean flags, formatted values, and final action labels.
- **Grouping and aggregation** that produces operational summaries with counts, unique counts, totals, averages, rates, percentages, and sorted risk indicators.
- **Joining multiple tables** with merge validation, missing-reference flags, and join audit checks.
- **Index-based joins** for cases where `join` is more appropriate than `merge`.

Basic examples are still included first because they teach the syntax. Complex examples are added after the basics so you can see the full capacity of each tool in a more realistic workflow.

---

# 2. What pandas Is and Why It Matters

`pandas` is a Python library for working with structured data. Structured data means data organized in rows and columns, like an Excel worksheet, CSV file, SQL table, or report export.

In pandas, the most important object is the **DataFrame**.

A DataFrame is basically a table:

- Rows represent records.
- Columns represent fields.
- Each column has a name.
- Each row has an index.

Example:

```python
import pandas as pd

df = pd.DataFrame({
    "Order": ["A100", "A101", "A102"],
    "Budgeted": [100.00, 250.00, 175.00],
    "Actual": [80.00, 250.00, 150.00]
})

print(df)
```

Output:

```text
  Order  Budgeted  Actual
0  A100     100.0     80.0
1  A101     250.0    250.0
2  A102     175.0    150.0
```

Why pandas matters:

- It reads Excel, CSV, JSON, SQL, and many other formats.
- It cleans messy data.
- It filters, groups, summarizes, and reshapes data.
- It calculates statistics.
- It creates charts.
- It works well with automation scripts.
- It can replace many repetitive Excel tasks.

---

# 3. Installation and Setup

## 3.1 Install pandas

In a terminal:

```bash
pip install pandas
```

For Excel support:

```bash
pip install openpyxl
```

For charts:

```bash
pip install matplotlib
```

For numerical operations:

```bash
pip install numpy
```

A common setup command is:

```bash
pip install pandas openpyxl matplotlib numpy
```

## 3.2 Verify installation

```python
import pandas as pd

print(pd.__version__)
```

If this prints a version number, pandas is installed correctly.

## 3.3 Recommended imports

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

`pd`, `np`, and `plt` are standard aliases used by most pandas examples and documentation.

---

# 4. Import Conventions

The standard import convention is:

```python
import pandas as pd
```

This means you call pandas functions using `pd`:

```python
df = pd.DataFrame({"Name": ["Ana", "Luis"], "Score": [90, 85]})
```

You will also often see:

```python
import numpy as np
```

NumPy is useful for numerical operations and conditional logic:

```python
df["Status"] = np.where(df["Score"] >= 90, "Excellent", "Normal")
```

For plotting:

```python
import matplotlib.pyplot as plt
```

Example:

```python
df["Score"].plot(kind="bar")
plt.show()
```

---

# 5. Core pandas Objects

pandas mainly uses two objects:

1. `Series`
2. `DataFrame`

## 5.1 Series

A `Series` is a one-dimensional labeled array. You can think of it as one column.

```python
scores = pd.Series([90, 85, 100], name="Score")

print(scores)
```

Output:

```text
0     90
1     85
2    100
Name: Score, dtype: int64
```

Important details:

- The left side is the index.
- The right side is the value.
- A Series has one data type.

Common Series methods:

```python
scores.mean()
scores.median()
scores.max()
scores.min()
scores.sum()
scores.count()
```

## 5.2 DataFrame

A `DataFrame` is a two-dimensional table.

```python
df = pd.DataFrame({
    "Employee": ["Ana", "Luis", "Maria"],
    "Department": ["Operations", "Operations", "Finance"],
    "Orders": [50, 45, 60]
})

print(df)
```

Output:

```text
  Employee Department  Orders
0      Ana    Operations      50
1     Luis    Operations      45
2    Maria      Finance      60
```

A DataFrame contains:

- Column labels: `Employee`, `Department`, `Orders`
- Row index: `0`, `1`, `2`
- Values: the actual data cells

## 5.3 Series vs DataFrame

```python
single_column = df["Orders"]        # Series
multiple_columns = df[["Employee", "Orders"]]  # DataFrame
```

A single bracket with one column returns a Series:

```python
type(df["Orders"])
```

Output:

```text
pandas.core.series.Series
```

A double bracket returns a DataFrame:

```python
type(df[["Orders"]])
```

Output:

```text
pandas.core.frame.DataFrame
```

This matters because Series and DataFrames have different shapes and sometimes behave differently.

---

# 6. Creating DataFrames

## 6.1 From a dictionary of lists

This is one of the most common ways to create a DataFrame manually.

```python
df = pd.DataFrame({
    "Order": ["C001", "C002", "C003"],
    "Budgeted": [100, 200, 300],
    "Actual": [90, 210, 250]
})
print(df)
```

Output:

```text
  Order  Budgeted  Actual
0  C001       100      90
1  C002       200     210
2  C003       300     250
```

Each dictionary key becomes a column name.

## 6.2 From a list of dictionaries

This is useful when each record comes as a separate dictionary.

```python
records = [
    {"Order": "C001", "Budgeted": 100, "Actual": 90},
    {"Order": "C002", "Budgeted": 200, "Actual": 210},
    {"Order": "C003", "Budgeted": 300, "Actual": 250},
]

df = pd.DataFrame(records)
print(df)
```

Output:

```text
  Order  Budgeted  Actual
0  C001       100      90
1  C002       200     210
2  C003       300     250
```

This format is common when processing API responses or parsed JSON.

## 6.3 From a list of lists

```python
data = [
    ["C001", 100, 90],
    ["C002", 200, 210],
    ["C003", 300, 250],
]

columns = ["Order", "Budgeted", "Actual"]

df = pd.DataFrame(data, columns=columns)
print(df)
```

Output:

```text
  Order  Budgeted  Actual
0  C001       100      90
1  C002       200     210
2  C003       300     250
```

This is useful when data is already arranged like rows.

## 6.4 Creating an empty DataFrame

```python
df = pd.DataFrame(columns=["Order", "Budgeted", "Actual"])
print(df)
```

Output:

```text
Empty DataFrame
Columns: [Order, Budgeted, Actual]
Index: []
```

This is sometimes used when collecting rows in a loop. However, repeatedly appending rows to a DataFrame is inefficient. Usually, it is better to collect dictionaries in a list and convert to a DataFrame once.

Better pattern:

```python
rows = []

for order in ["C001", "C002", "C003"]:
    rows.append({"Order": order})

df = pd.DataFrame(rows)
print(df)
```

Output:

```text
  Order
0  C001
1  C002
2  C003
```

---

# 7. Reading and Writing Files

## 7.1 Read CSV

```python
df = pd.read_csv("orders.csv")
```

Common options:

```python
df = pd.read_csv(
    "orders.csv",
    encoding="utf-8",
    dtype={"Order": "string"},
    parse_dates=["Order_Date"]
)
```

Explanation:

- `encoding="utf-8"`: tells pandas how text is encoded.
- `dtype={"Order": "string"}`: forces a column to be text.
- `parse_dates=["Order_Date"]`: converts a column to datetime.

## 7.2 Write CSV

```python
df.to_csv("output.csv", index=False)
```

Use `index=False` unless you intentionally want the pandas index saved as a column.

## 7.3 Read Excel

```python
df = pd.read_excel("orders.xlsx")
```

Read a specific sheet:

```python
df = pd.read_excel("orders.xlsx", sheet_name="Summary")
```

Read multiple sheets:

```python
sheets = pd.read_excel("orders.xlsx", sheet_name=None)

summary_df = sheets["Summary"]
detail_df = sheets["Detail"]
```

When `sheet_name=None`, pandas returns a dictionary where each key is a sheet name and each value is a DataFrame.

## 7.4 Write Excel

```python
df.to_excel("output.xlsx", index=False)
```

Write multiple sheets:

```python
with pd.ExcelWriter("report.xlsx", engine="openpyxl") as writer:
    summary_df.to_excel(writer, sheet_name="Summary", index=False)
    detail_df.to_excel(writer, sheet_name="Detail", index=False)
```

## 7.5 Read only specific columns

```python
df = pd.read_excel(
    "orders.xlsx",
    usecols=["Order", "Budgeted", "Actual"]
)
```

This is useful for large reports.

## 7.6 Skip rows

```python
df = pd.read_excel("orders.xlsx", skiprows=2)
```

This skips the first two rows. Useful when an Excel export has titles or notes above the actual headers.

## 7.7 Set header row

```python
df = pd.read_excel("orders.xlsx", header=1)
```

This tells pandas that row 2 in Excel should be used as the header row, because pandas uses zero-based row numbering.

---

# 8. Inspecting Data

Before cleaning or analyzing a file, inspect it. The examples in this section use this sample table so the outputs are concrete:

```python
df = pd.DataFrame({
    "Order": ["C001", "C002", "C003", "C004", "C005", "C006"],
    "Status": ["Open", "Closed", "Open", "Pending", "Closed", "Open"],
    "Budgeted": [100, 200, 300, 400, 500, 600],
    "Actual": [90, 210, 250, 400, 525, 580]
})
```

## 8.1 First rows

```python
df.head()
```

Output:

```text
  Order   Status  Budgeted  Actual
0  C001     Open       100      90
1  C002   Closed       200     210
2  C003     Open       300     250
3  C004  Pending       400     400
4  C005   Closed       500     525
```

Shows the first 5 rows.

```python
df.head(10)
```

Shows the first 10 rows.

## 8.2 Last rows

```python
df.tail()
```

Shows the last 5 rows.

## 8.3 Shape

```python
df.shape
```

Output:

```text
(6, 4)
```

Returns:

```text
(rows, columns)
```

Example:

```python
rows, columns = df.shape
print(f"Rows: {rows}, Columns: {columns}")
```

Output:

```text
Rows: 6, Columns: 4
```

## 8.4 Column names

```python
df.columns
```

Output:

```text
Index(['Order', 'Status', 'Budgeted', 'Actual'], dtype='object')
```

Convert columns to a list:

```python
list(df.columns)
```

## 8.5 Data types

```python
df.dtypes
```

This helps identify if numbers were accidentally loaded as text.

## 8.6 Summary info

```python
df.info()
```

This shows:

- Number of rows.
- Column names.
- Non-null count per column.
- Data type per column.
- Memory usage.

## 8.7 Summary statistics

```python
df.describe()
```

For numeric columns, this returns:

- Count
- Mean
- Standard deviation
- Minimum
- 25th percentile
- Median / 50th percentile
- 75th percentile
- Maximum

Include non-numeric columns:

```python
df.describe(include="all")
```

## 8.8 Unique values

```python
df["Status"].unique()
```

Output:

```text
array(['Open', 'Closed', 'Pending'], dtype=object)
```

Number of unique values:

```python
df["Status"].nunique()
```

## 8.9 Value counts

```python
df["Status"].value_counts()
```

Output:

```text
Status
Open       3
Closed     2
Pending    1
Name: count, dtype: int64
```

Include missing values:

```python
df["Status"].value_counts(dropna=False)
```

Normalize to percentages:

```python
df["Status"].value_counts(normalize=True)
```

---

# 9. Selecting Columns and Rows

## 9.1 Select one column

```python
df["Actual"]
```

Output:

```text
0     90
1    210
2    250
3    400
4    525
5    580
Name: Actual, dtype: int64
```

This returns a Series.

## 9.2 Select multiple columns

```python
df[["Order", "Budgeted", "Actual"]]
```

Output:

```text
  Order  Budgeted  Actual
0  C001       100      90
1  C002       200     210
2  C003       300     250
3  C004       400     400
4  C005       500     525
5  C006       600     580
```

This returns a DataFrame.

## 9.3 Select rows by position with `iloc`

`iloc` selects by integer position.

```python
df.iloc[0]
```

Output:

```text
Order       C001
Status      Open
Budgeted     100
Actual        90
Name: 0, dtype: object
```

First row.

```python
df.iloc[0:5]
```

First five rows.

```python
df.iloc[0, 2]
```

Output:

```text
100
```

Value at first row, third column.

## 9.4 Select rows/columns by label with `loc`

`loc` selects by labels.

```python
df.loc[0, "Actual"]
```

Output:

```text
90
```

Row index `0`, column `Actual`.

Select multiple columns:

```python
df.loc[:, ["Order", "Actual"]]
```

Select rows and columns:

```python
df.loc[0:2, ["Order", "Budgeted", "Actual"]]
```

## 9.5 `loc` vs `iloc`

Use `loc` when you know names/labels.

```python
df.loc[df["Actual"] < df["Budgeted"], ["Order", "Actual", "Budgeted"]]
```

Use `iloc` when you know positions.

```python
df.iloc[:, 0:3]
```

---

# 10. Filtering Data

Filtering means keeping only rows that match a condition.

Example dataset:

```python
df = pd.DataFrame({
    "Order": ["C001", "C002", "C003", "C004"],
    "Budgeted": [100, 200, 300, 400],
    "Actual": [90, 210, 250, 400],
    "Status": ["Under Budget", "Over Budget", "Under Budget", "On Budget"]
})
print(df)
```

Output:

```text
  Order  Budgeted  Actual        Status
0  C001       100      90  Under Budget
1  C002       200     210   Over Budget
2  C003       300     250  Under Budget
3  C004       400     400     On Budget
```

## 10.1 Basic filter

```python
under_budget = df[df["Actual"] < df["Budgeted"]]
print(under_budget)
```

Output:

```text
  Order  Budgeted  Actual        Status
0  C001       100      90  Under Budget
2  C003       300     250  Under Budget
```

This keeps rows where actual spending is less than budgeted spending.

## 10.2 Multiple conditions with AND

Use `&` for AND.

```python
result = df[(df["Actual"] < df["Budgeted"]) & (df["Budgeted"] >= 300)]
print(result)
```

Output:

```text
  Order  Budgeted  Actual        Status
2  C003       300     250  Under Budget
```

Each condition must be wrapped in parentheses.

## 10.3 Multiple conditions with OR

Use `|` for OR.

```python
result = df[(df["Status"] == "Under Budget") | (df["Status"] == "Over Budget")]
```

## 10.4 NOT condition

Use `~` for NOT.

```python
not_correct = df[~(df["Status"] == "On Budget")]
```

## 10.5 Filter with `isin`

```python
selected = df[df["Status"].isin(["Under Budget", "Over Budget"])]
```

This is cleaner than many OR conditions.

## 10.6 Filter text contains

```python
matching_status = df[df["Status"].str.contains("budget", case=False, na=False)]
```

Explanation:

- `case=False`: ignore uppercase/lowercase.
- `na=False`: treat missing values as not matching.

## 10.7 Filter missing values

```python
missing_status = df[df["Status"].isna()]
```

Rows where Status is not missing:

```python
known_status = df[df["Status"].notna()]
```

## 10.8 Query syntax

```python
result = df.query("Actual < Budgeted")
print(result)
```

Output:

```text
  Order  Budgeted  Actual        Status
0  C001       100      90  Under Budget
2  C003       300     250  Under Budget
```

Query syntax can be easier to read for simple numeric comparisons.

For column names with spaces:

```python
result = df.query("`Actual Amount` < `Budgeted Amount`")
```

## 10.9 Complex filter pattern: reusable masks

A **mask** is a Boolean Series that says which rows should be kept, updated, or reviewed. Complex filters are easier to understand when each business rule gets its own named mask.

```python
orders = pd.DataFrame({
    "Order": ["C001", "C002", "C003", "C004", "C005", "C006"],
    "Customer": ["North", "North", "South", "South", "West", "West"],
    "Reviewer": ["Ana", "Luis", "Ana", "Maria", "Luis", "Ana"],
    "Budgeted": [1000, 500, 800, 1200, 700, 900],
    "Actual": [950, 650, 760, 1500, 690, 1020],
    "Status": ["Closed", "Closed", "Open", "Closed", "Open", "Closed"],
    "Order_Date": pd.to_datetime([
        "2026-01-05", "2026-01-18", "2026-02-02",
        "2026-02-20", "2026-03-03", "2026-03-14"
    ])
})

orders["Variance"] = orders["Budgeted"] - orders["Actual"]
orders["Variance_Pct"] = orders["Variance"] / orders["Budgeted"]

closed_orders = orders["Status"].eq("Closed")
large_overage = orders["Variance"] < -100
first_quarter = orders["Order_Date"].between("2026-01-01", "2026-03-31")
priority_customers = orders["Customer"].isin(["North", "South"])

review_queue = orders[
    closed_orders
    & large_overage
    & first_quarter
    & priority_customers
].copy()

print(review_queue[["Order", "Customer", "Reviewer", "Variance", "Variance_Pct"]])
```

Output:

```text
  Order Customer Reviewer  Variance  Variance_Pct
1  C002    North     Luis      -150         -0.300
3  C004    South    Maria      -300         -0.250
```

Why this pattern is powerful:

- Each mask has a business meaning.
- You can reuse masks for filtering, updating, charting, or exports.
- The final filter reads like a checklist instead of one long unreadable expression.
- `.copy()` makes it clear that `review_queue` is a separate table you can safely modify.

## 10.10 When to create masks, copies, and temporary DataFrames

As a practical rule, create a named helper object when it makes the analysis safer or easier to explain. Do not create extra objects only to make the code longer.

| Helper object or function | Purpose | Use it when | Avoid it when |
| --- | --- | --- | --- |
| Boolean mask, such as `large_overage = df["Variance"] < -100` | Stores a True/False rule for each row | The condition has business meaning, will be reused, or would make a filter hard to read | The condition is short, used once, and obvious |
| Filtered DataFrame, such as `review_queue = df[mask]` | Stores the rows that match a rule | You need to inspect, export, chart, summarize, or pass those rows to another step | You only need one quick calculation and can keep the expression readable |
| `.copy()` | Creates an independent DataFrame instead of a view-like slice | You plan to edit the filtered result, add columns, rename columns, or pass it to a function that changes it | You are only reading from the filtered result |
| `.loc[row_mask, column_name] = value` | Updates selected rows and selected columns in the original DataFrame | You want to change the original table safely and clearly | You want a separate table that should not affect the original |
| `.query()` | Filters with a readable string expression | The filter is mostly simple column comparisons and arithmetic | Column names are awkward, conditions need many Python variables, or `.loc`/masks are clearer |
| `.assign()` | Adds columns while returning a new DataFrame, often in a chain | You are building a clean pipeline and want each step to return a DataFrame | The calculation needs many separate debugging steps |
| `.pipe()` | Sends the DataFrame into a custom function inside a method chain | You want reusable cleaning or validation steps with a clear purpose | A direct method call is simpler |

Use a **mask** when the rule itself is important enough to name:

```python
closed_orders = orders["Status"].eq("Closed")
large_overage = orders["Variance"] < -100
needs_review = closed_orders & large_overage

review_queue = orders.loc[needs_review].copy()
```

Use `.copy()` when the filtered result becomes its own working table:

```python
review_queue = orders.loc[needs_review].copy()
review_queue["Review_Reason"] = "Closed order over budget by more than 100"
```

This is safer than editing a slice because it makes your intent clear: `review_queue` is now separate from `orders`.

Use `.loc` when you want to update the original DataFrame directly:

```python
orders.loc[needs_review, "Needs_Review"] = True
```

This says exactly which rows and which column should change in `orders`.

A good workflow is:

1. Create masks for meaningful rules.
2. Combine masks into a final rule.
3. Use `.loc` to update the original table, or use `.loc[mask].copy()` to create a separate table for reporting, exporting, or further editing.
4. Add a short comment or clear variable name when a function's purpose is not obvious.

---

# 11. Creating, Updating, and Removing Columns

## 11.1 Create a new column

```python
df["Variance"] = df["Budgeted"] - df["Actual"]
print(df[["Order", "Budgeted", "Actual", "Variance"]])
```

Output:

```text
  Order  Budgeted  Actual  Variance
0  C001       100      90        10
1  C002       200     210       -10
2  C003       300     250        50
3  C004       400     400         0
```

Positive variance means budgeted is greater than actual.

## 11.2 Create a column with conditional logic

```python
import numpy as np

df["Category"] = np.where(
    df["Actual"] < df["Budgeted"],
    "Under Budget",
    "Not Under Budget"
)
```

## 11.3 Multiple conditions with `np.select`

```python
conditions = [
    df["Actual"] < df["Budgeted"],
    df["Actual"] > df["Budgeted"],
    df["Actual"] == df["Budgeted"],
]

choices = ["Under Budget", "Over Budget", "On Budget"]

df["Budget_Status"] = np.select(conditions, choices, default="Review")
print(df[["Order", "Budget_Status"]])
```

Output:

```text
  Order  Budget_Status
0  C001   Under Budget
1  C002    Over Budget
2  C003   Under Budget
3  C004      On Budget
```

## 11.4 Update existing column

```python
df["Status"] = df["Status"].str.upper()
```

## 11.5 Update selected rows

```python
df.loc[df["Variance"] > 0, "Needs_Review"] = True
```

## 11.6 Drop a column

```python
df = df.drop(columns=["Needs_Review"])
```

Drop multiple columns:

```python
df = df.drop(columns=["Column1", "Column2"])
```

## 11.7 Rename columns

```python
df = df.rename(columns={
    "Actual Amt": "Actual",
    "Budgeted Amt": "Budgeted"
})
```

## 11.8 Reorder columns

```python
df = df[["Order", "Budgeted", "Actual", "Variance", "Budget_Status"]]
```

## 11.9 Complex custom column creation

Real analysis often creates several columns in sequence: raw calculations, percentages, categories, flags, and final action labels. The order matters because later columns can depend on earlier columns.

```python
orders = pd.DataFrame({
    "Order": ["C001", "C002", "C003", "C004", "C005"],
    "Customer": ["North", "North", "South", "South", "West"],
    "Budgeted": [1000, 500, 800, 1200, 700],
    "Actual": [950, 650, 760, 1500, 690],
    "Days_Open": [4, 12, 30, 18, 7],
    "Priority": ["Normal", "High", "Normal", "High", "Normal"]
})

orders = orders.assign(
    Variance=lambda d: d["Budgeted"] - d["Actual"],
    Variance_Pct=lambda d: d["Variance"] / d["Budgeted"],
    Is_Over_Budget=lambda d: d["Variance"] < 0,
    Is_Late=lambda d: d["Days_Open"] > 14,
)

conditions = [
    orders["Is_Over_Budget"] & orders["Is_Late"] & orders["Priority"].eq("High"),
    orders["Is_Over_Budget"] & orders["Priority"].eq("High"),
    orders["Is_Over_Budget"],
    orders["Variance_Pct"] >= 0.10,
]

choices = [
    "Escalate immediately",
    "Manager review",
    "Budget review",
    "Savings opportunity",
]

orders["Action"] = np.select(conditions, choices, default="No action")
orders["Variance_Dollars"] = orders["Variance"].map("${:,.0f}".format)

print(orders[[
    "Order", "Customer", "Variance_Dollars", "Variance_Pct",
    "Is_Over_Budget", "Is_Late", "Action"
]])
```

Output:

```text
  Order Customer Variance_Dollars  Variance_Pct  Is_Over_Budget  Is_Late                Action
0  C001    North              $50      0.050000           False    False             No action
1  C002    North            $-150     -0.300000            True    False        Manager review
2  C003    South              $40      0.050000           False     True             No action
3  C004    South            $-300     -0.250000            True     True  Escalate immediately
4  C005     West              $10      0.014286           False    False             No action
```

Important idea: custom columns should separate **calculation columns** from **decision columns**. Calculation columns like `Variance` and `Variance_Pct` explain the numbers. Decision columns like `Action` explain what should happen next.

---

# 12. Index Basics

The index identifies rows.

By default, pandas creates a numeric index:

```text
0, 1, 2, 3, ...
```

## 12.1 Set a column as index

```python
df = df.set_index("Order")
```

Now Order becomes the row label.

## 12.2 Reset index

```python
df = df.reset_index()
```

This converts the index back into a normal column.

## 12.3 Why index matters

Some operations align by index. Example:

```python
s1 = pd.Series([10, 20, 30], index=["A", "B", "C"])
s2 = pd.Series([1, 2, 3], index=["B", "C", "D"])

print(s1 + s2)
```

Output:

```text
A     NaN
B    21.0
C    32.0
D     NaN
dtype: float64
```

pandas matched values by index label, not row position.

---

# 13. Sorting and Ranking

## 13.1 Sort by one column

```python
df = df.sort_values("Variance")
```

Descending:

```python
df = df.sort_values("Variance", ascending=False)
print(df[["Order", "Variance"]])
```

Output:

```text
  Order  Variance
2  C003        50
0  C001        10
3  C004         0
1  C002       -10
```

## 13.2 Sort by multiple columns

```python
df = df.sort_values(["Status", "Variance"], ascending=[True, False])
```

This sorts by Status alphabetically, then by Variance descending inside each Status.

## 13.3 Sort by index

```python
df = df.sort_index()
```

## 13.4 Ranking

```python
df["Variance_Rank"] = df["Variance"].rank(ascending=False)
print(df[["Order", "Variance", "Variance_Rank"]])
```

Output:

```text
  Order  Variance  Variance_Rank
2  C003        50            1.0
0  C001        10            2.0
3  C004         0            3.0
1  C002       -10            4.0
```

Highest variance gets rank 1.

Dense ranking:

```python
df["Dense_Rank"] = df["Variance"].rank(method="dense", ascending=False)
```

Dense ranking does not skip numbers after ties.

---

# 14. Handling Missing Data

Missing data is common in real reports. The examples in this section use this small DataFrame:

```python
df = pd.DataFrame({
    "Order": ["C001", "C002", None, "C004"],
    "Budgeted": [100, 200, 300, None],
    "Actual": [90, None, 250, 400],
    "Status": ["Open", None, "Closed", "Open"]
})
```

pandas usually represents missing values as:

- `NaN`
- `NaT` for missing dates
- `None` in object columns
- `pd.NA` in nullable columns

## 14.1 Detect missing values

```python
df.isna()
```

Count missing values per column:

```python
df.isna().sum()
```

Output:

```text
Order       1
Budgeted    1
Actual      1
Status      1
dtype: int64
```

Percentage missing:

```python
missing_pct = df.isna().mean() * 100
```

## 14.2 Filter rows with missing values

```python
missing_orders = df[df["Order"].isna()]
print(missing_orders)
```

Output:

```text
  Order  Budgeted  Actual  Status
2  None     300.0   250.0  Closed
```

## 14.3 Fill missing values

```python
df["Status"] = df["Status"].fillna("Unknown")
print(df[["Order", "Status"]])
```

Output:

```text
  Order   Status
0  C001     Open
1  C002  Unknown
2  None   Closed
3  C004     Open
```

Fill numeric values with zero:

```python
df["Actual"] = df["Actual"].fillna(0)
```

## 14.4 Fill with mean or median

```python
df["Actual"] = df["Actual"].fillna(df["Actual"].median())
```

Use this carefully. Filling financial values with mean or median can distort totals.

## 14.5 Drop rows with missing values

```python
df_clean = df.dropna()
```

Drop only if specific columns are missing:

```python
df_clean = df.dropna(subset=["Order", "Budgeted", "Actual"])
```

## 14.6 Drop columns with too many missing values

```python
threshold = len(df) * 0.7

df = df.dropna(axis=1, thresh=threshold)
```

This keeps columns that have at least 70% non-missing values.

---

# 15. Data Types and Type Conversion

Data types control how pandas interprets values.

Common pandas data types:

| Type | Meaning | Example |
|---|---|---|
| `int64` | Integer | 10 |
| `float64` | Decimal number | 10.5 |
| `object` | Usually text or mixed values | "ABC" |
| `string` | Text | "ABC" |
| `bool` | True/False | True |
| `datetime64[ns]` | Date/time | 2026-01-01 |
| `category` | Limited set of values | "Open", "Closed" |

## 15.1 Check data types

```python
df.dtypes
```

## 15.2 Convert to numeric

```python
df["Actual"] = pd.to_numeric(df["Actual"], errors="coerce")
```

`errors="coerce"` converts invalid values to missing values.

Example:

```python
s = pd.Series(["100", "200", "bad"])
pd.to_numeric(s, errors="coerce")
```

Output:

```text
0    100.0
1    200.0
2      NaN
dtype: float64
```

## 15.3 Convert to string

```python
df["Order"] = df["Order"].astype("string")
```

This is useful for IDs that may contain leading zeros.

## 15.4 Convert to date

```python
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
```

## 15.5 Convert to category

```python
df["Status"] = df["Status"].astype("category")
```

Category can save memory when a column has repeated values.

---

# 16. String/Text Operations

String methods are accessed through `.str`.

Example:

```python
df = pd.DataFrame({
    "Vendor": ["  Acme Supplies ", "BLUE RIVER", "northwind traders"]
})
print(df)
```

Output:

```text
              Vendor
0    Acme Supplies
1         BLUE RIVER
2  northwind traders
```

## 16.1 Strip spaces

```python
df["Vendor"] = df["Vendor"].str.strip()
print(df)
```

Output:

```text
              Vendor
0      Acme Supplies
1         BLUE RIVER
2  northwind traders
```

## 16.2 Uppercase/lowercase/title case

```python
df["Vendor_Upper"] = df["Vendor"].str.upper()
df["Vendor_Lower"] = df["Vendor"].str.lower()
df["Vendor_Title"] = df["Vendor"].str.title()
print(df[["Vendor", "Vendor_Title"]])
```

Output:

```text
              Vendor       Vendor_Title
0      Acme Supplies      Acme Supplies
1         BLUE RIVER         Blue River
2  northwind traders  Northwind Traders
```

## 16.3 Contains

```python
df["Is_Blue_River"] = df["Vendor"].str.contains("blue", case=False, na=False)
```

## 16.4 Replace text

```python
df["Vendor"] = df["Vendor"].str.replace("BLUE", "Blue", regex=False)
```

## 16.5 Split text

```python
df = pd.DataFrame({"Full_Name": ["John Smith", "Maria Lopez"]})

df[["First_Name", "Last_Name"]] = df["Full_Name"].str.split(" ", n=1, expand=True)
print(df)
```

Output:

```text
     Full_Name First_Name Last_Name
0   John Smith       John     Smith
1  Maria Lopez      Maria     Lopez
```

## 16.6 Extract with regex

```python
df = pd.DataFrame({"Log": ["Paid at 150.00%", "Paid at 200.00%"]})

df["Percent"] = df["Log"].str.extract(r"(\d+\.\d+)%")
print(df)
```

Output:

```text
               Log Percent
0  Paid at 150.00%  150.00
1  Paid at 200.00%  200.00
```

This extracts `150.00` and `200.00` from the text.

## 16.7 Clean column names

```python
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_", regex=False)
)
```

Before:

```text
Customer DOB
```

After:

```text
customer_since
```

---

# 17. Date and Time Operations

Dates are very important in reports.

## 17.1 Convert to datetime

```python
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
```

## 17.2 Extract date parts

```python
df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month
df["Month_Name"] = df["Order_Date"].dt.month_name()
df["Day"] = df["Order_Date"].dt.day
df["Weekday"] = df["Order_Date"].dt.day_name()
```

## 17.3 Format dates as text

```python
df["Order_Date_Text"] = df["Order_Date"].dt.strftime("%m/%d/%Y")
```

For folder names:

```python
df["Month_Folder"] = df["Order_Date"].dt.strftime("%m.%Y")
df["Day_Folder"] = df["Order_Date"].dt.strftime("%m%d%y")
```

## 17.4 Date difference

```python
df["Days_Open"] = (df["Closed_Date"] - df["Open_Date"]).dt.days
```

## 17.5 Filter by date

```python
recent = df[df["Order_Date"] >= "2026-01-01"]
```

Between dates:

```python
mask = df["Order_Date"].between("2026-01-01", "2026-03-31")
quarter_1 = df[mask]
```

## 17.6 Group by month

```python
monthly = df.groupby(df["Order_Date"].dt.to_period("M"))["Actual"].sum()
```

Convert period back to timestamp for plotting:

```python
monthly.index = monthly.index.to_timestamp()
```

---

# 18. Conditional Logic in pandas

## 18.1 Simple condition

```python
df["Under Budget"] = df["Actual"] < df["Budgeted"]
```

This creates a Boolean column.

## 18.2 If/else with `np.where`

```python
df["Status"] = np.where(
    df["Actual"] < df["Budgeted"],
    "Under Budget",
    "Not Under Budget"
)
```

## 18.3 Multiple conditions with `np.select`

```python
conditions = [
    df["Actual"] < df["Budgeted"],
    df["Actual"] > df["Budgeted"],
    df["Actual"] == df["Budgeted"]
]

choices = ["Under Budget", "Over Budget", "On Budget"]

df["Status"] = np.select(conditions, choices, default="Review")
```

## 18.4 Conditional assignment with `loc`

```python
df["Needs_Review"] = False

df.loc[df["Variance"] > 100, "Needs_Review"] = True
```

## 18.5 Nested logic pattern

Avoid deeply nested `np.where` when possible. Use readable conditions.

Less readable:

```python
df["Category"] = np.where(df["Variance"] > 0, "Under Budget", np.where(df["Variance"] < 0, "Over Budget", "On Budget"))
```

More readable:

```python
conditions = [
    df["Variance"] > 0,
    df["Variance"] < 0,
    df["Variance"] == 0
]
choices = ["Under Budget", "Over Budget", "On Budget"]

df["Category"] = np.select(conditions, choices, default="Review")
```

---

# 19. Apply, Map, Replace, and Vectorization

## 19.1 Vectorized operations

Vectorized operations work on entire columns at once.

```python
df["Variance"] = df["Budgeted"] - df["Actual"]
```

This is fast and preferred.

## 19.2 `map`

Use `map` to convert values using a dictionary.

```python
status_map = {
    "U": "Under Budget",
    "O": "Over Budget",
    "C": "On Budget"
}

df["Status_Name"] = df["Status_Code"].map(status_map)
```

Values not found in the dictionary become missing.

## 19.3 `replace`

```python
df["Status"] = df["Status"].replace({
    "Under Budgeted": "Under Budget",
    "Savings Opportunity": "Under Budget"
})
```

## 19.4 `apply` on a column

```python
def classify_variance(value):
    if value > 0:
        return "Under Budget"
    elif value < 0:
        return "Over Budget"
    return "On Budget"


df["Category"] = df["Variance"].apply(classify_variance)
```

## 19.5 `apply` on rows

```python
def create_note(row):
    return f"Order {row['Order']} has variance {row['Variance']}"


df["Note"] = df.apply(create_note, axis=1)
```

Row-wise `apply` is flexible but slower than vectorized logic.

## 19.6 When to use each

| Task | Recommended tool |
|---|---|
| Simple math between columns | Vectorized operation |
| Simple if/else | `np.where` |
| Multiple if/else branches | `np.select` |
| Replace known values | `replace` or `map` |
| Custom row-based text | `apply(axis=1)` |
| Complex function per value | `apply` |

---

# 20. Grouping and Aggregation

Grouping means splitting data into groups and calculating summaries.

Example:

```python
df = pd.DataFrame({
    "Reviewer": ["Ana", "Ana", "Luis", "Luis", "Maria"],
    "Customer": ["A", "B", "A", "B", "A"],
    "Orders": [10, 20, 15, 25, 30],
    "Sales": [1000, 2500, 1500, 3000, 4000]
})
print(df)
```

Output:

```text
  Reviewer Customer  Orders  Sales
0      Ana        A      10   1000
1      Ana        B      20   2500
2     Luis        A      15   1500
3     Luis        B      25   3000
4    Maria        A      30   4000
```

## 20.1 Group by one column

```python
by_reviewer = df.groupby("Reviewer")["Orders"].sum()
print(by_reviewer)
```

Output:

```text
Reviewer
Ana      30
Luis     40
Maria    30
Name: Orders, dtype: int64
```

## 20.2 Group by multiple columns

```python
by_reviewer_customer = df.groupby(["Reviewer", "Customer"])["Sales"].sum()
print(by_reviewer_customer)
```

Output:

```text
Reviewer  Customer
Ana       A           1000
          B           2500
Luis      A           1500
          B           3000
Maria     A           4000
Name: Sales, dtype: int64
```

## 20.3 Multiple aggregations

```python
summary = df.groupby("Reviewer").agg(
    Total_Orders=("Orders", "sum"),
    Average_Orders=("Orders", "mean"),
    Total_Sales=("Sales", "sum"),
    Average_Sales=("Sales", "mean")
).reset_index()
print(summary)
```

Output:

```text
  Reviewer  Total_Orders  Average_Orders  Total_Sales  Average_Sales
0      Ana            30            15.0         3500         1750.0
1     Luis            40            20.0         4500         2250.0
2    Maria            30            30.0         4000         4000.0
```

This is one of the most useful pandas patterns.

## 20.4 Group and count rows

```python
counts = df.groupby("Reviewer").size().reset_index(name="Row_Count")
```

## 20.5 Group and count non-missing values

```python
counts = df.groupby("Reviewer")["Sales"].count()
```

`size()` counts rows.
`count()` counts non-missing values.

## 20.6 Group by date period

```python
monthly = df.groupby(df["Date"].dt.to_period("M")).agg(
    Total_Sales=("Sales", "sum"),
    Order_Count=("Order", "nunique")
)
```

## 20.7 Transform

`transform` returns a value for every original row.

Example: calculate each row's percentage of reviewer total.

```python
df["Reviewer_Total"] = df.groupby("Reviewer")["Sales"].transform("sum")
df["Percent_of_Reviewer_Total"] = df["Sales"] / df["Reviewer_Total"]
```

This keeps the original row count.

## 20.8 Complex grouping example: operational summary

A realistic groupby usually answers several questions at once:

- How much volume did each group handle?
- How many unique records were involved?
- What percentage of records need review?
- Which group has the largest risk or opportunity?

```python
orders = pd.DataFrame({
    "Order": ["C001", "C002", "C003", "C004", "C005", "C006", "C007"],
    "Region": ["East", "East", "East", "West", "West", "West", "West"],
    "Reviewer": ["Ana", "Ana", "Luis", "Luis", "Maria", "Maria", "Ana"],
    "Customer": ["North", "North", "South", "South", "West", "West", "North"],
    "Budgeted": [1000, 500, 800, 1200, 700, 900, 400],
    "Actual": [950, 650, 760, 1500, 690, 1020, 380],
    "Days_Open": [4, 12, 30, 18, 7, 21, 5]
})

orders = orders.assign(
    Variance=lambda d: d["Budgeted"] - d["Actual"],
    Over_Budget=lambda d: d["Variance"] < 0,
    Late=lambda d: d["Days_Open"] > 14,
    Review_Flag=lambda d: d["Over_Budget"] | d["Late"]
)

summary = (
    orders
    .groupby(["Region", "Reviewer"], as_index=False)
    .agg(
        Orders=("Order", "nunique"),
        Customers=("Customer", "nunique"),
        Total_Budgeted=("Budgeted", "sum"),
        Total_Actual=("Actual", "sum"),
        Total_Variance=("Variance", "sum"),
        Review_Rate=("Review_Flag", "mean"),
        Average_Days_Open=("Days_Open", "mean"),
    )
    .assign(Actual_to_Budget=lambda d: d["Total_Actual"] / d["Total_Budgeted"])
    .round({"Review_Rate": 2, "Actual_to_Budget": 2})
    .sort_values(["Review_Rate", "Total_Variance"], ascending=[False, True])
)

print(summary)
```

Output:

```text
  Region Reviewer  Orders  Customers  Total_Budgeted  Total_Actual  Total_Variance  Review_Rate  Average_Days_Open  Actual_to_Budget
3   West     Luis       1          1            1200          1500            -300         1.00               18.0              1.25
1   East     Luis       1          1             800           760              40         1.00               30.0              0.95
4   West    Maria       2          1            1600          1710            -110         0.50               14.0              1.07
0   East      Ana       2          1            1500          1600            -100         0.50                8.0              1.07
2   West      Ana       1          1             400           380              20         0.00                5.0              0.95
```

How to read this result:

- `Orders` and `Customers` describe volume and customer spread.
- `Total_Variance` shows dollar impact. Negative values mean actual spending exceeded budget.
- `Review_Rate` is the share of rows in the group where `Review_Flag` is `True`. Because `True` behaves like `1` and `False` behaves like `0`, the mean of a Boolean column becomes a percentage-like rate.
- Sorting by `Review_Rate` first and `Total_Variance` second puts the most concerning groups near the top.

## 20.9 Group filtering and top records within each group

Sometimes you do not want a summary table. You want the original rows, but only for groups that meet a rule.

```python
orders["Reviewer_Over_Budget_Total"] = (
    orders.groupby("Reviewer")["Variance"]
    .transform(lambda s: s[s < 0].sum())
)

high_risk_rows = orders[orders["Reviewer_Over_Budget_Total"] <= -250]

top_variance_per_region = (
    orders.sort_values("Variance")
    .groupby("Region")
    .head(2)
)
```

Use `transform` when the group calculation needs to return to every original row. Use `agg` when you want one row per group. Use `head`, `tail`, or ranking after sorting when you need the top records inside each group.

---

# 21. Pivot Tables and Cross Tabs

Pivot tables summarize data in a spreadsheet-like way.

## 21.1 Basic pivot table

```python
pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Reviewer",
    columns="Customer",
    aggfunc="sum",
    fill_value=0
)
print(pivot)
```

Output:

```text
Customer     A     B
Reviewer
Ana       1000  2500
Luis      1500  3000
Maria     4000     0
```

Interpretation:

- Rows are reviewers.
- Columns are customers.
- Values are sales amounts.
- The aggregation is sum.

## 21.2 Multiple values

```python
pivot = pd.pivot_table(
    df,
    values=["Orders", "Sales"],
    index="Reviewer",
    columns="Customer",
    aggfunc="sum",
    fill_value=0
)
```

## 21.3 Add totals

```python
pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Reviewer",
    columns="Customer",
    aggfunc="sum",
    fill_value=0,
    margins=True,
    margins_name="Total"
)
```

## 21.4 Cross tab

`crosstab` counts combinations of categories.

```python
ct = pd.crosstab(df["Reviewer"], df["Customer"])
```

Normalize to percentages:

```python
ct_pct = pd.crosstab(df["Reviewer"], df["Customer"], normalize="index")
```

This shows each reviewer's distribution across customers.

---

# 22. Reshaping Data

Reshaping changes the structure of your DataFrame.

## 22.1 Wide vs long format

Wide format:

| Reviewer | Jan | Feb | Mar |
|---|---:|---:|---:|
| Ana | 10 | 12 | 15 |
| Luis | 8 | 9 | 11 |

Long format:

| Reviewer | Month | Orders |
|---|---|---:|
| Ana | Jan | 10 |
| Ana | Feb | 12 |
| Ana | Mar | 15 |
| Luis | Jan | 8 |
| Luis | Feb | 9 |
| Luis | Mar | 11 |

Long format is usually better for analysis and plotting.

## 22.2 Melt wide to long

```python
wide = pd.DataFrame({
    "Reviewer": ["Ana", "Luis"],
    "Jan": [10, 8],
    "Feb": [12, 9],
    "Mar": [15, 11]
})

long = wide.melt(
    id_vars="Reviewer",
    var_name="Month",
    value_name="Orders"
)
print(long)
```

Output:

```text
  Reviewer Month  Orders
0      Ana   Jan      10
1     Luis   Jan       8
2      Ana   Feb      12
3     Luis   Feb       9
4      Ana   Mar      15
5     Luis   Mar      11
```

## 22.3 Pivot long to wide

```python
wide_again = long.pivot(
    index="Reviewer",
    columns="Month",
    values="Orders"
).reset_index()
```

## 22.4 Stack and unstack

```python
summary = df.groupby(["Reviewer", "Customer"])["Sales"].sum()
```

This creates a Series with a multi-index.

Unstack:

```python
wide_summary = summary.unstack(fill_value=0)
```

Stack back:

```python
long_summary = wide_summary.stack()
```

---

# 23. Combining DataFrames

There are three common ways to combine DataFrames:

1. `concat`
2. `merge`
3. `join`

## 23.1 Concatenate rows

Use `concat` when stacking similar tables.

```python
january = pd.DataFrame({"Order": ["C001", "C002"], "Month": ["Jan", "Jan"]})
february = pd.DataFrame({"Order": ["C003", "C004"], "Month": ["Feb", "Feb"]})

all_orders = pd.concat([january, february], ignore_index=True)
```

Use `ignore_index=True` to create a new clean index.

## 23.2 Concatenate columns

```python
combined = pd.concat([df1, df2], axis=1)
```

This combines side by side by index alignment.

## 23.3 Merge like SQL joins

```python
orders = pd.DataFrame({
    "Order": ["C001", "C002", "C003"],
    "Vendor_ID": [1, 2, 1]
})

vendors = pd.DataFrame({
    "Vendor_ID": [1, 2],
    "Vendor_Name": ["Acme Supplies", "Blue River"]
})

merged = orders.merge(vendors, on="Vendor_ID", how="left")
print(merged)
```

Output:

```text
  Order  Vendor_ID    Vendor_Name
0  C001          1  Acme Supplies
1  C002          2     Blue River
2  C003          1  Acme Supplies
```

## 23.4 Join types

| Join type | Keeps |
|---|---|
| `inner` | Only matching rows in both tables |
| `left` | All rows from left table, matches from right |
| `right` | All rows from right table, matches from left |
| `outer` | All rows from both tables |

## 23.5 Merge on different column names

```python
merged = orders.merge(
    vendors,
    left_on="Vendor_ID",
    right_on="ID",
    how="left"
)
```

## 23.6 Validate merge quality

```python
merged = orders.merge(
    vendors,
    on="Vendor_ID",
    how="left",
    validate="many_to_one"
)
```

This helps catch unexpected duplicate matches.

Common validations:

| Validation | Meaning |
|---|---|
| `one_to_one` | Each key appears once in each table |
| `one_to_many` | Left key unique, right key can repeat |
| `many_to_one` | Left key can repeat, right key unique |
| `many_to_many` | Both sides can repeat |

## 23.7 Indicator column

```python
merged = orders.merge(vendors, on="Vendor_ID", how="left", indicator=True)
```

This adds `_merge`:

- `both`
- `left_only`
- `right_only`

Useful for audit checks.

## 23.8 Complex example: joining multiple lookup tables

Real projects rarely merge only two tables. A common workflow starts with a transaction table and joins several lookup or reference tables onto it.

```python
orders = pd.DataFrame({
    "Order": ["C001", "C002", "C003", "C004", "C005"],
    "Customer_ID": [10, 10, 20, 30, 40],
    "Vendor_ID": [1, 2, 1, 3, 99],
    "Reviewer_ID": [100, 101, 100, 102, 103],
    "Budgeted": [1000, 500, 800, 1200, 700],
    "Actual": [950, 650, 760, 1500, 690]
})

customers = pd.DataFrame({
    "Customer_ID": [10, 20, 30],
    "Customer": ["North", "South", "West"],
    "Region": ["East", "East", "West"]
})

vendors = pd.DataFrame({
    "Vendor_ID": [1, 2, 3],
    "Vendor_Name": ["Acme Supplies", "Blue River", "Canyon Parts"],
    "Vendor_Tier": ["Preferred", "Standard", "Preferred"]
})

reviewers = pd.DataFrame({
    "Reviewer_ID": [100, 101, 102],
    "Reviewer": ["Ana", "Luis", "Maria"]
})

merged = (
    orders
    .merge(customers, on="Customer_ID", how="left", validate="many_to_one")
    .merge(vendors, on="Vendor_ID", how="left", validate="many_to_one")
    .merge(reviewers, on="Reviewer_ID", how="left", validate="many_to_one")
    .assign(
        Variance=lambda d: d["Budgeted"] - d["Actual"],
        Needs_Reference_Review=lambda d: (
            d[["Customer", "Vendor_Name", "Reviewer"]].isna().any(axis=1)
        )
    )
)

print(merged[[
    "Order", "Customer", "Region", "Vendor_Name",
    "Vendor_Tier", "Reviewer", "Variance", "Needs_Reference_Review"
]])
```

Output:

```text
  Order Customer Region     Vendor_Name Vendor_Tier Reviewer  Variance  Needs_Reference_Review
0  C001    North   East   Acme Supplies  Preferred      Ana        50                   False
1  C002    North   East      Blue River   Standard     Luis      -150                   False
2  C003    South   East   Acme Supplies  Preferred      Ana        40                   False
3  C004     West   West    Canyon Parts  Preferred    Maria      -300                   False
4  C005      NaN    NaN             NaN        NaN      NaN        10                    True
```

What this shows:

- `orders` is the base table because every output row should represent an order.
- Each lookup table is joined with `how="left"` so missing reference data does not delete orders.
- `validate="many_to_one"` confirms that many orders can match one lookup record, but the lookup key should not duplicate.
- `Needs_Reference_Review` flags rows where at least one lookup failed.

## 23.9 Merge audit pattern with `_merge`

When data quality matters, audit the join before trusting the output.

```python
audit = orders.merge(
    vendors,
    on="Vendor_ID",
    how="left",
    indicator=True,
    validate="many_to_one"
)

unmatched_vendors = audit[audit["_merge"].eq("left_only")]

print(unmatched_vendors[["Order", "Vendor_ID", "_merge"]])
```

Output:

```text
  Order  Vendor_ID     _merge
4  C005         99  left_only
```

Use this pattern before exporting or summarizing merged data. A failed lookup can silently create missing customer names, vendor names, prices, categories, or reviewer assignments.

## 23.10 `join` when the index is the key

`join` is most convenient when one or both DataFrames already use the key as the index.

```python
orders_by_customer = orders.set_index("Customer_ID")
customer_lookup = customers.set_index("Customer_ID")

joined = orders_by_customer.join(customer_lookup, how="left")
```

Use `merge` for most business joins because it makes the key columns explicit. Use `join` when index-based alignment is intentional.

---

# 24. Duplicates and Data Quality Checks

## 24.1 Find duplicate rows

```python
duplicates = df[df.duplicated()]
```

## 24.2 Find duplicate based on specific columns

```python
duplicates = df[df.duplicated(subset=["Order"], keep=False)]
```

`keep=False` shows all duplicated records.

## 24.3 Drop duplicates

```python
df_unique = df.drop_duplicates(subset=["Order"])
```

Keep last:

```python
df_unique = df.drop_duplicates(subset=["Order"], keep="last")
```

## 24.4 Basic quality checks

```python
checks = {
    "row_count": len(df),
    "duplicate_orders": df.duplicated(subset=["Order"]).sum(),
    "missing_orders": df["Order"].isna().sum(),
    "missing_budgeted": df["Budgeted"].isna().sum(),
    "missing_actual": df["Actual"].isna().sum(),
}

print(checks)
```

## 24.5 Validate required columns

```python
required_columns = ["Order", "Budgeted", "Actual"]

missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    raise ValueError(f"Missing required columns: {missing_columns}")
```

This is very useful for automation scripts that depend on consistent headers.

---

# 25. Working with Excel Reports

Excel reports often need special handling.

## 25.1 Read Excel safely

```python
df = pd.read_excel(
    "report.xlsx",
    sheet_name="Summary",
    dtype={"Order": "string", "Member ID": "string"}
)
```

IDs should often be text, not numbers, because numbers may lose leading zeros.

## 25.2 Clean Excel column names

```python
df.columns = (
    df.columns
      .str.strip()
      .str.replace("\n", " ", regex=False)
      .str.replace(r"\s+", " ", regex=True)
)
```

This removes extra spaces and line breaks.

## 25.3 Save filtered results to Excel

```python
under_budget = df[df["Actual"] < df["Budgeted"]]

under_budget.to_excel("budget_variance_items.xlsx", index=False)
```

## 25.4 Save multiple outputs

```python
with pd.ExcelWriter("order_review_output.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="All Data", index=False)
    under_budget.to_excel(writer, sheet_name="Under Budget", index=False)
    summary.to_excel(writer, sheet_name="Summary", index=False)
```

## 25.5 Avoid common Excel problems

| Problem | Cause | Fix |
|---|---|---|
| IDs become numbers | Excel/pandas inferred numeric type | Use `dtype={"ID": "string"}` |
| Dates become text | Date column not parsed | Use `pd.to_datetime()` |
| Blank rows appear | Export contains extra blank rows | Use `dropna(how="all")` |
| Wrong header row | Report has title rows | Use `skiprows` or `header` |
| Money values are text | Dollar signs/commas | Clean text, then `pd.to_numeric()` |

Example cleaning money stored as text:

```python
df["Actual"] = (
    df["Actual"]
      .astype("string")
      .str.replace("$", "", regex=False)
      .str.replace(",", "", regex=False)
)

df["Actual"] = pd.to_numeric(df["Actual"], errors="coerce")
```

---

# Part II: Statistics

This part separates the statistical concepts from the pandas workflow. It explains what common statistics mean, how to calculate them with pandas, and how to interpret them in practical review work.

---

# 26. Basic Statistics with pandas

Statistics help summarize and understand data. pandas has many built-in methods for statistics.

Example dataset:

```python
scores = pd.Series([2, 3, 3, 4, 4, 4, 5, 6, 7, 20], name="Score")
```

This dataset has one large value: `20`. That value is an outlier compared with the rest.

## 26.1 Count

Count means how many non-missing values exist.

```python
scores.count()
```

Interpretation:

- If count is 10, there are 10 non-missing values.
- Missing values are ignored by default.

For a DataFrame:

```python
df.count()
```

This gives non-missing counts per column.

## 26.2 Sum

```python
scores.sum()
```

The sum is the total of all values.

Use cases:

- Total order amounts.
- Total budgeted and actual amount.
- Total sales amount.
- Total variance.

## 26.3 Mean

![Mean, Median, and Mode](pandas_manual_assets/stats_mean_median_mode.svg)

Mean is the average.

Formula concept:

```text
mean = total sum / number of values
```

In pandas:

```python
scores.mean()
```

Interpretation:

- Mean represents the balance point of the data.
- It is useful when values are fairly consistent.
- It is sensitive to outliers.

Example:

```python
pd.Series([10, 10, 10, 10, 100]).mean()
```

The mean is pulled upward by `100`.

Use mean when:

- You want the general average.
- Outliers are not extreme.
- Total distribution is reasonably balanced.

Be careful with mean when:

- There are extreme values.
- The data is skewed.
- A few large orders can distort the average.

## 26.4 Median

Median is the middle value after sorting.

```python
scores.median()
```

Interpretation:

- Half the values are below the median.
- Half the values are above the median.
- Median is more resistant to outliers than mean.

Use median when:

- Data is skewed.
- Outliers exist.
- You want the “typical” value.

Example:

```python
pd.Series([10, 10, 10, 10, 100]).median()
```

The median is `10`, which better represents the typical value than the mean.

## 26.5 Mode

Mode is the most frequent value.

```python
scores.mode()
```

Output can contain more than one value if there are ties.

Example:

```python
pd.Series(["A", "A", "B", "B", "C"]).mode()
```

Returns both `A` and `B` because both appear twice.

Use mode when:

- You need the most common product category.
- You need the most common issue type.
- You need the most common status.
- You are analyzing categorical data.

## 26.6 Minimum and maximum

```python
scores.min()
scores.max()
```

Interpretation:

- Minimum is the smallest value.
- Maximum is the largest value.
- They help you understand the range of possible values.

## 26.7 Range

Range is maximum minus minimum.

```python
value_range = scores.max() - scores.min()
```

Interpretation:

- A small range means values are close together.
- A large range means values are spread out.
- Range is sensitive to outliers.

## 26.8 Variance

Variance measures how spread out values are from the mean.

```python
scores.var()
```

Interpretation:

- Low variance means values are close to the mean.
- High variance means values are more spread out.
- Variance is in squared units, so it can be less intuitive than standard deviation.

## 26.9 Standard deviation

Standard deviation is the square root of variance.

```python
scores.std()
```

Interpretation:

- Standard deviation measures typical distance from the mean.
- A small standard deviation means values are consistent.
- A large standard deviation means values vary a lot.

Example interpretation:

If average sales amount is `$1,000` and standard deviation is `$100`, most values are relatively close to `$1,000`.

If average sales amount is `$1,000` and standard deviation is `$900`, values are highly spread out.

## 26.10 Percentiles and quantiles

![Box Plot Quartiles](pandas_manual_assets/plot_boxplot_quartiles_outliers.svg)

A percentile tells you the value below which a percentage of data falls.

```python
scores.quantile(0.25)  # 25th percentile
scores.quantile(0.50)  # 50th percentile, same as median
scores.quantile(0.75)  # 75th percentile
```

Interpretation:

- 25th percentile: 25% of values are below this.
- 50th percentile: median.
- 75th percentile: 75% of values are below this.

## 26.11 Quartiles

Quartiles divide data into four parts.

- Q1 = 25th percentile
- Q2 = 50th percentile / median
- Q3 = 75th percentile

```python
q1 = scores.quantile(0.25)
q2 = scores.quantile(0.50)
q3 = scores.quantile(0.75)
```

## 26.12 IQR

IQR means Interquartile Range.

```python
iqr = q3 - q1
```

Interpretation:

- IQR measures the spread of the middle 50% of values.
- It is less affected by outliers than the full range.
- It is often used for outlier detection.

## 26.13 Outlier detection with IQR

```python
q1 = scores.quantile(0.25)
q3 = scores.quantile(0.75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = scores[(scores < lower_bound) | (scores > upper_bound)]
```

Interpretation:

- Values below `lower_bound` may be unusually low.
- Values above `upper_bound` may be unusually high.
- Outliers are not automatically errors; they are values that deserve review.

## 26.14 Correlation

![Correlation Heatmap](pandas_manual_assets/plot_correlation_heatmap.svg)

Correlation measures how two numeric columns move together.

```python
df[["Budgeted", "Actual"]].corr()
```

Correlation ranges from `-1` to `1`.

| Correlation | Meaning |
|---:|---|
| Close to `1` | Strong positive relationship |
| Close to `0` | Little or no linear relationship |
| Close to `-1` | Strong negative relationship |

Important: correlation does not prove causation.

## 26.15 Covariance

Covariance also measures how two variables move together.

```python
df[["Budgeted", "Actual"]].cov()
```

Interpretation:

- Positive covariance: values tend to increase together.
- Negative covariance: one tends to increase while the other decreases.
- Covariance is harder to interpret than correlation because it depends on units.

## 26.16 Skewness

![Histogram Distribution](pandas_manual_assets/plot_histogram_distribution.svg)

Skewness measures whether a distribution leans left or right.

```python
scores.skew()
```

Interpretation:

- Positive skew: long tail to the right; a few high values.
- Negative skew: long tail to the left; a few low values.
- Near zero: roughly balanced distribution.

## 26.17 `describe()`

```python
scores.describe()
```

For a DataFrame:

```python
df.describe()
```

This is one of the fastest ways to get a statistical overview.

## 26.18 Multiple statistics at once

```python
summary = scores.agg(["count", "sum", "mean", "median", "min", "max", "std"])
```

For a DataFrame:

```python
summary = df[["Budgeted", "Actual", "Variance"]].agg([
    "count", "sum", "mean", "median", "min", "max", "std"
])
```

## 26.19 Grouped statistics

```python
summary = df.groupby("Reviewer").agg(
    Order_Count=("Order", "nunique"),
    Total_Budgeted=("Budgeted", "sum"),
    Total_Actual=("Actual", "sum"),
    Average_Variance=("Variance", "mean"),
    Median_Variance=("Variance", "median")
).reset_index()
```

Interpretation:

- Total columns show volume.
- Average columns show central tendency.
- Median columns show typical values when outliers may exist.
- Order count shows workload or sample size.

## 26.20 Numeric-column statistics only

Many DataFrames contain text, dates, IDs, and numeric measures together. When calculating statistics, choose the numeric columns intentionally.

```python
numeric_cols = ["Budgeted", "Actual", "Variance"]
summary = df[numeric_cols].describe()
```

You can also let pandas select numeric columns:

```python
numeric_summary = df.select_dtypes(include="number").describe()
```

Use intentional numeric selection when:

- ID columns are stored as numbers but should not be averaged.
- Some numeric-looking columns are actually codes.
- You want the summary to include only business measures.

## 26.21 Missing values in statistics

Most pandas statistics skip missing values by default.

```python
scores_with_missing = pd.Series([2, 3, None, 4, 20])

scores_with_missing.mean()
scores_with_missing.count()
```

Interpretation:

- The mean is calculated from the non-missing values.
- `count()` reports how many values were actually used.
- Missing values can make a statistic less reliable if many records are incomplete.

Always check missingness next to important statistics:

```python
stats_with_missing = pd.DataFrame({
    "mean": df[["Budgeted", "Actual"]].mean(),
    "count_used": df[["Budgeted", "Actual"]].count(),
    "missing_count": df[["Budgeted", "Actual"]].isna().sum(),
    "missing_pct": df[["Budgeted", "Actual"]].isna().mean() * 100
})
```

## 26.22 Sample vs population standard deviation

By default, pandas uses sample standard deviation for `std()` and sample variance for `var()`.

```python
sample_std = scores.std()
population_std = scores.std(ddof=0)
```

Plain-English meaning:

- Use sample standard deviation when your data is a sample used to estimate a larger group.
- Use population standard deviation when your data contains every record you care about.
- For large datasets, the difference is often small.
- For small datasets, the difference can be noticeable.

## 26.23 Percentages and proportions

A proportion is a part divided by a whole. A percentage is a proportion multiplied by 100.

```python
status_counts = df["Status"].value_counts(dropna=False)
status_proportions = df["Status"].value_counts(normalize=True, dropna=False)
status_percentages = status_proportions * 100
```

Interpretation:

- `0.25` as a proportion means one quarter of the records.
- `25%` as a percentage means the same thing in a reader-friendly format.
- `dropna=False` includes missing status values in the denominator.

## 26.24 Cross-tabulation

A cross-tabulation counts how two categorical columns combine.

```python
pd.crosstab(df["Region"], df["Status"])
```

Add row percentages:

```python
pd.crosstab(df["Region"], df["Status"], normalize="index") * 100
```

Interpretation:

- Counts answer: how many records are in each combination?
- Row percentages answer: within each row group, what share belongs to each category?
- Cross-tabs are useful for comparing status mix, issue mix, or category mix across groups.

## 26.25 Weighted averages

A regular mean treats every row equally. A weighted average gives more importance to rows with larger weights.

Example: average price per unit sold.

```python
weighted_average_price = (df["Price"] * df["Units"]).sum() / df["Units"].sum()
```

Use weighted averages when:

- Rows represent different quantities.
- Some records should count more than others.
- You want an average per unit, dollar, hour, or other weight.

Avoid weighted averages when the weight column has missing, zero, or negative values unless those values are expected and handled intentionally.

## 26.26 Coefficient of variation

Coefficient of variation compares standard deviation to the mean.

```python
cv = df["Actual"].std() / df["Actual"].mean()
```

Interpretation:

- Higher coefficient of variation means more relative variation.
- Lower coefficient of variation means more consistency relative to the average.
- It can help compare spread between groups with different average sizes.

Example grouped calculation:

```python
variation_by_region = df.groupby("Region").agg(
    Average_Actual=("Actual", "mean"),
    Std_Actual=("Actual", "std")
)

variation_by_region["CV_Actual"] = (
    variation_by_region["Std_Actual"] / variation_by_region["Average_Actual"]
)
```

## 26.27 Ranking and top-N analysis

Ranking helps find the largest, smallest, best, worst, fastest, or slowest records.

```python
top_orders = df.nlargest(10, "Actual")
bottom_orders = df.nsmallest(10, "Actual")
```

For grouped top-N analysis:

```python
top_customers = (
    df.groupby("Customer", as_index=False)
      .agg(Total_Actual=("Actual", "sum"), Order_Count=("Order", "count"))
      .sort_values("Total_Actual", ascending=False)
      .head(10)
)
```

Interpretation:

- Top-N lists are useful for prioritizing review work.
- Always show the measure used for ranking.
- Include counts when ranking grouped summaries so small groups do not look more important than they are.

## 26.28 A compact statistics report

A practical report often combines totals, typical values, spread, and missingness.

```python
report = df.groupby("Region").agg(
    Records=("Order", "count"),
    Total_Actual=("Actual", "sum"),
    Average_Actual=("Actual", "mean"),
    Median_Actual=("Actual", "median"),
    Std_Actual=("Actual", "std"),
    P90_Actual=("Actual", lambda s: s.quantile(0.90)),
    Missing_Actual=("Actual", lambda s: s.isna().sum())
).reset_index()
```

This report supports several questions at once:

- Which region has the largest total actual amount?
- Which region has the highest typical order?
- Which region has the most variation?
- Which region has unusually high 90th percentile values?
- Which region has missing data that may weaken the summary?

---

# 27. Statistics Interpretation Guide

Statistics are tools for answering specific questions. A statistic is useful only when you know:

1. **What question it answers.**
2. **What data was included.**
3. **What data was excluded or missing.**
4. **Whether the result describes totals, typical records, variation, ranking, or relationships.**
5. **What action or follow-up question the result suggests.**

A good statistical summary should help a reader move from raw data to a decision. It should not be a pile of numbers without context.

## 27.1 The basic statistics decision table

Use this table when deciding which statistic to calculate.

| If you need to know... | Use... | pandas example | Plain-English interpretation |
|---|---|---|---|
| How many records exist | Count | `df["Order"].count()` | There are this many non-missing records. |
| Total volume | Sum | `df["Actual"].sum()` | All records together add up to this amount. |
| Typical value in balanced data | Mean | `df["Actual"].mean()` | The average record is about this amount. |
| Typical value with outliers | Median | `df["Actual"].median()` | The middle record is this amount. |
| Most common category | Mode / value counts | `df["Status"].value_counts()` | This category appears most often. |
| Lowest and highest values | Min / max | `df["Actual"].min()` | Values run from this low to this high. |
| Overall spread | Standard deviation | `df["Actual"].std()` | Values are usually this far from the average. |
| Middle spread | IQR | `q3 - q1` | The middle half of records spans this range. |
| Thresholds | Percentiles | `df["Actual"].quantile(0.90)` | 90% of records are at or below this value. |
| Relationship between two numbers | Correlation | `df[["Orders", "Profit"]].corr()` | These two columns tend to move together, apart, or not much at all. |
| Share of a whole | Percentage | `counts / counts.sum()` | This category represents this share of the total. |
| Group comparison | Grouped aggregation | `df.groupby("Region")["Actual"].mean()` | Each group has its own summary value. |

## 27.2 Count, missing values, and the denominator

Before interpreting any statistic, check the denominator. The denominator is the number that the statistic is based on.

```python
row_count = len(df)
non_missing_actual = df["Actual"].count()
missing_actual = df["Actual"].isna().sum()
missing_actual_pct = df["Actual"].isna().mean() * 100
```

Interpretation:

- `len(df)` counts all rows.
- `count()` counts only non-missing values in the selected column.
- `isna().sum()` counts missing values.
- `isna().mean() * 100` gives the missing percentage.

This matters because an average from 10 complete records is much weaker than an average from 10,000 complete records. It also matters when each column has a different number of missing values.

Useful reporting sentence:

> The average actual amount was `$1,240`, based on 8,415 non-missing records; 3.2% of records were missing actual amount.

## 27.3 Mean vs median

![Mean vs Median with Outlier](pandas_manual_assets/stats_mean_median_mode.svg)

Mean and median answer different questions.

| Statistic | Question it answers | Best when | Weakness |
|---|---|---|---|
| Mean | What is the arithmetic average? | Data is balanced and totals matter | Pulled by outliers |
| Median | What is the middle record? | Data has outliers or skew | Ignores the size of extreme values |

Example:

```python
amounts = pd.Series([100, 110, 120, 130, 10000])

print(amounts.mean())
print(amounts.median())
```

The mean is much higher because of `10000`. The median better represents the typical record.

In order data, this matters because a few very large orders can distort averages.

Practical rule:

- Report the **mean** when the question is about total load spread across records, such as average cost per order.
- Report the **median** when the question is about the typical record, especially when amounts are skewed.
- Report **both** when readers need to understand whether outliers are affecting the average.

## 27.4 Mode and value counts interpretation

Mode tells you what appears most often.

```python
df["Issue_Type"].mode()
```

If the mode is `Quantity Issue`, that means it is the most frequently occurring issue type.

For categories, `value_counts()` is often more useful than `mode()` because it shows the full ranking.

```python
issue_counts = df["Issue_Type"].value_counts(dropna=False)
issue_share = df["Issue_Type"].value_counts(normalize=True, dropna=False) * 100
```

Interpretation:

- Counts show volume.
- Percentages show share.
- `dropna=False` keeps missing categories visible.

Useful reporting sentence:

> Quantity Issue was the most common issue type, with 184 records, representing 37.6% of all reviewed issues.

## 27.5 Standard deviation interpretation

Standard deviation tells you consistency.

Example:

```python
team_a = pd.Series([98, 100, 101, 99, 102])
team_b = pd.Series([50, 80, 100, 130, 170])

team_a.std()
team_b.std()
```

Team A has low standard deviation, meaning results are consistent.

Team B has high standard deviation, meaning results vary a lot.

Use standard deviation when:

- You want to describe consistency around the average.
- The mean is meaningful for the data.
- You are comparing variation between similar measures.

Be careful when:

- The data is strongly skewed.
- Outliers dominate the spread.
- You compare groups with very different averages.

When group averages are very different, the coefficient of variation can help compare relative variation.

```python
cv = df["Actual"].std() / df["Actual"].mean()
```

A higher coefficient of variation means more variation relative to the average.

## 27.6 Percentiles interpretation

Percentiles help understand thresholds.

Example:

```python
df["Sales"].quantile([0.25, 0.50, 0.75, 0.90])
```

If the 90th percentile is `$5,000`, that means 90% of records are at or below `$5,000`, and 10% are above `$5,000`.

Percentiles are useful for questions like:

- What amount separates the largest 10% of orders from the rest?
- What processing time do 95% of records meet?
- Where should we set a review threshold?

Useful reporting sentence:

> The 95th percentile processing time was 12 days, meaning 95% of records were completed in 12 days or less and 5% took longer.

## 27.7 Quartiles and IQR interpretation

Quartiles divide the data into four parts:

- **Q1:** 25% of values are at or below this point.
- **Q2:** the median; 50% of values are at or below this point.
- **Q3:** 75% of values are at or below this point.

The IQR is `Q3 - Q1`. It describes the spread of the middle 50% of records.

```python
q1 = df["Actual"].quantile(0.25)
q3 = df["Actual"].quantile(0.75)
iqr = q3 - q1
```

Interpretation:

- A small IQR means the middle records are tightly grouped.
- A large IQR means typical records vary widely.
- IQR is less affected by extreme outliers than the full range.

## 27.8 Outlier interpretation

![Box Plot Outliers](pandas_manual_assets/plot_boxplot_quartiles_outliers.svg)

An outlier is unusual, not automatically wrong.

Examples of valid outliers:

- A very high-dollar order.
- A rare contract issue.
- An order with many line items.
- A large one-time purchase.

Examples of suspicious outliers:

- Negative order amounts when impossible.
- Dates far outside the reporting period.
- Actual amount much higher than budgeted.
- Unit count extremely high because of data entry error.

A useful outlier workflow:

```python
q1 = df["Actual"].quantile(0.25)
q3 = df["Actual"].quantile(0.75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = df[(df["Actual"] < lower_bound) | (df["Actual"] > upper_bound)]
```

Then review the outlier rows instead of deleting them automatically.

Questions to ask:

1. Is the value possible?
2. Is the unit correct?
3. Is the date in scope?
4. Is the record a duplicate?
5. Does the outlier represent a real business exception?
6. Should the statistic be reported with and without the outlier?

## 27.9 Correlation interpretation

![Correlation Heatmap](pandas_manual_assets/plot_correlation_heatmap.svg)

Example:

```python
df[["Order_Count", "Sales_Amount"]].corr()
```

If correlation is `0.90`, order count and sales amount tend to increase together.

If correlation is `0.05`, order count does not explain sales amount very well.

If correlation is `-0.80`, as one goes up, the other tends to go down.

Interpret correlation with these cautions:

- Correlation describes a **linear** relationship; curved relationships may be missed.
- Correlation does not prove that one column causes the other.
- Outliers can make correlation look stronger or weaker than it really is.
- A strong relationship may be caused by a third factor not shown in the data.
- Correlation should usually be checked with a scatter plot.

Useful reporting sentence:

> Orders and profit had a correlation of 0.78, suggesting they usually increase together, but this does not prove that more orders caused higher profit.

## 27.10 Grouped statistics interpretation

Grouped statistics compare summaries across categories.

```python
summary = df.groupby("Region").agg(
    Order_Count=("Order", "nunique"),
    Total_Actual=("Actual", "sum"),
    Average_Actual=("Actual", "mean"),
    Median_Actual=("Actual", "median")
).reset_index()
```

Interpret grouped results carefully:

- A group with a high total may simply have more records.
- A group with a high average may have only a few records.
- A group with a high median is usually high for a typical record.
- A group with a large gap between mean and median may have outliers or skew.

Good grouped summaries usually include both a measure and a count.

```python
summary = summary.sort_values("Total_Actual", ascending=False)
```

Sorting helps readers see the largest groups first.

## 27.11 Percentages, rates, and shares

Percentages need a clear denominator.

```python
status_counts = df["Status"].value_counts()
status_pct = df["Status"].value_counts(normalize=True) * 100
```

For grouped percentages, calculate the denominator inside each group.

```python
status_by_region = pd.crosstab(
    df["Region"],
    df["Status"],
    normalize="index"
) * 100
```

Interpretation:

- `normalize="index"` means each row adds to 100%.
- This answers: within each region, what percentage belongs to each status?

Do not compare percentages without asking:

1. What is the denominator?
2. Is the denominator large enough?
3. Are missing values included or excluded?
4. Are the groups comparable?

## 27.12 Weighted average interpretation

A regular average treats every row equally. A weighted average gives more influence to rows with larger weights.

Use a weighted average when records do not represent equal importance.

Example:

```python
weighted_avg_price = (df["Price"] * df["Units"]).sum() / df["Units"].sum()
```

Interpretation:

- A regular average price answers: what is the average row price?
- A weighted average price answers: what is the average price per unit sold?

This difference matters when one row represents 1 unit and another row represents 10,000 units.

## 27.13 Sample vs population interpretation

Sometimes your data is the full population. Other times it is a sample.

| Situation | Meaning | pandas default to know |
|---|---|---|
| Population | You have every record in scope | `std(ddof=0)` calculates population standard deviation |
| Sample | You have part of the records and are estimating the whole | `std()` uses sample standard deviation by default |

Example:

```python
sample_std = df["Actual"].std()
population_std = df["Actual"].std(ddof=0)
```

For most business review work, the difference is small when there are many records. It can matter when the dataset is small.

## 27.14 Distribution shape: balanced, skewed, and multimodal

Do not rely only on a table of numbers. The shape of the data changes how statistics should be read.

Common shapes:

| Shape | What it means | What to use |
|---|---|---|
| Balanced | Values are fairly even around the center | Mean and standard deviation are often useful |
| Right-skewed | Most values are low, with a few very high values | Median, percentiles, and IQR are often useful |
| Left-skewed | Most values are high, with a few very low values | Median, percentiles, and IQR are often useful |
| Multimodal | There are multiple common clusters | Segment the data into groups before summarizing |

Quick checks:

```python
df["Actual"].describe()
df["Actual"].skew()
df["Actual"].plot(kind="hist", bins=20)
```

If the histogram has separate clusters, one overall average may hide important group differences.

## 27.15 Practical interpretation checklist

When reading statistics, ask:

1. What question am I answering?
2. What is the sample size?
3. What is the denominator?
4. Are missing values included, excluded, or reported separately?
5. Are there outliers?
6. Is the data skewed?
7. Is mean or median more appropriate?
8. Are totals more important than averages?
9. Are grouped statistics hiding important details?
10. Are percentages based on comparable groups?
11. Does correlation need a scatter plot before interpretation?
12. Does the statistic answer the business question?
13. What decision, risk, or follow-up action does the statistic suggest?

## 27.16 A practical statistics workflow in pandas

Use this workflow when starting an analysis.

### Step 1: Understand the rows and columns

```python
df.shape
df.dtypes
df.head()
```

Ask:

- What does one row represent?
- Which columns are numeric?
- Which columns are categories?
- Which columns contain dates?

### Step 2: Check missingness

```python
missing = df.isna().sum().sort_values(ascending=False)
missing_pct = df.isna().mean().mul(100).sort_values(ascending=False)
```

Ask whether missing values are random, expected, or a data-quality problem.

### Step 3: Summarize numeric columns

```python
numeric_summary = df.describe(percentiles=[0.25, 0.5, 0.75, 0.9, 0.95])
```

Look for very large gaps between mean and median, unusually high maximums, and suspicious minimums.

### Step 4: Summarize categorical columns

```python
status_counts = df["Status"].value_counts(dropna=False)
status_pct = df["Status"].value_counts(normalize=True, dropna=False) * 100
```

Look for unexpected categories, spelling variations, missing categories, and dominant categories.

### Step 5: Compare groups

```python
group_summary = df.groupby("Region").agg(
    Records=("Order", "count"),
    Total_Actual=("Actual", "sum"),
    Average_Actual=("Actual", "mean"),
    Median_Actual=("Actual", "median"),
    P90_Actual=("Actual", lambda s: s.quantile(0.90))
).reset_index()
```

Look for groups with high totals, high typical values, unusually wide spread, or very small record counts.

### Step 6: Check relationships

```python
relationship = df[["Budgeted", "Actual", "Variance"]].corr()
```

Use correlation as a clue, then inspect charts and business context.

### Step 7: Write an insight statement

A useful insight statement includes statistic, context, and implication.

Template:

```text
[Group or measure] had [statistic], based on [count/denominator], which suggests [business meaning or next step].
```

Example:

```text
The West region had the highest median actual amount at $1,420, based on 318 orders, which suggests the typical West order is larger than in other regions and should be reviewed separately from total volume.
```

---

# Part III: Charts and Plots

This part focuses on visual analysis. It separates chart-reading skills from the statistics chapter and shows how to create, read, and explain common plot types.

---

# 28. Charts for Understanding Statistics

## 28.1 Mean, median, and mode chart

![Mean, Median, and Mode](pandas_manual_assets/stats_mean_median_mode.svg)

How to read this chart:

- The bars show how often values appear.
- The mean line shows the arithmetic average.
- The median line shows the middle value.
- The mode line shows the most common value.
- The large value on the right pulls the mean higher.

Code to generate a similar chart:

```python
import pandas as pd
import matplotlib.pyplot as plt

values = pd.Series([2, 3, 3, 4, 4, 4, 5, 6, 7, 20])

mean_val = values.mean()
median_val = values.median()
mode_val = values.mode().iloc[0]

ax = values.plot(kind="hist", bins=10, edgecolor="black")
ax.axvline(mean_val, linestyle="--", label=f"Mean = {mean_val:.1f}")
ax.axvline(median_val, linestyle="-", label=f"Median = {median_val:.1f}")
ax.axvline(mode_val, linestyle=":", label=f"Mode = {mode_val:.1f}")
ax.legend()
plt.show()
```

## 28.2 Histogram distribution chart

![Histogram Distribution](pandas_manual_assets/plot_histogram_distribution.svg)

How to read this chart:

- The x-axis shows score ranges.
- The y-axis shows how many records fall into each range.
- Tall bars show common value ranges.
- If the chart has a long right tail, the data is right-skewed.
- If the chart has a long left tail, the data is left-skewed.

Use a histogram when you want to understand distribution.

## 28.3 Box plot chart

![Box Plot](pandas_manual_assets/plot_boxplot_quartiles_outliers.svg)

How to read this chart:

- The line inside the box is the median.
- The bottom of the box is Q1.
- The top of the box is Q3.
- The box itself contains the middle 50% of the data.
- The whiskers show typical low/high range.
- Points outside the whiskers are possible outliers.

Use a box plot when comparing spread between groups.

## 28.4 Correlation heatmap

![Correlation Heatmap](pandas_manual_assets/plot_correlation_heatmap.svg)

How to read this chart:

- Each cell compares two numeric variables.
- Values close to `1` mean strong positive relationship.
- Values close to `-1` mean strong negative relationship.
- Values close to `0` mean weak linear relationship.
- The diagonal is always `1` because each variable perfectly correlates with itself.

## 28.5 Chart-reading foundations for non-mathematicians

Charts are visual summaries. They do not replace the data; they help you notice patterns faster than reading every row. A good chart should answer one clear question, such as "Are orders increasing?", "Which customer has the highest total?", or "Are there unusual values that need review?"

Before interpreting any chart, identify these parts:

- **Title:** tells you the main subject. If the title is vague, ask what question the chart is supposed to answer.
- **X-axis:** usually shows time, categories, or value ranges. Read the labels before comparing anything.
- **Y-axis:** shows the measured amount, count, percentage, dollars, rate, or score. Check the units.
- **Legend:** explains colors, lines, markers, or groups. A chart with multiple colors is hard to read without a clear legend.
- **Scale:** tells you how big the numbers are. A chart that starts at 90 instead of 0 can make small differences look dramatic.
- **Source and filters:** tell you which records were included or excluded. A chart filtered to one region should not be interpreted as the entire business.

A simple reading process:

1. **Read the title and labels first.** Do not interpret the shape until you know what the chart measures.
2. **Look for the biggest message.** Is one category clearly largest? Is the line rising? Is the distribution concentrated?
3. **Check the scale.** Are numbers dollars, percentages, counts, thousands, or millions? Does the axis start at zero?
4. **Compare only like with like.** Counts, percentages, dollars, averages, and rates answer different questions.
5. **Look for exceptions.** Outliers, gaps, sudden drops, or unusual categories often identify records to inspect.
6. **Ask what action follows.** A useful chart should lead to a decision, question, investigation, or confirmation.

## 28.6 Insight vocabulary: what a chart can tell you

When you describe a chart, use practical words instead of statistical jargon whenever possible:

| Pattern | Plain-English meaning | Example business question |
|---|---|---|
| **Trend** | Values generally move up, down, or stay flat over time. | Are monthly orders increasing? |
| **Spike** | A sudden unusually high value. | Was there a one-time rush order or data error? |
| **Drop** | A sudden unusually low value. | Did volume fall because of a process issue or missing data? |
| **Seasonality** | A pattern repeats by day, month, quarter, or season. | Are Mondays heavier than Fridays? |
| **Ranking** | Categories can be ordered from highest to lowest. | Which customer creates the most work? |
| **Share** | Each category contributes part of a total. | What percent of orders came through each method? |
| **Distribution** | Shows common, rare, low, high, and typical values. | What is a normal processing time? |
| **Spread** | Values are tightly grouped or widely different. | Are reviewers producing consistent results? |
| **Outlier** | A value is far away from most other values. | Which records need manual review? |
| **Relationship** | Two measures tend to move together, apart, or not at all. | Do more units usually mean more profit? |
| **Cluster** | Records form visible groups. | Are there different types of customers or orders? |

## 28.7 Chart integrity checklist

Use this checklist before trusting a chart in a report or presentation:

- Does the chart answer one specific question?
- Are the title, axes, legend, and units clear?
- Is the data source stated or understood?
- Are important filters shown?
- Are missing values handled intentionally?
- Are totals, averages, and percentages labeled correctly?
- Are categories sorted in a meaningful order?
- Does the y-axis scale exaggerate or hide differences?
- Are there too many colors, labels, or categories?
- Is the chart type appropriate for the question?

A chart can be technically correct and still confusing. If a reader cannot explain the main point in one sentence, simplify the chart or add a short interpretation note.

## 28.8 Chart selection decision table

Choose a chart by starting with the question, the field types, and the comparison you want the reader to make.

| Analysis question | Data needed | Strong chart choices | What the reader should learn |
|---|---|---|---|
| How did a measure change over time? | Date/time column plus numeric measure | Line chart, area chart | Direction, trend, seasonality, spikes, and drops. |
| Which category is largest? | Category plus numeric measure | Sorted bar chart, horizontal bar chart | Ranking and size differences. |
| What share belongs to each category? | Category plus counts or totals | Percentage bar, 100% stacked bar, simple pie only for few categories | Composition of the whole. |
| What values are typical or unusual? | Numeric column | Histogram, box plot | Distribution, center, spread, skew, and outliers. |
| Are two numeric measures related? | Two numeric columns | Scatter plot, correlation heatmap for many columns | Direction and strength of relationship. |
| How do groups compare over time? | Date/time, group, numeric measure | Small multiples, grouped lines, faceted charts | Whether groups follow similar or different patterns. |
| What causes most of the problem? | Category plus count or total | Pareto chart | The few categories that contribute most. |
| Did something improve after a change? | Before and after measures | Before/after bars, slope chart, line chart | Size and direction of change. |

## 28.9 Measures, dimensions, and grain

Most chart mistakes come from misunderstanding what each row means. Before building a chart, identify these three ideas:

- **Measure:** the number being summarized, such as `Actual`, `Revenue`, `Orders`, `Profit`, or `Processing_Days`.
- **Dimension:** the category or time field used to split the measure, such as `Customer`, `Region`, `Month`, `Status`, or `Reviewer`.
- **Grain:** what one row represents, such as one order, one line item, one customer-month, or one daily total.

Example:

```python
monthly_customer = df.groupby(["Month", "Customer"], as_index=False).agg(
    Total_Actual=("Actual", "sum"),
    Order_Count=("Order", "nunique")
)
```

Interpretation:

- `Actual` is the measure.
- `Month` and `Customer` are dimensions.
- The summary grain is one row per month per customer.

If the grain is wrong, the chart may double-count records or hide important detail. For example, plotting line-item totals by customer may answer a different question than plotting order totals by customer.

## 28.10 The chart title should contain the answer

A weak title names the chart. A strong title explains the message.

| Weak title | Stronger title |
|---|---|
| `Revenue Chart` | `Revenue Increased Each Month from January to June` |
| `Customer Actuals` | `West Shop Had the Highest Actual Amount` |
| `Status Mix` | `Late Orders Were Concentrated in the West Region` |
| `Processing Days` | `Most Orders Finished Within 12 Days, with Three Outliers` |

Use a neutral title when the chart is exploratory. Use an insight title when the chart is part of a report and the evidence supports the conclusion.

## 28.11 When not to make a chart

A chart is not always the best output. Sometimes a table or sentence is clearer.

Use a table instead when:

- The reader needs exact values for many rows.
- There are many columns that must be compared together.
- The data is mostly IDs, names, notes, or exceptions.
- The audience needs to copy values into another process.

Use a sentence instead when:

- There is only one number to report.
- The conclusion is simple and does not need visual comparison.
- A chart would add decoration but not understanding.

Example:

```text
There were 18 late orders in May, representing 6.4% of May orders.
```

That sentence may be clearer than a chart if no comparison is needed.

---

# 29. Plotting with pandas and Matplotlib

pandas has a `.plot()` method that uses Matplotlib behind the scenes.

Basic setup:

```python
import pandas as pd
import matplotlib.pyplot as plt
```

Example dataset:

```python
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Revenue": [12500, 13200, 15100, 14800, 17400, 18900],
    "Cost": [8000, 8200, 9000, 9100, 10300, 11100],
    "Orders": [80, 85, 92, 89, 101, 108]
})

df["Profit"] = df["Revenue"] - df["Cost"]
```

## 29.1 Line plot

![Line Plot](pandas_manual_assets/plot_line_over_time.svg)

Use a line plot for trends over time.

```python
ax = df.plot(x="Month", y=["Revenue", "Cost"], kind="line", marker="o")
ax.set_title("Revenue and Cost Over Time")
ax.set_xlabel("Month")
ax.set_ylabel("Amount")
plt.show()
```

How to read it:

- The x-axis usually represents time.
- The y-axis represents the measured value.
- Upward movement means increase.
- Downward movement means decrease.
- Lines help compare trends between variables.

## 29.2 Bar plot

![Bar Plot](pandas_manual_assets/plot_bar_profit.svg)

Use a bar plot to compare categories.

```python
ax = df.plot(x="Month", y="Profit", kind="bar")
ax.set_title("Profit by Month")
ax.set_xlabel("Month")
ax.set_ylabel("Profit")
plt.show()
```

How to read it:

- Each bar is one category.
- Taller bars mean larger values.
- Compare bar heights to identify highest and lowest categories.

## 29.3 Horizontal bar plot

![Horizontal Bar Plot](pandas_manual_assets/plot_horizontal_bar_profit.svg)

```python
ax = df.plot(x="Month", y="Profit", kind="barh")
ax.set_title("Profit by Month")
ax.set_xlabel("Profit")
ax.set_ylabel("Month")
plt.show()
```

Use horizontal bars when category labels are long.

## 29.4 Histogram

![Histogram](pandas_manual_assets/plot_histogram_distribution.svg)

```python
ax = df["Orders"].plot(kind="hist", bins=5, edgecolor="black")
ax.set_title("Distribution of Order Counts")
ax.set_xlabel("Orders")
plt.show()
```

Use a histogram to understand how values are distributed.

## 29.5 Box plot

![Box Plot](pandas_manual_assets/plot_boxplot_quartiles_outliers.svg)

```python
ax = df[["Revenue", "Cost", "Profit"]].plot(kind="box")
ax.set_title("Distribution of Revenue, Cost, and Profit")
plt.show()
```

Use box plots to compare median, spread, and outliers.

## 29.6 Scatter plot

![Scatter Plot](pandas_manual_assets/plot_scatter_relationship.svg)

Use a scatter plot to inspect the relationship between two numeric variables.

```python
ax = df.plot(x="Orders", y="Profit", kind="scatter")
ax.set_title("Orders vs Profit")
ax.set_xlabel("Orders")
ax.set_ylabel("Profit")
plt.show()
```

How to read it:

- Each dot is one record.
- If dots rise from left to right, the relationship is positive.
- If dots fall from left to right, the relationship is negative.
- If dots are random, there may be little relationship.

## 29.7 Area plot

![Area Plot](pandas_manual_assets/plot_area_volume.svg)

Use an area plot to emphasize volume over time.

```python
ax = df.plot(x="Month", y=["Revenue", "Cost"], kind="area", alpha=0.4)
ax.set_title("Revenue and Cost Volume")
ax.set_ylabel("Amount")
plt.show()
```

How to read it:

- Larger filled area means larger total volume.
- It is useful for trends and cumulative-looking comparisons.
- Be careful: overlapping areas can sometimes be misleading.

## 29.8 Pie chart

![Pie Chart](pandas_manual_assets/plot_pie_share.svg)

Use pie charts only for simple part-to-whole comparisons.

```python
method_counts = pd.Series({
    "Faxed Operations": 42,
    "Website Orders": 28,
    "Mailed Operations": 18,
    "Projects": 12
})

ax = method_counts.plot(kind="pie", autopct="%1.1f%%")
ax.set_ylabel("")
ax.set_title("Share of Work by Method")
plt.show()
```

How to read it:

- The full circle is 100%.
- Each slice is a category's share.
- Bigger slices represent larger percentages.

Avoid pie charts when:

- There are too many categories.
- Values are very similar.
- You need precise comparison.

## 29.9 Density plot

![Density Plot](pandas_manual_assets/plot_density_profit.svg)

```python
ax = df["Profit"].plot(kind="kde")
ax.set_title("Profit Density")
plt.show()
```

A density plot is a smooth estimate of distribution. It is useful for seeing shape, but it can be less intuitive than a histogram for beginners.

## 29.10 Correlation heatmap without seaborn

![Correlation Heatmap](pandas_manual_assets/plot_correlation_heatmap.svg)

```python
corr = df[["Revenue", "Cost", "Profit", "Orders"]].corr()

fig, ax = plt.subplots()
im = ax.imshow(corr.values, vmin=-1, vmax=1)

ax.set_xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right")
ax.set_yticks(range(len(corr.index)), corr.index)

for i in range(len(corr.index)):
    for j in range(len(corr.columns)):
        ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center")

fig.colorbar(im, ax=ax)
plt.show()
```

## 29.11 Save a plot

```python
ax = df.plot(x="Month", y="Profit", kind="bar")
fig = ax.get_figure()
fig.savefig("profit_by_month.png", dpi=150, bbox_inches="tight")
```

## 29.12 Improve labels

```python
ax = df.plot(x="Month", y="Profit", kind="bar")
ax.set_title("Profit by Month")
ax.set_xlabel("Month")
ax.set_ylabel("Profit ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

Clear labels are not cosmetic. They make the chart understandable.

## 29.13 Add reference lines and annotations

![Reference Line and Annotation](pandas_manual_assets/plot_reference_annotation.svg)

Reference lines help readers compare values to a target, average, budget, or threshold. An annotation calls attention to one important point.

```python
ax = df.plot(x="Month", y="Profit", kind="bar", legend=False)
average_profit = df["Profit"].mean()

ax.axhline(average_profit, color="red", linestyle="--", label="Average profit")
ax.annotate(
    "Highest profit",
    xy=(df["Profit"].idxmax(), df["Profit"].max()),
    xytext=(df["Profit"].idxmax(), df["Profit"].max() + 1000),
    arrowprops={"arrowstyle": "->"}
)
ax.set_title("Profit by Month Compared with Average")
ax.set_xlabel("Month")
ax.set_ylabel("Profit ($)")
ax.legend()
plt.tight_layout()
plt.show()
```

Use reference lines when the reader needs to know whether a value is above or below a standard. Use annotations sparingly; too many notes make the chart harder to read.

## 29.14 Format numbers for readable charts

![Formatted Revenue Chart](pandas_manual_assets/plot_formatted_revenue.svg)

Large numbers and percentages should be formatted so the reader does not have to mentally decode them.

```python
from matplotlib.ticker import FuncFormatter, PercentFormatter

def dollars(value, position):
    return f"${value:,.0f}"

ax = df.plot(x="Month", y="Revenue", kind="line", marker="o")
ax.yaxis.set_major_formatter(FuncFormatter(dollars))
ax.set_title("Revenue by Month")
ax.set_ylabel("Revenue")
plt.tight_layout()
plt.show()
```

Percentage example:

```python
status_share = pd.Series({"On Time": 0.82, "Late": 0.18})
ax = status_share.plot(kind="bar")
ax.yaxis.set_major_formatter(PercentFormatter(xmax=1))
ax.set_title("Order Timeliness Share")
plt.tight_layout()
plt.show()
```

## 29.15 Plot grouped summaries from pandas

![Grouped Summary Plot](pandas_manual_assets/plot_grouped_summary_profit.svg)

Most useful business charts start with a grouped summary rather than raw rows.

```python
customer_profit = (
    df.groupby("Month", as_index=False)
      .agg(Total_Profit=("Profit", "sum"), Order_Count=("Orders", "sum"))
)

ax = customer_profit.plot(x="Month", y="Total_Profit", kind="bar", legend=False)
ax.set_title("Total Profit by Month")
ax.set_xlabel("Month")
ax.set_ylabel("Total Profit")
plt.tight_layout()
plt.show()
```

The chart should match the summary table. If the table says the highest month is June, the tallest bar should also be June. This is a simple but important quality check.

## 29.16 Small multiples for cleaner comparisons

![Small Multiples Plot](pandas_manual_assets/plot_small_multiples_regions.svg)

A chart with too many lines can become unreadable. Instead, use separate panels with the same scale.

```python
monthly = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"] * 2,
    "Region": ["East"] * 4 + ["West"] * 4,
    "Orders": [40, 45, 50, 48, 30, 42, 44, 52]
})

axes = monthly.pivot(index="Month", columns="Region", values="Orders").plot(
    kind="line",
    marker="o",
    subplots=True,
    layout=(1, 2),
    sharey=True,
    figsize=(8, 3)
)
plt.tight_layout()
plt.show()
```

Small multiples are useful when each group deserves comparison but putting every group on one chart would create a spaghetti chart.

## 29.17 Sort bars so the message is obvious

![Sorted Horizontal Bars](pandas_manual_assets/plot_sorted_horizontal_bars.svg)

Bar charts are easiest to read when categories are sorted by value, unless the categories already have a natural order such as months, workflow stages, or priority levels.

```python
customer_summary = pd.DataFrame({
    "Customer": ["North Co", "West Shop", "Online", "South LLC"],
    "Total_Actual": [2200, 3400, 950, 1800]
})

ordered = customer_summary.sort_values("Total_Actual", ascending=True)

ax = ordered.plot(x="Customer", y="Total_Actual", kind="barh", legend=False)
ax.set_title("Total Actual Amount by Customer")
ax.set_xlabel("Actual Amount ($)")
ax.set_ylabel("Customer")
plt.tight_layout()
plt.show()
```

Interpretation:

- The longest horizontal bar is the largest customer by actual amount.
- Horizontal bars work well when labels are long.
- Sorting from smallest to largest places the largest bar at the top in many rendered charts, which is often easier for readers.

## 29.18 Show percentages as a 100% stacked bar

![100 Percent Stacked Bar](pandas_manual_assets/plot_stacked_percent_status.svg)

A regular stacked bar shows total size and category composition. A **100% stacked bar** shows composition only. This is useful when you want to compare percentages across groups even if the groups have different total volumes.

```python
from matplotlib.ticker import PercentFormatter

status_counts = pd.DataFrame({
    "Region": ["East", "West", "South"],
    "On_Time": [90, 50, 40],
    "Late": [10, 25, 5],
    "Review": [5, 10, 5]
})

status_pct = status_counts.set_index("Region")
status_pct = status_pct.div(status_pct.sum(axis=1), axis=0)

ax = status_pct.plot(kind="bar", stacked=True)
ax.yaxis.set_major_formatter(PercentFormatter(xmax=1))
ax.set_title("Order Status Mix by Region")
ax.set_xlabel("Region")
ax.set_ylabel("Percent of Orders")
plt.legend(title="Status", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()
plt.show()
```

How to read it:

- Each bar equals 100% for that region.
- The colored sections show the share of each status inside the region.
- Use this when the question is about mix, not total count.
- If total volume also matters, show a count table or a second chart beside it.

## 29.19 Pareto chart for the biggest contributors

![Pareto Chart](pandas_manual_assets/plot_pareto_issues.svg)

A Pareto chart combines bars and a cumulative-percentage line. It helps answer: "Which few categories explain most of the total?"

```python
from matplotlib.ticker import PercentFormatter

issues = pd.Series({
    "Missing Info": 42,
    "Price Mismatch": 30,
    "Late Shipment": 18,
    "Duplicate": 7,
    "Other": 5
}).sort_values(ascending=False)

pareto = pd.DataFrame({"Count": issues})
pareto["Cumulative_Percent"] = pareto["Count"].cumsum() / pareto["Count"].sum()

fig, ax1 = plt.subplots()
pareto["Count"].plot(kind="bar", ax=ax1, color="steelblue")
ax1.set_ylabel("Issue Count")
ax1.set_title("Pareto Chart of Issue Types")

ax2 = ax1.twinx()
pareto["Cumulative_Percent"].plot(ax=ax2, color="darkorange", marker="o")
ax2.yaxis.set_major_formatter(PercentFormatter(xmax=1))
ax2.set_ylabel("Cumulative Percent")
plt.tight_layout()
plt.show()
```

Interpretation:

- The bars show the largest issue types.
- The line shows how quickly those issue types add up toward 100%.
- If the first two bars explain most of the total, improving those two issues may have the biggest impact.

## 29.20 Before-and-after comparison

![Before and After Comparison](pandas_manual_assets/plot_before_after_comparison.svg)

Use a before-and-after chart when you want to show change between two points, such as before and after a process update.

```python
before_after = pd.DataFrame({
    "Metric": ["Average Days", "Late Orders", "Manual Reviews"],
    "Before": [8.5, 32, 45],
    "After": [5.2, 18, 29]
})

ax = before_after.plot(x="Metric", y=["Before", "After"], kind="bar")
ax.set_title("Before-and-After Process Comparison")
ax.set_xlabel("Metric")
ax.set_ylabel("Value")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()
```

How to read it:

- Compare the two bars within each metric.
- Lower may be better for some metrics, such as days or late orders.
- Always state whether higher or lower is better so the reader does not guess.

## 29.21 Dual-axis charts: use carefully

![Dual Axis Chart](pandas_manual_assets/plot_dual_axis_revenue_orders.svg)

A dual-axis chart uses one y-axis on the left and another y-axis on the right. It can be useful when two measures have very different units, but it can also mislead readers because the line shapes depend on the chosen scales.

```python
fig, ax1 = plt.subplots()

df.plot(x="Month", y="Revenue", kind="bar", ax=ax1, color="lightsteelblue", legend=False)
ax1.set_ylabel("Revenue ($)")

ax2 = ax1.twinx()
df.plot(x="Month", y="Orders", kind="line", marker="o", ax=ax2, color="darkorange", legend=False)
ax2.set_ylabel("Orders")

ax1.set_title("Revenue and Orders by Month")
plt.tight_layout()
plt.show()
```

Use a dual-axis chart only when:

- The two measures are clearly labeled.
- The chart is for high-level comparison, not precise proof.
- You explain that the axes use different scales.

If the audience may be confused, use two aligned charts instead.

## 29.22 Plotting missing values intentionally

![Missing Values Gap Plot](pandas_manual_assets/plot_missing_values_gap.svg)

Missing values can create gaps or misleading lines. Decide whether missing means "zero," "not collected," or "not applicable." These are different meanings.

```python
series = pd.Series(
    [100, 120, None, 150, 160],
    index=pd.to_datetime(["2026-01-01", "2026-02-01", "2026-03-01", "2026-04-01", "2026-05-01"])
)

ax = series.plot(marker="o")
ax.set_title("Monthly Value with Missing March Data")
ax.set_xlabel("Month")
ax.set_ylabel("Value")
plt.tight_layout()
plt.show()
```

Options:

```python
# Keep the gap so readers see data was missing.
series_with_gap = series

# Fill only when zero is the true business meaning.
series_zero_filled = series.fillna(0)

# Interpolate only when estimating between known points makes sense.
series_interpolated = series.interpolate()
```

Do not fill missing values just to make a chart look smooth. The visual should represent the business truth.

## 29.23 A reusable plotting pattern

Most good pandas charts follow the same pattern:

1. Build a clean summary table.
2. Sort or reshape the summary for the message.
3. Plot the summary, not messy raw rows.
4. Add title, axis labels, units, and formatting.
5. Write the interpretation.

```python
summary = (
    df.groupby("Customer", as_index=False)
      .agg(Total_Actual=("Actual", "sum"), Orders=("Order", "nunique"))
      .sort_values("Total_Actual", ascending=False)
)

ax = summary.head(10).plot(
    x="Customer",
    y="Total_Actual",
    kind="bar",
    legend=False,
    color="steelblue"
)

ax.set_title("Top 10 Customers by Total Actual Amount")
ax.set_xlabel("Customer")
ax.set_ylabel("Actual Amount ($)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
```

Quality check:

```python
summary.head(10)
```

Always inspect the summary table behind the chart. If the table is wrong, the chart will also be wrong.

## 29.24 Wide data vs long data for plotting

pandas can plot both wide and long data, but each shape is useful for different tasks.

Wide data has one column per measure or group:

```python
wide = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar"],
    "Revenue": [12500, 13200, 15100],
    "Cost": [8000, 8200, 9000]
})

wide.plot(x="Month", y=["Revenue", "Cost"], kind="line")
```

Long data has one row per measure or group:

```python
long = wide.melt(
    id_vars="Month",
    value_vars=["Revenue", "Cost"],
    var_name="Measure",
    value_name="Amount"
)
```

Long data is often better for filtering, grouping, and using libraries that expect tidy data. Wide data is often convenient for quick pandas plots with multiple lines or bars.

## 29.25 Grouped bar charts

Use grouped bars when you need to compare categories inside another category.

```python
status_by_region = pd.DataFrame({
    "Region": ["East", "West", "South"],
    "On_Time": [90, 50, 40],
    "Late": [10, 25, 5]
}).set_index("Region")

ax = status_by_region.plot(kind="bar")
ax.set_title("On-Time and Late Orders by Region")
ax.set_xlabel("Region")
ax.set_ylabel("Order Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
```

Interpretation:

- Compare bars within each region to understand status mix.
- Compare the same color across regions to understand where each status is highest.
- If there are too many statuses or regions, use a table, small multiples, or a heatmap instead.

## 29.26 Date axes and time order

Time charts should be sorted by actual dates, not alphabetic month names.

```python
daily = pd.DataFrame({
    "Date": pd.to_datetime(["2026-01-03", "2026-01-01", "2026-01-02"]),
    "Orders": [82, 75, 79]
}).sort_values("Date")

ax = daily.plot(x="Date", y="Orders", kind="line", marker="o")
ax.set_title("Daily Orders")
ax.set_xlabel("Date")
ax.set_ylabel("Orders")
plt.tight_layout()
plt.show()
```

For month names, create a real date or an ordered categorical column so the chart does not sort months alphabetically.

```python
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
df["Month"] = pd.Categorical(df["Month"], categories=month_order, ordered=True)
df = df.sort_values("Month")
```

## 29.27 Data labels and annotations

Data labels can help readers, but too many labels create clutter. Label the most important values instead of every value.

```python
ax = summary.head(10).plot(x="Customer", y="Total_Actual", kind="bar", legend=False)
ax.set_title("Top 10 Customers by Total Actual Amount")
ax.set_ylabel("Actual Amount ($)")

largest = summary.head(10).iloc[0]
ax.annotate(
    f"Highest: ${largest['Total_Actual']:,.0f}",
    xy=(0, largest["Total_Actual"]),
    xytext=(0.5, largest["Total_Actual"] * 1.05),
    arrowprops={"arrowstyle": "->"}
)

plt.tight_layout()
plt.show()
```

Use annotations for:

- Highest or lowest value.
- Target misses.
- Sudden spikes or drops.
- Known business events.
- Data-quality warnings.

## 29.28 Color, accessibility, and emphasis

Color should communicate meaning. Do not rely only on red and green because some readers may not distinguish those colors easily.

Practical color rules:

- Use one main color for neutral bars or lines.
- Use a highlight color only for the item that needs attention.
- Use consistent colors for the same category across charts.
- Avoid rainbow palettes for ordered values.
- Use line style, markers, labels, or annotations in addition to color.

Example highlighting one category:

```python
colors = ["darkorange" if customer == "West Shop" else "lightgray"
          for customer in summary["Customer"].head(10)]

ax = summary.head(10).plot(
    x="Customer",
    y="Total_Actual",
    kind="bar",
    legend=False,
    color=colors
)
ax.set_title("West Shop Had the Highest Actual Amount")
ax.set_ylabel("Actual Amount ($)")
plt.tight_layout()
plt.show()
```

## 29.29 Saving charts for reports

Use a consistent size, resolution, and file naming pattern when saving charts.

```python
fig = ax.get_figure()
fig.savefig(
    "top_customers_actual_amount.png",
    dpi=150,
    bbox_inches="tight",
    facecolor="white"
)
```

Practical tips:

- Use `.png` for reports and slides.
- Use `.svg` when you need scalable graphics.
- Use `bbox_inches="tight"` to prevent labels from being cut off.
- Save the summary table next to the chart when the chart supports a decision.

```python
summary.to_excel("top_customers_actual_amount_summary.xlsx", index=False)
```

---

# 30. How to Read Common Plot Types

## 30.1 Line plot

![Line Plot](pandas_manual_assets/plot_line_over_time.svg)

Best for:

- Trends over time.
- Monthly volume.
- Daily production.
- Revenue over time.

Look for:

- Upward trends.
- Downward trends.
- Sudden jumps.
- Flat periods.
- Seasonality.

## 30.2 Bar plot

![Bar Plot](pandas_manual_assets/plot_bar_profit.svg)

Best for:

- Comparing categories.
- Reviewer productivity.
- Orders by customer.
- Revenue by product category.

Look for:

- Highest category.
- Lowest category.
- Large gaps.
- Unexpected categories.

## 30.3 Histogram

![Histogram](pandas_manual_assets/plot_histogram_distribution.svg)

Best for:

- Distribution of numeric values.
- Understanding typical ranges.
- Detecting skew.
- Seeing if data is concentrated or spread out.

Look for:

- One peak or multiple peaks.
- Left or right skew.
- Gaps.
- Extreme bars.

## 30.4 Box plot

![Box Plot](pandas_manual_assets/plot_boxplot_quartiles_outliers.svg)

Best for:

- Comparing groups.
- Outlier detection.
- Seeing median and spread.

Look for:

- Median line.
- Box height.
- Whisker length.
- Outlier points.

## 30.5 Scatter plot

![Scatter Plot](pandas_manual_assets/plot_scatter_relationship.svg)

Best for:

- Relationship between two numeric variables.
- Detecting clusters.
- Detecting unusual records.

Look for:

- Positive relationship.
- Negative relationship.
- No relationship.
- Outliers.
- Clusters.

## 30.6 Pie chart

![Pie Chart](pandas_manual_assets/plot_pie_share.svg)

Best for:

- Simple part-to-whole percentages.

Look for:

- Largest slice.
- Smallest slice.
- Whether categories add up logically.

Avoid for detailed comparisons.

## 30.7 Heatmap

![Correlation Heatmap](pandas_manual_assets/plot_correlation_heatmap.svg)

Best for:

- Correlations.
- Matrix-style comparisons.
- Pattern detection across two dimensions.

Look for:

- Strong positive values.
- Strong negative values.
- Blocks of similar values.

## 30.8 Which chart should I use?

Start with the question, not the chart. The same data can produce many charts, but only a few will answer the question clearly.

| If your question is... | Use this chart | Why | Avoid |
|---|---|---|---|
| "How has this changed over time?" | Line chart | Shows direction, trend, and timing. | Pie chart |
| "Which category is biggest or smallest?" | Bar chart | Makes category comparison easy. | Pie chart with many slices |
| "What is the total volume over time?" | Area chart or line chart | Emphasizes size and trend. | Stacked area with too many groups |
| "What share of the whole does each category represent?" | Bar chart with percentages or simple pie chart | Shows part-to-whole relationship. | Pie chart with similar-sized slices |
| "What values are typical, high, low, or unusual?" | Histogram or box plot | Shows distribution and outliers. | Line chart |
| "Are two numeric measures related?" | Scatter plot | Shows relationship, clusters, and unusual records. | Bar chart |
| "Which combinations are high or low?" | Heatmap | Shows patterns across rows and columns. | 3-D charts |
| "Are groups different from each other?" | Box plot, grouped bar chart, or small multiples | Compares centers, spread, or totals by group. | One overcrowded chart |

A practical rule: if readers need to compare exact sizes, use bars. If readers need to see movement over time, use lines. If readers need to see the shape of numeric values, use histograms or box plots.

## 30.9 What each chart type is not good for

Understanding limitations prevents misleading conclusions.

- **Line plots** are not ideal for unordered categories. Connecting unrelated categories implies a sequence that may not exist.
- **Bar plots** can hide what is happening inside each category. A bar showing an average may hide extreme values.
- **Histograms** depend on bin size. Different bins can make the same data look smoother, rougher, or more clustered.
- **Box plots** are compact but can feel abstract to beginners. Pair them with a short explanation or a table of medians.
- **Scatter plots** show association, not proof that one variable caused another.
- **Pie charts** are poor for precise comparison, rankings, negative values, or many categories.
- **Heatmaps** can exaggerate patterns if the color scale is poorly chosen. Always label the values or provide a clear color bar.

## 30.10 Common misleading chart problems

Watch for these issues when reviewing charts from any tool, including pandas, Excel, BI dashboards, or presentations:

1. **Truncated axis:** a y-axis that starts above zero can make small differences look large. This is especially risky with bar charts.
2. **Wrong denominator:** a percentage is meaningless unless you know what it is a percentage of.
3. **Mixed units:** do not compare dollars, counts, and rates as if they are the same measurement.
4. **Too many categories:** a crowded chart hides the message. Group small categories as "Other" when appropriate.
5. **Unsorted bars:** random category order makes comparison harder. Sort bars by value unless time or a required business order matters.
6. **Averages without counts:** an average based on 3 records should not be treated the same as an average based on 3,000 records.
7. **Ignoring missing data:** a drop may mean records are missing, not that performance changed.
8. **Correlation treated as causation:** two measures moving together does not prove one caused the other.
9. **Decorative 3-D effects:** 3-D charts distort size and make values harder to compare.
10. **Color without meaning:** colors should group, warn, highlight, or separate; they should not be random decoration.

## 30.11 Chart design rules that improve understanding

Use these rules for charts meant for non-technical readers:

- Put the main message in the title: "June Had the Highest Profit" is more useful than "Profit Chart."
- Label axes with units: "Profit ($)" is clearer than "Profit."
- Use consistent colors: for example, green for positive, red for negative, gray for reference.
- Sort categories intentionally: highest-to-lowest for rankings, calendar order for months, process order for workflow stages.
- Reduce clutter: remove unnecessary gridlines, extra decimals, and redundant legends.
- Show data labels only when they help. Labeling every point can create noise.
- Use annotations for the one or two points that require attention.
- Keep comparisons fair: use the same scale when comparing similar charts.
- Include the time period and filters in the chart title, subtitle, or surrounding text.

## 30.12 Turning a chart into an insight statement

A chart becomes useful when you can explain what it means. Use this sentence structure:

```text
[What changed or stands out] + [how much or where] + [why it matters or what to check next].
```

Examples:

- "Profit increased from January to June, with June highest at $7,800, so June's order mix should be reviewed for repeatable patterns."
- "West Shop has the largest negative variance, so those records should be checked for rush fees, pricing changes, or data-entry issues."
- "Most orders are between 80 and 100 units, but one month is far higher, so confirm whether it was a valid spike or a duplicate entry."
- "Orders and profit generally rise together, but two high-order months have low profit, so review cost or discount differences."

## 30.13 Chart-to-pandas workflow

A reliable workflow connects the visual back to the DataFrame:

1. **Prepare the data:** clean column names, convert dates, handle missing values, and validate numeric columns.
2. **Summarize the data:** use `groupby`, `pivot_table`, `value_counts`, or calculated columns.
3. **Check the summary table:** confirm totals, counts, percentages, and sorting before plotting.
4. **Create the chart:** choose the chart type based on the question.
5. **Improve readability:** add title, labels, formatting, legend, reference lines, and annotations.
6. **Interpret the result:** write a one-sentence insight and identify records that need deeper review.
7. **Save or export:** save the plot and, when useful, export the summary table used to make the chart.

Example:

```python
summary = (
    orders.groupby("Customer", as_index=False)
          .agg(Orders=("Reference", "nunique"), Total_Actual=("Actual", "sum"))
          .sort_values("Total_Actual", ascending=False)
)

ax = summary.plot(x="Customer", y="Total_Actual", kind="bar", legend=False)
ax.set_title("Total Actual Amount by Customer")
ax.set_xlabel("Customer")
ax.set_ylabel("Actual Amount ($)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
```

Interpretation: the tallest bar identifies the customer with the highest actual amount, but the `Orders` column in the summary table should also be checked because one large order and many small orders can create the same total.

## 30.14 Dashboard and report review checklist

When multiple charts appear together, review the whole page:

- What decision is the dashboard supposed to support?
- Are the date ranges and filters consistent across charts?
- Do totals in different charts reconcile with each other?
- Are the same colors used for the same categories across the page?
- Is the most important chart placed first or largest?
- Are there tables for details when a chart shows an exception?
- Are definitions clear, especially for metrics like "completed," "late," "savings," "variance," or "active"?
- Does the dashboard show both volume and rate when both matter? For example, late-order count and late-order percentage answer different questions.

## 30.15 Measures, dimensions, grain, and filters

Many chart mistakes happen before plotting. Four words help prevent confusion:

- **Measure:** the number being analyzed, such as sales, profit, order count, processing days, error rate, or variance.
- **Dimension:** the category or time field used to split the measure, such as customer, month, region, reviewer, status, or product line.
- **Grain:** what one row represents. One row might be one order, one line item, one customer per month, or one daily summary.
- **Filter:** which records are included, such as one month, one region, active customers only, or completed orders only.

Example questions:

| Question | Measure | Dimension | Grain | Filter |
|---|---|---|---|---|
| Which customer has the most actual spend? | Actual amount | Customer | Order or line item | Reporting period |
| Are late orders improving over time? | Late-order rate | Month | Order | Completed orders |
| Which reviewer handles the most work? | Order count | Reviewer | Order | Assigned orders |
| Which product line has the highest average variance? | Average variance | Product line | Order | Non-cancelled orders |

Before creating a chart, say the question out loud in this format:

```text
I want to compare [measure] by [dimension] for [filtered records] where each row represents [grain].
```

If you cannot complete that sentence, the chart definition is not clear enough yet.

## 30.16 Count, sum, average, percentage, and rate

Non-mathematicians often see a chart and ask, "Is that a count or a percent?" That question matters because each metric tells a different story.

| Metric type | What it answers | pandas pattern | Common mistake |
|---|---|---|---|
| Count | How many records? | `df.groupby("Status").size()` | Treating count as performance quality. |
| Sum | How much total value? | `df.groupby("Customer")["Actual"].sum()` | Ignoring that one large record can dominate. |
| Average | What is typical per record? | `df.groupby("Reviewer")["Days"].mean()` | Comparing averages without checking counts. |
| Median | What is the middle record? | `df.groupby("Customer")["Actual"].median()` | Forgetting that it ignores total volume. |
| Percentage | What share of the whole? | `counts / counts.sum()` | Not stating the denominator. |
| Rate | How often did something happen? | `late_orders / total_orders` | Comparing rates from very small samples. |

Example: one reviewer may have the highest number of late orders because they handled the most orders overall. A late-order **rate** may be fairer than a late-order **count**.

```python
reviewer = pd.DataFrame({
    "Reviewer": ["Ana", "Luis", "Maria"],
    "Orders": [120, 40, 20],
    "Late_Orders": [12, 8, 3]
})

reviewer["Late_Rate"] = reviewer["Late_Orders"] / reviewer["Orders"]
```

Interpretation:

- `Late_Orders` answers "how many late orders?"
- `Late_Rate` answers "what percent of each reviewer's orders were late?"
- Both can be important, but they should not be treated as the same metric.

## 30.17 Reading trends over time

![Line Plot for Reading Trends](pandas_manual_assets/plot_line_over_time.svg)

A time chart should usually be read in layers:

1. **Overall direction:** is the line generally rising, falling, or flat?
2. **Size of change:** is the change small, moderate, or large compared with the starting value?
3. **Volatility:** does the line move smoothly, or does it jump up and down?
4. **Turning points:** where did the direction change?
5. **Seasonality:** does the same pattern repeat by month, quarter, weekday, or season?
6. **Recent values:** are the latest periods better, worse, or normal compared with the past?

Useful pandas calculations for time charts:

```python
daily = df.sort_values("Date").set_index("Date")

monthly = daily.resample("ME").agg(
    Revenue=("Revenue", "sum"),
    Orders=("Orders", "sum")
)

monthly["Revenue_Change"] = monthly["Revenue"].diff()
monthly["Revenue_Pct_Change"] = monthly["Revenue"].pct_change()
monthly["Revenue_3_Month_Avg"] = monthly["Revenue"].rolling(3).mean()
```

Interpretation:

- `diff()` shows the absolute change from the previous period.
- `pct_change()` shows the percentage change from the previous period.
- `rolling(3).mean()` smooths short-term noise so the broader trend is easier to see.

## 30.18 Reading category comparisons

![Sorted Horizontal Bars for Category Comparison](pandas_manual_assets/plot_sorted_horizontal_bars.svg)

When comparing categories, ask whether the chart shows total volume, average performance, or share of total.

Good category-comparison questions:

- Which customer has the highest total spend?
- Which product line has the most orders?
- Which reviewer has the highest average processing time?
- Which status accounts for the largest share of records?
- Which category is unexpectedly small or missing?

A useful category chart often starts with this pattern:

```python
summary = (
    df.groupby("Category", as_index=False)
      .agg(
          Records=("Order_ID", "nunique"),
          Total_Actual=("Actual", "sum"),
          Average_Actual=("Actual", "mean")
      )
      .sort_values("Total_Actual", ascending=False)
)
```

Interpretation checklist:

- Are categories sorted in a meaningful way?
- Are small categories grouped as `Other` if there are too many?
- Are category names clean and consistent? For example, `North`, `north`, and `North ` may be the same category with messy spelling.
- Is the chart comparing totals when it should compare rates, or rates when it should compare totals?

## 30.19 Reading distributions without advanced math

![Box Plot for Distribution Reading](pandas_manual_assets/plot_boxplot_quartiles_outliers.svg)

A distribution shows how values are spread across low, middle, and high ranges. You do not need advanced math to read one.

Ask these questions:

- What values are most common?
- What values are rare?
- Is there one main group or more than one group?
- Is the data mostly low with a few very high values?
- Are there values that seem impossible or suspicious?

Practical examples:

- A histogram of processing days may show that most orders finish in 2 to 4 days, with a few taking 20 days. Those 20-day records need investigation.
- A box plot by reviewer may show that most reviewers have similar medians, but one reviewer has much wider spread. That may indicate a different work mix or inconsistent process.
- A distribution of actual amounts may be right-skewed because most orders are small and a few orders are very large. In that case, the median may describe a typical order better than the mean.

Useful pandas summary:

```python
df["Processing_Days"].describe(percentiles=[0.25, 0.5, 0.75, 0.9, 0.95])
```

The 90th or 95th percentile can be useful in business reports because it answers, "How high are the unusually high but still common-enough values?"

## 30.20 Reading relationships without assuming causation

![Scatter Plot for Relationship Reading](pandas_manual_assets/plot_scatter_relationship.svg)

Scatter plots and correlations can show that two numeric measures move together, but they do not prove cause and effect.

When reading a relationship chart, ask:

1. Do the points rise, fall, or form no clear pattern?
2. Are there clusters that suggest different groups?
3. Are there outliers that deserve separate review?
4. Could another factor explain the pattern?
5. Is the relationship strong enough to be useful for decisions?

Example:

```python
ax = df.plot(x="Orders", y="Profit", kind="scatter")
ax.set_title("Orders vs Profit")
ax.set_xlabel("Orders")
ax.set_ylabel("Profit ($)")
plt.tight_layout()
plt.show()

df[["Orders", "Profit"]].corr()
```

Interpretation:

- A positive pattern means higher order counts often appear with higher profit.
- It does not prove that increasing order count automatically increases profit. Pricing, discounts, product mix, cost, and customer type may also matter.
- Outliers may be more important than the overall relationship because they can identify unusual high-value or high-risk records.

## 30.21 Chart captions for business reports

A short caption can make a chart much easier to understand. A good caption contains:

- **Finding:** what stands out.
- **Evidence:** the number, group, or period that supports it.
- **Caution:** anything the reader should not over-assume.
- **Next step:** what to investigate or do.

Template:

```text
Finding: [main point]. Evidence: [specific value or comparison]. Caution: [limit of chart]. Next step: [action].
```

Example captions:

- `Finding: West Shop has the highest actual amount. Evidence: its bar is the largest in the customer summary. Caution: the chart shows total dollars, not number of orders. Next step: review whether the total is driven by many orders or one large order.`
- `Finding: Processing time improved after April. Evidence: the line drops for May and June. Caution: confirm that the same order types are included in all months. Next step: compare May and June by product line.`
- `Finding: A few records are much higher than the normal range. Evidence: the box plot shows outlier points. Caution: outliers may be valid large orders. Next step: inspect those records before removing them.`

## 30.22 Choosing colors for clarity and accessibility

Color should communicate meaning. It should not be decoration only.

Practical rules:

- Use one main color for normal bars or lines.
- Use an accent color to highlight the important category or exception.
- Use red/green carefully because some readers have color-vision limitations and because red/green can imply good/bad even when that is not intended.
- Do not rely on color alone. Use labels, legends, marker shapes, or annotations too.
- Keep the same category the same color across related charts.
- Use lighter colors for background or reference information and stronger colors for the main point.

Simple highlight example:

```python
summary = pd.DataFrame({
    "Customer": ["North Co", "West Shop", "Online", "South LLC"],
    "Total_Actual": [2200, 3400, 950, 1800]
}).sort_values("Total_Actual", ascending=False)

colors = ["darkorange" if value == summary["Total_Actual"].max() else "lightgray"
          for value in summary["Total_Actual"]]

ax = summary.plot(x="Customer", y="Total_Actual", kind="bar", color=colors, legend=False)
ax.set_title("Highest Customer by Actual Amount")
ax.set_ylabel("Actual Amount ($)")
plt.tight_layout()
plt.show()
```

The highlight tells the reader where to look first.

## 30.23 When a table is better than a chart

Charts are not always the answer. Use a table when readers need exact values, detailed records, or many fields at once.

Use a chart when:

- You need to show a pattern, trend, comparison, distribution, or relationship.
- The exact value is less important than the overall message.
- You want readers to spot exceptions quickly.

Use a table when:

- Readers need exact dollar amounts, IDs, dates, or names.
- There are only a few values and a chart would add clutter.
- You need to audit individual records.
- You need to show many columns of detail.

A strong report often uses both: a chart to identify the issue and a table to show the records behind it.

## 30.24 From question to final chart: a complete mini-example

![Over-Budget Amount by Customer](pandas_manual_assets/plot_over_budget_customer.svg)

Business question: "Which customers are driving over-budget actuals, and is the issue common or caused by a few orders?"

Step 1: start with order-level data and calculate the needed fields.

```python
orders = pd.DataFrame({
    "Reference": ["R001", "R002", "R003", "R004", "R005", "R006"],
    "Customer": ["North Co", "North Co", "West Shop", "West Shop", "Online", "North Co"],
    "Budgeted": [500, 750, 300, 1000, 250, 400],
    "Actual": [400, 900, 450, 1200, 250, 390]
})

orders["Variance"] = orders["Budgeted"] - orders["Actual"]
orders["Over_Budget"] = orders["Variance"] < 0
orders["Over_Budget_Amount"] = orders["Variance"].abs().where(orders["Over_Budget"], 0)
```

Step 2: summarize by customer.

```python
customer_risk = (
    orders.groupby("Customer", as_index=False)
          .agg(
              Orders=("Reference", "nunique"),
              Over_Budget_Orders=("Over_Budget", "sum"),
              Total_Over_Budget=("Over_Budget_Amount", "sum")
          )
)

customer_risk["Over_Budget_Rate"] = (
    customer_risk["Over_Budget_Orders"] / customer_risk["Orders"]
)
```

Step 3: chart the total over-budget amount.

```python
plot_data = customer_risk.sort_values("Total_Over_Budget", ascending=True)

ax = plot_data.plot(x="Customer", y="Total_Over_Budget", kind="barh", legend=False)
ax.set_title("Total Over-Budget Amount by Customer")
ax.set_xlabel("Over-Budget Amount ($)")
ax.set_ylabel("Customer")
plt.tight_layout()
plt.show()
```

Step 4: interpret with both amount and frequency.

```python
customer_risk.sort_values("Total_Over_Budget", ascending=False)
```

Interpretation:

- `Total_Over_Budget` shows where the largest dollar risk is.
- `Over_Budget_Orders` shows whether many orders are affected.
- `Over_Budget_Rate` shows whether over-budget records are common for that customer.
- A customer with one very large over-budget order may need a different response than a customer with many smaller over-budget orders.

---

# Part IV: Applied pandas and Reference

This part returns to pandas for applied workflows, advanced operations, performance tips, reporting patterns, troubleshooting, and quick reference material.

---

# 31. Practical Orders and Inventory Example

This example uses generic order and inventory data. It is not real customer data.

## 31.1 Create sample order and inventory data

```python
orders = pd.DataFrame({
    "Reference": ["R001", "R002", "R003", "R004", "R005"],
    "Customer": ["North Co", "North Co", "West Shop", "West Shop", "Online"],
    "Reviewer": ["Ana", "Luis", "Ana", "Maria", "Luis"],
    "Product_Line": ["Office", "Office", "Hardware", "Hardware", "Software"],
    "Budgeted": [500.00, 750.00, 300.00, 1000.00, 250.00],
    "Actual": [400.00, 750.00, 200.00, 1200.00, 0.00],
    "Units_Ordered": [2, 3, 1, 4, 1],
    "Units_Received": [1, 3, 1, 4, 0],
    "Log_Message": ["Delivered complete", "Delivered complete", "Partial shipment", "Rush fee applied", "Backordered"]
})
```

## 31.2 Calculate variance

```python
orders["Variance"] = orders["Budgeted"] - orders["Actual"]
```

Interpretation:

- Positive variance: budgeted is higher than actual; possible savings opportunity.
- Zero variance: actual matches budgeted.
- Negative variance: actual is higher than budgeted; possible over-budget item or calculation difference.

## 31.3 Categorize budget status

```python
conditions = [
    orders["Variance"] > 0,
    orders["Variance"] < 0,
    orders["Variance"] == 0
]

choices = ["Under Budget", "Over Budget", "On Budget"]

orders["Budget_Status"] = np.select(conditions, choices, default="Review")
```

## 31.4 Detect possible quantity issue

```python
orders["Possible_Quantity_Issue"] = orders["Units_Received"] < orders["Units_Ordered"]
```

## 31.5 Create a final tag

```python
orders["Tag"] = "Review"

orders.loc[orders["Possible_Quantity_Issue"], "Tag"] = "Quantity Issue"
orders.loc[orders["Budget_Status"] == "On Budget", "Tag"] = "No Issue"
orders.loc[orders["Budget_Status"] == "Over Budget", "Tag"] = "Over Budget"
```

## 31.6 Summary by customer

```python
customer_summary = orders.groupby("Customer").agg(
    Order_Count=("Reference", "nunique"),
    Total_Budgeted=("Budgeted", "sum"),
    Total_Actual=("Actual", "sum"),
    Total_Variance=("Variance", "sum"),
    Average_Variance=("Variance", "mean"),
    Median_Variance=("Variance", "median")
).reset_index()
```

## 31.7 Summary by reviewer

```python
reviewer_summary = orders.groupby("Reviewer").agg(
    Orders=("Reference", "nunique"),
    Savings_Orders=("Budget_Status", lambda s: (s == "Under Budget").sum()),
    Total_Variance=("Variance", "sum")
).reset_index()
```

## 31.8 Export results

```python
with pd.ExcelWriter("order_analysis.xlsx", engine="openpyxl") as writer:
    orders.to_excel(writer, sheet_name="Orders", index=False)
    customer_summary.to_excel(writer, sheet_name="Customer Summary", index=False)
    reviewer_summary.to_excel(writer, sheet_name="Reviewer Summary", index=False)
```

---

# 32. Method Chaining

Method chaining means applying multiple operations in a readable sequence.

Without chaining:

```python
df = pd.read_excel("orders.xlsx")
df.columns = df.columns.str.strip()
df = df.dropna(how="all")
df["Variance"] = df["Budgeted"] - df["Actual"]
df = df[df["Variance"] > 0]
df = df.sort_values("Variance", ascending=False)
```

With chaining:

```python
def clean_columns(dataframe):
    dataframe = dataframe.copy()
    dataframe.columns = dataframe.columns.str.strip()
    return dataframe

under_budget = (
    pd.read_excel("orders.xlsx")
      .pipe(clean_columns)
      .dropna(how="all")
      .assign(Variance=lambda d: d["Budgeted"] - d["Actual"])
      .query("Variance > 0")
      .sort_values("Variance", ascending=False)
)
```

Benefits:

- Reduces temporary variables.
- Shows the data pipeline clearly.
- Works well for repeatable cleaning steps.

Use chaining when it improves readability. Do not force it when simple steps are clearer.

---

# 33. Performance Tips

## 33.1 Prefer vectorized operations

Fast:

```python
df["Variance"] = df["Budgeted"] - df["Actual"]
```

Slower:

```python
df["Variance"] = df.apply(lambda row: row["Budgeted"] - row["Actual"], axis=1)
```

## 33.2 Avoid building DataFrames row by row

Slower pattern:

```python
df = pd.DataFrame()
for item in items:
    df = pd.concat([df, pd.DataFrame([item])], ignore_index=True)
```

Better pattern:

```python
rows = []
for item in items:
    rows.append(item)

df = pd.DataFrame(rows)
```

## 33.3 Read only needed columns

```python
df = pd.read_excel("large_report.xlsx", usecols=["Order", "Budgeted", "Actual"])
```

## 33.4 Use categories for repeated text

```python
df["Customer"] = df["Customer"].astype("category")
```

This can reduce memory usage.

## 33.5 Check memory usage

```python
df.info(memory_usage="deep")
```

## 33.6 Process large files in chunks

For CSV files:

```python
chunks = pd.read_csv("large_file.csv", chunksize=100_000)

results = []
for chunk in chunks:
    summary = chunk.groupby("Customer")["Actual"].sum()
    results.append(summary)

final = pd.concat(results).groupby(level=0).sum()
```

`read_excel` does not support chunking the same way CSV does, so very large Excel files may need a different strategy.

---


# 34. Additional pandas Operations

This section covers important pandas tools that do not always appear in beginner tutorials but are very useful in real work.

## 34.1 `where` and `mask`

`where` keeps values when a condition is true and replaces values when the condition is false.

```python
df["Positive_Variance"] = df["Variance"].where(df["Variance"] > 0, 0)
```

Interpretation:

- If `Variance` is positive, keep it.
- If `Variance` is zero or negative, replace it with `0`.

`mask` does the opposite: it replaces values when the condition is true.

```python
df["Variance_No_Negatives"] = df["Variance"].mask(df["Variance"] < 0, 0)
```

Use `where` and `mask` when you want conditional replacement without writing a full `np.where`.

## 34.2 `clip`

`clip` limits values to a lower and/or upper boundary.

```python
df["Score_Capped"] = df["Score"].clip(lower=0, upper=100)
```

Interpretation:

- Values below 0 become 0.
- Values above 100 become 100.
- Values between 0 and 100 stay unchanged.

This is useful for percentages, scores, or quality metrics that should not exceed a valid range.

## 34.3 `assign`

`assign` creates columns in a chain-friendly way.

```python
df = (
    df.assign(
        Variance=lambda d: d["Budgeted"] - d["Actual"],
        Budget_Use_Rate=lambda d: d["Actual"] / d["Budgeted"]
    )
)
```

The `lambda d:` receives the DataFrame as it exists at that step.

## 34.4 `pipe`

`pipe` lets you insert custom functions into a pandas chain.

```python
def clean_headers(dataframe):
    dataframe = dataframe.copy()
    dataframe.columns = dataframe.columns.str.strip().str.replace(" ", "_", regex=False)
    return dataframe

cleaned = (
    pd.read_excel("report.xlsx")
      .pipe(clean_headers)
      .dropna(how="all")
)
```

Use `pipe` when you want reusable cleaning steps.

## 34.5 `explode`

`explode` turns list-like values into multiple rows.

```python
df = pd.DataFrame({
    "Order": ["C001", "C002"],
    "SKU_List": [["99213", "93000"], ["80053"]]
})

exploded = df.explode("SKU_List")
```

Output concept:

```text
  Order SKU_List
0  C001    99213
0  C001    93000
1  C002    80053
```

Use this when one row contains multiple values that should be analyzed separately.

## 34.6 `nlargest` and `nsmallest`

```python
top_10 = df.nlargest(10, "Variance")
bottom_10 = df.nsmallest(10, "Variance")
```

This is cleaner and often faster than sorting the entire DataFrame when you only need top or bottom records.

## 34.7 Sampling data

```python
sample = df.sample(n=100, random_state=42)
```

Random percentage sample:

```python
sample = df.sample(frac=0.10, random_state=42)
```

Use sampling when reviewing a large dataset manually.

## 34.8 Random state

`random_state` makes random operations reproducible.

```python
df.sample(n=5, random_state=42)
```

If you run it again, you get the same sample.

## 34.9 `value_counts` for multiple columns

```python
counts = df.value_counts(["Customer", "Status"]).reset_index(name="Count")
```

This counts unique combinations of Customer and Status.

## 34.10 Percent of total

```python
df["Percent_of_Total"] = df["Sales"] / df["Sales"].sum()
```

Formatted as percentage:

```python
df["Percent_Text"] = df["Percent_of_Total"].map(lambda x: f"{x:.2%}")
```

## 34.11 Difference between rows

```python
df = df.sort_values("Date")
df["Change_From_Previous"] = df["Sales"].diff()
```

Interpretation:

- Positive value means increase from previous row.
- Negative value means decrease.
- First row is missing because there is no previous row.

## 34.12 Percentage change

```python
df["Pct_Change"] = df["Sales"].pct_change()
```

Interpretation:

- `0.10` means 10% increase.
- `-0.05` means 5% decrease.

## 34.13 Cumulative sum

```python
df["Running_Total"] = df["Sales"].cumsum()
```

Use this for month-to-date or year-to-date tracking.

## 34.14 Cumulative count

```python
df["Running_Count"] = range(1, len(df) + 1)
```

Or grouped:

```python
df["Reviewer_Running_Count"] = df.groupby("Reviewer").cumcount() + 1
```

## 34.15 Rank within group

```python
df["Customer_Rank"] = df.groupby("Customer")["Variance"].rank(ascending=False)
```

This ranks rows inside each customer.

## 34.16 `idxmax` and `idxmin`

Find the row with maximum value:

```python
max_row = df.loc[df["Variance"].idxmax()]
```

Find the row with minimum value:

```python
min_row = df.loc[df["Variance"].idxmin()]
```

## 34.17 `select_dtypes`

Select numeric columns:

```python
numeric_df = df.select_dtypes(include="number")
```

Select text/object columns:

```python
text_df = df.select_dtypes(include=["object", "string"])
```

This is useful for automated cleaning and summaries.

## 34.18 Memory-friendly categorical columns

```python
for col in ["Customer", "Status", "Method"]:
    df[col] = df[col].astype("category")
```

Use this when a text column repeats the same values many times.

---

# 35. MultiIndex and Hierarchical Data

A MultiIndex is an index with more than one level.

It often appears after grouping by multiple columns.

## 35.1 Create a MultiIndex through groupby

```python
summary = df.groupby(["Customer", "Reviewer"])["Sales"].sum()
```

The result has two index levels:

- Customer
- Reviewer

## 35.2 Convert MultiIndex result back to normal columns

```python
summary = summary.reset_index()
```

This is usually the easiest format for exporting to Excel.

## 35.3 Set a MultiIndex manually

```python
df_indexed = df.set_index(["Customer", "Reviewer"])
```

## 35.4 Select from a MultiIndex

```python
ghs_rows = df_indexed.loc["GHS"]
```

Select a specific customer and reviewer:

```python
ghs_ana = df_indexed.loc[("GHS", "Ana")]
```

## 35.5 Sort a MultiIndex

```python
df_indexed = df_indexed.sort_index()
```

## 35.6 Unstack a MultiIndex

```python
wide = summary.unstack(fill_value=0)
```

This turns one index level into columns.

## 35.7 Stack back to long format

```python
long = wide.stack()
```

## 35.8 When to avoid MultiIndex

MultiIndex is powerful, but it can make code harder to read.

For business reports and Excel outputs, it is often better to use:

```python
summary.reset_index()
```

This keeps everything as normal columns.

---

# 36. Cumulative, Rolling, and Window Calculations

Window calculations are useful for trends and moving averages.

Example:

```python
daily = pd.DataFrame({
    "Date": pd.date_range("2026-01-01", periods=7),
    "Sales": [100, 150, 80, 200, 220, 180, 250]
})
```

## 36.1 Cumulative sum

```python
daily["Running_Total"] = daily["Sales"].cumsum()
```

Interpretation:

Each row shows total sales up to that date.

## 36.2 Cumulative maximum

```python
daily["Best_So_Far"] = daily["Sales"].cummax()
```

Interpretation:

Each row shows the highest sales value seen so far.

## 36.3 Rolling average

```python
daily["Rolling_3_Day_Avg"] = daily["Sales"].rolling(window=3).mean()
```

Interpretation:

- Each row averages the current row and previous two rows.
- The first two rows are missing because there are not enough values yet.

Allow partial windows:

```python
daily["Rolling_3_Day_Avg"] = daily["Sales"].rolling(window=3, min_periods=1).mean()
```

## 36.4 Rolling sum

```python
daily["Rolling_3_Day_Total"] = daily["Sales"].rolling(window=3, min_periods=1).sum()
```

## 36.5 Expanding average

```python
daily["Expanding_Avg"] = daily["Sales"].expanding().mean()
```

Interpretation:

The average grows from the first row through the current row.

## 36.6 Rolling by group

```python
df = df.sort_values(["Reviewer", "Date"])

df["Reviewer_Rolling_Avg"] = (
    df.groupby("Reviewer")["Sales"]
      .transform(lambda s: s.rolling(window=3, min_periods=1).mean())
)
```

This calculates a rolling average separately for each reviewer.

## 36.7 When rolling calculations are useful

Use rolling calculations to smooth noisy data.

Examples:

- Daily productivity trend.
- Moving average of sales amount.
- Rolling error rate.
- Last 7 days of order volume.

---

# 37. Binning, Bucketing, and Segmentation

Binning means grouping numeric values into ranges.

## 37.1 Fixed bins with `cut`

```python
df["Variance_Bucket"] = pd.cut(
    df["Variance"],
    bins=[-float("inf"), 0, 100, 500, float("inf")],
    labels=["No Savings", "Small", "Medium", "Large"]
)
```

Interpretation:

- `<= 0` becomes `No Savings`.
- `0 to 100` becomes `Small`.
- `100 to 500` becomes `Medium`.
- `> 500` becomes `Large`.

## 37.2 Equal-sized groups with `qcut`

```python
df["Variance_Quartile"] = pd.qcut(df["Variance"], q=4, labels=["Q1", "Q2", "Q3", "Q4"])
```

Interpretation:

- `qcut` tries to put the same number of records in each bucket.
- Q1 contains the lowest values.
- Q4 contains the highest values.

## 37.3 Count records by bucket

```python
bucket_counts = df["Variance_Bucket"].value_counts().sort_index()
```

## 37.4 Summarize by bucket

```python
bucket_summary = df.groupby("Variance_Bucket", observed=True).agg(
    Orders=("Reference", "nunique"),
    Total_Variance=("Variance", "sum"),
    Average_Variance=("Variance", "mean")
).reset_index()
```

## 37.5 When buckets are useful

Use buckets when individual values are too detailed.

Examples:

- Variance severity: small, medium, large.
- Age groups.
- Days open buckets.
- Revenue amount tiers.
- Order amount ranges.

---

# 38. Working with Many Files and JSON

pandas is often used to combine many reports before analysis. Keep this workflow separate from database work: file ingestion is usually about finding files, standardizing columns, and keeping an audit trail; SQL work is usually about requesting the right rows from a database before pandas receives them.

## 38.1 Read all CSV files in a folder

```python
from pathlib import Path

folder = Path("reports")
files = folder.glob("*.csv")

frames = []
for file in files:
    temp = pd.read_csv(file)
    temp["Source_File"] = file.name
    frames.append(temp)

combined = pd.concat(frames, ignore_index=True)
```

Adding `Source_File` helps audit where each row came from.

## 38.2 Read all Excel files in a folder

```python
from pathlib import Path

folder = Path("reports")
files = folder.glob("*.xlsx")

frames = []
for file in files:
    temp = pd.read_excel(file)
    temp["Source_File"] = file.name
    frames.append(temp)

combined = pd.concat(frames, ignore_index=True)
```

## 38.3 Skip temporary Excel files

Excel often creates temporary files that start with `~$`.

```python
files = [file for file in folder.glob("*.xlsx") if not file.name.startswith("~$")]
```

## 38.4 Standardize columns while combining files

Reports from different months or teams often use slightly different column names. Standardize them before concatenating.

```python
rename_map = {
    "Order #": "Order_ID",
    "Order Number": "Order_ID",
    "Customer Name": "Customer",
    "Order Amount": "Amount",
}

frames = []
for file in folder.glob("*.csv"):
    temp = pd.read_csv(file)
    temp = temp.rename(columns=rename_map)
    temp.columns = temp.columns.str.strip().str.replace(" ", "_", regex=False)
    temp["Source_File"] = file.name
    frames.append(temp)

combined = pd.concat(frames, ignore_index=True)
```

## 38.5 Validate required columns after combining files

```python
required = {"Order_ID", "Customer", "Amount", "Source_File"}
missing = required - set(combined.columns)

if missing:
    raise ValueError(f"Missing required columns: {sorted(missing)}")
```

This catches report layout changes before they silently damage the analysis.

## 38.6 Read JSON

```python
df = pd.read_json("data.json")
```

## 38.7 Normalize nested JSON

```python
data = [
    {
        "order": "C001",
        "customer": {"first": "John", "last": "Smith"},
        "lines": [{"sku": "99213", "actual": 100}, {"sku": "93000", "actual": 50}]
    }
]

flat = pd.json_normalize(data)
```

For nested line items:

```python
lines = pd.json_normalize(
    data,
    record_path="lines",
    meta=["order", ["customer", "first"], ["customer", "last"]]
)
```

## 38.8 Create an error report while processing files

```python
errors = []
frames = []

for file in files:
    try:
        temp = pd.read_excel(file)
        temp["Source_File"] = file.name
        frames.append(temp)
    except Exception as exc:
        errors.append({"File": file.name, "Error": str(exc)})

combined = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
error_report = pd.DataFrame(errors)
```

This is useful in automation because one bad file should not always stop the whole process.

---

# 39. SQL for pandas and Python Data Work

SQL is one of the most important companion skills for pandas. pandas is excellent after the data is in memory, but SQL is often the best way to bring only the right data from a database: the right columns, the right rows, the right date range, and the right joins.

A strong workflow is:

1. Use SQL to reduce and shape the data close to the database.
2. Use pandas to inspect, clean, validate, analyze, visualize, and export the result.
3. Push cleaned or summarized results back to a database only when that is part of the workflow.

## 39.1 When to use SQL before pandas

Use SQL before pandas when:

- The source data is in a database.
- The table is too large to load fully into memory.
- You need only selected columns or recent dates.
- Joins can be performed reliably in the database.
- Aggregating in the database will greatly reduce row count.
- You want database permissions, indexes, and query planning to do their job.

Use pandas after SQL when:

- You need flexible cleaning, business rules, or custom calculations.
- You need Excel, CSV, charts, or review workbooks.
- You need exploratory analysis with quick iterations.
- You need final validation and exception reporting.

## 39.2 Basic connection patterns

For a local SQLite database, Python's standard library is enough.

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect("orders.db")

orders = pd.read_sql_query(
    "SELECT order_id, customer, order_date, amount FROM orders",
    conn
)
```

For many production databases, use SQLAlchemy or a database-specific driver. The exact connection string depends on the database and company environment.

```python
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql+psycopg://user:password@host:5432/database")

orders = pd.read_sql_query(
    "SELECT order_id, customer, order_date, amount FROM orders",
    engine
)
```

In real projects, do not hard-code passwords in notebooks or scripts. Use environment variables, a secrets manager, or your organization's approved credential tool.

## 39.3 Read SQL with selected columns

Avoid `SELECT *` for routine work. Bring columns intentionally.

```python
query = """
SELECT
    order_id,
    customer_id,
    order_date,
    status,
    amount
FROM orders
"""

orders = pd.read_sql_query(query, conn)
```

Benefits:

- Less memory usage in pandas.
- Faster transfer from database to Python.
- Fewer confusing duplicate or unused columns.
- More stable code when the table gains extra columns.

## 39.4 Filter rows in SQL before loading

```python
query = """
SELECT
    order_id,
    customer_id,
    order_date,
    status,
    amount
FROM orders
WHERE order_date >= '2026-01-01'
  AND status IN ('Open', 'Shipped')
"""

orders = pd.read_sql_query(query, conn, parse_dates=["order_date"])
```

Filtering in SQL is usually better than loading millions of rows and filtering in pandas afterward.

## 39.5 Use parameters instead of string formatting

Do not build SQL by directly inserting user input into a string. Use parameters so values are passed safely.

```python
query = """
SELECT
    order_id,
    customer_id,
    order_date,
    amount
FROM orders
WHERE order_date BETWEEN ? AND ?
  AND customer_id = ?
"""

orders = pd.read_sql_query(
    query,
    conn,
    params=["2026-01-01", "2026-03-31", "C001"],
    parse_dates=["order_date"]
)
```

Different database drivers may use different parameter styles, such as `?`, `%s`, or named parameters. Follow the driver documentation for your database.

## 39.6 Join database tables before pandas

If the database already has clean keys and indexes, join there first.

```python
query = """
SELECT
    o.order_id,
    o.order_date,
    c.customer_name,
    c.region,
    o.amount
FROM orders AS o
LEFT JOIN customers AS c
    ON o.customer_id = c.customer_id
WHERE o.order_date >= '2026-01-01'
"""

orders = pd.read_sql_query(query, conn, parse_dates=["order_date"])
```

This is similar to `pd.merge`, but the database may be faster and avoids bringing unnecessary lookup tables into Python.

## 39.7 Aggregate in SQL to reduce data volume

If you need a monthly summary, let the database return the monthly summary instead of every transaction.

```python
query = """
SELECT
    customer_id,
    strftime('%Y-%m', order_date) AS order_month,
    COUNT(*) AS order_count,
    SUM(amount) AS total_amount,
    AVG(amount) AS average_amount
FROM orders
WHERE order_date >= '2026-01-01'
GROUP BY customer_id, strftime('%Y-%m', order_date)
"""

monthly = pd.read_sql_query(query, conn)
```

Date functions differ by database. For example, SQLite uses `strftime`, PostgreSQL uses functions such as `date_trunc`, and SQL Server uses functions such as `DATEFROMPARTS` or `FORMAT` depending on the need.

## 39.8 Preview tables and understand schema

Before writing a large query, inspect the available fields.

```python
# SQLite example: list tables
pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name",
    conn
)

# Preview a table
pd.read_sql_query("SELECT * FROM orders LIMIT 5", conn)
```

For production systems, prefer your database catalog, data dictionary, or approved metadata views.

## 39.9 Read large SQL results in chunks

Use chunks when the result may be too large for memory.

```python
query = """
SELECT order_id, customer_id, order_date, amount
FROM orders
WHERE order_date >= '2026-01-01'
"""

chunks = pd.read_sql_query(query, conn, chunksize=100_000, parse_dates=["order_date"])

summary_parts = []
for chunk in chunks:
    part = chunk.groupby("customer_id", as_index=False)["amount"].sum()
    summary_parts.append(part)

summary = (
    pd.concat(summary_parts, ignore_index=True)
      .groupby("customer_id", as_index=False)["amount"].sum()
)
```

Chunking is especially useful when you can process each chunk independently and combine small summaries at the end.

## 39.10 Control data types after reading SQL

Database types do not always arrive in pandas exactly how you expect. Check and convert after loading.

```python
orders = pd.read_sql_query(query, conn, parse_dates=["order_date"])

orders["customer_id"] = orders["customer_id"].astype("string")
orders["status"] = orders["status"].astype("category")
orders["amount"] = pd.to_numeric(orders["amount"], errors="coerce")
```

Common conversions:

| Database value | pandas action |
|---|---|
| Date or timestamp text | `parse_dates=["date_column"]` or `pd.to_datetime()` |
| Repeated labels | `.astype("category")` |
| Codes with leading zeroes | `.astype("string")` |
| Numeric text | `pd.to_numeric(..., errors="coerce")` |

## 39.11 Write a DataFrame to SQL

```python
clean_orders.to_sql(
    "orders_clean",
    conn,
    if_exists="replace",
    index=False
)
```

Common `if_exists` options:

| Option | Meaning |
|---|---|
| `fail` | Error if table exists |
| `replace` | Drop and recreate table |
| `append` | Add rows to an existing table |

Be careful with `replace` in shared databases because it can drop an existing table. In production, write to a staging table first unless you are certain replacement is safe.

## 39.12 Append results safely

When appending, make sure columns, data types, and grain match the destination table.

```python
required_columns = ["order_id", "customer_id", "order_date", "amount"]
output = clean_orders[required_columns].copy()

output.to_sql(
    "orders_clean",
    conn,
    if_exists="append",
    index=False,
    method="multi",
    chunksize=10_000
)
```

Good append checks:

- Confirm the destination table is the correct table.
- Confirm row count before and after writing.
- Confirm key columns are not missing.
- Confirm date and numeric types are correct.
- Avoid appending the same extract twice.

## 39.13 Use transactions for write workflows

A transaction helps keep database writes all-or-nothing when the connection and database support it.

```python
with conn:
    clean_orders.to_sql("orders_stage", conn, if_exists="replace", index=False)
    conn.execute("DELETE FROM load_log WHERE load_name = ?", ["orders_stage"])
    conn.execute(
        "INSERT INTO load_log (load_name, row_count) VALUES (?, ?)",
        ["orders_stage", len(clean_orders)]
    )
```

If an error occurs inside the `with conn:` block for SQLite, the transaction is rolled back.

## 39.14 SQL query checklist before loading to pandas

Before running a query that brings data into pandas, ask:

- What is one row supposed to represent?
- Which columns do I actually need?
- What date range or business filter should limit the data?
- Are joins one-to-one, many-to-one, or many-to-many?
- Could the query create duplicate business keys?
- Can I aggregate in SQL before loading?
- Do I need parameters for dates, IDs, or user-provided values?
- Will the result fit comfortably in memory?

## 39.15 SQL-to-pandas troubleshooting

| Problem | Likely cause | Fix |
|---|---|---|
| Query is slow | Missing filters, too many columns, expensive join | Add `WHERE`, select fewer columns, ask a database expert about indexes |
| pandas runs out of memory | Result set too large | Aggregate in SQL or use `chunksize` |
| Date column is text | Driver did not convert dates | Use `parse_dates` or `pd.to_datetime` |
| IDs lose leading zeroes | ID was interpreted as numeric | Convert to string and preserve codes as text |
| Row count is larger than expected | Join duplicated rows | Check key uniqueness before and after the join |
| SQL injection risk | Values inserted with f-strings or concatenation | Use query parameters |

---

# 40. Styling Tables and Creating Review Outputs

pandas can style DataFrames for display and Excel output.

## 40.1 Format numbers for display

```python
styled = df.style.format({
    "Budgeted": "${:,.2f}",
    "Actual": "${:,.2f}",
    "Variance": "${:,.2f}",
    "Budget_Use_Rate": "{:.2%}"
})
```

This changes display formatting, not the underlying values.

## 40.2 Highlight maximum values

```python
styled = df.style.highlight_max(subset=["Variance"])
```

## 40.3 Highlight minimum values

```python
styled = df.style.highlight_min(subset=["Variance"])
```

## 40.4 Conditional formatting with a custom function

```python
def highlight_savings(value):
    if value > 0:
        return "background-color: yellow"
    return ""

styled = df.style.applymap(highlight_savings, subset=["Variance"])
```

Note: styling syntax can change across pandas versions. If `applymap` is deprecated in your version, use the current Styler elementwise method recommended by the installed pandas version.

## 40.5 Export styled DataFrame to Excel

```python
styled.to_excel("styled_report.xlsx", engine="openpyxl", index=False)
```

## 40.6 Create a review workbook

```python
with pd.ExcelWriter("review_package.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="All Data", index=False)
    df[df["Variance"] > 0].to_excel(writer, sheet_name="Under Budget", index=False)
    df[df["Variance"] <= 0].to_excel(writer, sheet_name="No Savings", index=False)
```

## 40.7 Add an audit summary sheet

```python
summary = pd.DataFrame({
    "Metric": ["Rows", "Savings Rows", "Missing Budgeted", "Missing Actual"],
    "Value": [
        len(df),
        (df["Variance"] > 0).sum(),
        df["Budgeted"].isna().sum(),
        df["Actual"].isna().sum()
    ]
})

with pd.ExcelWriter("review_package.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="All Data", index=False)
    summary.to_excel(writer, sheet_name="Finance Summary", index=False)
```

---

# 41. Common Errors and How to Fix Them

## 41.1 KeyError: column not found

Error:

```text
KeyError: 'Actual'
```

Cause:

- Column name does not exist exactly.
- Extra spaces.
- Different capitalization.
- Line breaks in header.

Fix:

```python
print(df.columns.tolist())
```

Clean columns:

```python
df.columns = df.columns.str.strip()
```

## 41.2 TypeError when doing math

Example problem:

```python
df["Variance"] = df["Budgeted"] - df["Actual"]
```

If columns are text, this may fail.

Fix:

```python
df["Budgeted"] = pd.to_numeric(df["Budgeted"], errors="coerce")
df["Actual"] = pd.to_numeric(df["Actual"], errors="coerce")
```

## 41.3 SettingWithCopyWarning

Problem pattern:

```python
savings = df[df["Variance"] > 0]
savings["Status"] = "Under Budget"
```

Better:

```python
savings = df[df["Variance"] > 0].copy()
savings["Status"] = "Under Budget"
```

Or update original DataFrame:

```python
df.loc[df["Variance"] > 0, "Status"] = "Under Budget"
```

## 41.4 Dates not working

Fix:

```python
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
```

Then check invalid dates:

```python
bad_dates = df[df["Order_Date"].isna()]
```

## 41.5 Merge creates too many rows

Cause:

- Duplicate keys in one or both tables.

Check duplicates:

```python
right_table[right_table.duplicated(subset=["Key"], keep=False)]
```

Use validation:

```python
merged = left.merge(right, on="Key", how="left", validate="many_to_one")
```

## 41.6 Missing values after merge

Use indicator:

```python
merged = left.merge(right, on="Key", how="left", indicator=True)

unmatched = merged[merged["_merge"] == "left_only"]
```

## 41.7 Wrong totals after filtering

Check whether your filter is correct:

```python
print(df.shape)
print(filtered.shape)
print(filtered["Status"].value_counts(dropna=False))
```

Always verify row counts before and after major transformations.

---

# 42. Mini Cheat Sheet

This quick reference collects the most common pandas patterns from the manual. It is intentionally compact, but it is broad enough to use as a day-to-day checklist when starting an analysis, cleaning a report, building a summary, or exporting review files.

## Imports and setup

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)
```

## Read/write

```python
# CSV
pd.read_csv("file.csv")
pd.read_csv("file.csv", usecols=["Order", "Amount"], parse_dates=["Date"])
pd.read_csv("file.csv", dtype={"Zip": "string"})

# Excel
pd.read_excel("file.xlsx")
pd.read_excel("file.xlsx", sheet_name="Summary")
sheets = pd.read_excel("file.xlsx", sheet_name=None)  # dictionary of DataFrames

# Other common formats
pd.read_json("file.json")
pd.read_parquet("file.parquet")
pd.read_sql("select * from orders", connection)

# Export
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
df.to_json("output.json", orient="records", indent=2)
df.to_parquet("output.parquet", index=False)
```

## Inspect

```python
df.head()
df.tail()
df.sample(5, random_state=1)
df.shape
df.info()
df.describe()
df.describe(include="all")
df.dtypes
df.columns.tolist()
df.index
df.nunique()
df.isna().sum()
df.memory_usage(deep=True)
```

## Select columns and rows

```python
# Columns
df["Column"]
df[["Col1", "Col2"]]
df.filter(like="Amount")
df.filter(regex="Amount|Revenue")

# Label-based selection
df.loc[:, ["Customer", "Amount"]]
df.loc[df["Amount"] > 100, ["Customer", "Amount"]]

# Position-based selection
df.iloc[0]
df.iloc[:10, :3]

# Scalar lookup
df.at[5, "Amount"]
df.iat[0, 2]
```

## Filter rows

```python
df[df["Amount"] > 100]
df[(df["Amount"] > 100) & (df["Status"] == "Open")]
df[(df["Amount"] < 0) | (df["Status"] == "Cancelled")]
df[~df["Status"].eq("Closed")]
df[df["Status"].isin(["Open", "Pending"])]
df[df["Name"].str.contains("abc", case=False, na=False)]
df[df["Date"].between("2026-01-01", "2026-01-31")]
df.query("Amount > 100 and Status == 'Open'")
```

## Sort, rank, and get top/bottom records

```python
df.sort_values("Amount")
df.sort_values(["Customer", "Amount"], ascending=[True, False])
df.nlargest(10, "Amount")
df.nsmallest(10, "Amount")
df["AmountRank"] = df["Amount"].rank(ascending=False, method="dense")
```

## Clean column names and values

```python
df.columns = df.columns.str.strip()
df.columns = df.columns.str.lower().str.replace(" ", "_", regex=False)

df["Name"] = df["Name"].str.strip()
df["Status"] = df["Status"].str.title()
df["Status"] = df["Status"].replace({"In Progress": "Open", "N/A": np.nan})
df = df.rename(columns={"old_name": "new_name"})
df = df.drop(columns=["UnusedColumn"])
```

## Missing data

```python
df.isna().sum()
df[df["Amount"].isna()]
df = df.dropna(how="all")
df = df.dropna(subset=["Customer", "Amount"])
df["Amount"] = df["Amount"].fillna(0)
df["Status"] = df["Status"].fillna("Unknown")
df["Amount"] = df["Amount"].ffill()
```

## Data types and conversions

```python
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["ID"] = df["ID"].astype("string")
df["Category"] = df["Category"].astype("category")
df["IsLate"] = df["IsLate"].astype("boolean")
```

## Dates and times

```python
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["MonthName"] = df["Date"].dt.month_name()
df["Weekday"] = df["Date"].dt.day_name()
df["DaysOpen"] = (pd.Timestamp.today().normalize() - df["Date"]).dt.days

df = df.set_index("Date")
monthly = df.resample("ME")["Amount"].sum()
```

## String/text operations

```python
df["Name"].str.lower()
df["Name"].str.upper()
df["Name"].str.contains("smith", case=False, na=False)
df["Code"].str.startswith("A", na=False)
df["Code"].str.slice(0, 3)
df[["First", "Last"]] = df["FullName"].str.split(" ", n=1, expand=True)
```

## Create and update columns

```python
df["Variance"] = df["Budgeted"] - df["Actual"]
df["VariancePct"] = df["Variance"] / df["Budgeted"]
df["Status"] = np.where(df["Variance"] > 0, "Under Budget", "Other")

df["Risk"] = np.select(
    [df["Amount"] >= 1000, df["Amount"] >= 500],
    ["High", "Medium"],
    default="Low"
)

df = df.assign(Net=lambda x: x["Revenue"] - x["Cost"])
```

## Group and aggregate

```python
df.groupby("Customer")["Amount"].sum()

df.groupby("Customer").agg(
    Total=("Amount", "sum"),
    Average=("Amount", "mean"),
    Count=("Order", "nunique"),
    FirstDate=("Date", "min"),
    LastDate=("Date", "max")
).reset_index()

# Percent of total
summary = df.groupby("Customer", as_index=False)["Amount"].sum()
summary["PctOfTotal"] = summary["Amount"] / summary["Amount"].sum()
```

## Pivot tables and cross tabs

```python
pd.pivot_table(
    df,
    index="Customer",
    columns="Status",
    values="Amount",
    aggfunc="sum",
    fill_value=0,
    margins=True
)

pd.crosstab(df["Region"], df["Status"])
pd.crosstab(df["Region"], df["Status"], normalize="index")
```

## Reshape data

```python
# Wide to long
long = df.melt(
    id_vars=["Customer"],
    value_vars=["Jan", "Feb", "Mar"],
    var_name="Month",
    value_name="Amount"
)

# Long to wide
wide = long.pivot(index="Customer", columns="Month", values="Amount").reset_index()
```

## Merge, join, and concatenate

```python
# Database-style joins
merged = left.merge(right, on="Key", how="left")
merged = left.merge(right, on="Key", how="left", validate="many_to_one", indicator=True)

# Different key names
merged = orders.merge(customers, left_on="CustomerID", right_on="ID", how="left")

# Stack rows or columns
combined_rows = pd.concat([jan, feb, mar], ignore_index=True)
combined_cols = pd.concat([left, right], axis=1)

# Index-based join
joined = left.set_index("Key").join(right.set_index("Key"), how="left")
```

## Duplicates and data quality checks

```python
df.duplicated().sum()
df[df.duplicated(subset=["Order"], keep=False)]
df = df.drop_duplicates(subset=["Order"])

required = ["Customer", "Date", "Amount"]
missing_columns = [col for col in required if col not in df.columns]

bad_amounts = df[df["Amount"] < 0]
missing_customers = df[df["Customer"].isna()]
```

## Statistics

```python
df["Amount"].count()
df["Amount"].sum()
df["Amount"].mean()
df["Amount"].median()
df["Amount"].mode()
df["Amount"].min()
df["Amount"].max()
df["Amount"].std()
df["Amount"].var()
df["Amount"].quantile([0.25, 0.5, 0.75])
df[["A", "B"]].corr()
```

## Cumulative, rolling, and window calculations

```python
df = df.sort_values("Date")
df["RunningTotal"] = df["Amount"].cumsum()
df["RunningCount"] = np.arange(1, len(df) + 1)

df["Rolling7DayAvg"] = df["Amount"].rolling(window=7, min_periods=1).mean()
df["PctChange"] = df["Amount"].pct_change()
df["PreviousAmount"] = df["Amount"].shift(1)
```

## Binning and segmentation

```python
df["AmountBand"] = pd.cut(
    df["Amount"],
    bins=[0, 100, 500, 1000, np.inf],
    labels=["Small", "Medium", "Large", "Very Large"]
)

df["Quartile"] = pd.qcut(df["Amount"], q=4, labels=["Q1", "Q2", "Q3", "Q4"])
```

## Method chaining pattern

```python
summary = (
    df
    .rename(columns=str.strip)
    .assign(Amount=lambda x: pd.to_numeric(x["Amount"], errors="coerce"))
    .dropna(subset=["Customer", "Amount"])
    .query("Amount > 0")
    .groupby("Customer", as_index=False)
    .agg(Total=("Amount", "sum"), Orders=("Order", "nunique"))
    .sort_values("Total", ascending=False)
)
```

## Excel reporting

```python
with pd.ExcelWriter("review_output.xlsx", engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name="All Data", index=False)
    summary.to_excel(writer, sheet_name="Summary", index=False)
    exceptions.to_excel(writer, sheet_name="Exceptions", index=False)
```

## Plot

```python
df.plot(x="Month", y="Amount", kind="line")
df.plot(x="Customer", y="Amount", kind="bar")
df.plot(x="Customer", y="Amount", kind="barh")
df["Amount"].plot(kind="hist", bins=20)
df[["Amount"]].plot(kind="box")
df.plot(x="Orders", y="Sales", kind="scatter")
df.plot(x="Month", y=["Revenue", "Cost"], kind="area", alpha=0.4)
plt.tight_layout()
plt.show()
```

## SQL with pandas

```python
# Read selected rows and columns from SQL
query = """
SELECT order_id, customer_id, order_date, amount
FROM orders
WHERE order_date BETWEEN ? AND ?
"""
orders = pd.read_sql_query(
    query,
    conn,
    params=["2026-01-01", "2026-03-31"],
    parse_dates=["order_date"]
)

# Read large results in chunks
chunks = pd.read_sql_query(query, conn, params=["2026-01-01", "2026-03-31"], chunksize=100_000)

# Write cleaned results to a staging table
clean_orders.to_sql("orders_stage", conn, if_exists="replace", index=False)
```

## Display formatting

```python
pd.options.display.float_format = "{:,.2f}".format
summary["PctOfTotal"] = summary["PctOfTotal"].map("{:.1%}".format)
summary["Total"] = summary["Total"].map("${:,.2f}".format)
```

## Common pandas reminders

```python
# Use parentheses around each condition when filtering with & or |.
df[(df["Amount"] > 100) & (df["Status"] == "Open")]

# Use .copy() when you intentionally create an independent filtered DataFrame.
open_orders = df[df["Status"] == "Open"].copy()

# Prefer vectorized operations over row-by-row loops when possible.
df["Net"] = df["Revenue"] - df["Cost"]

# Use reset_index() after groupby when you want a normal DataFrame.
summary = df.groupby("Customer")["Amount"].sum().reset_index()
```

---

# 43. References

Official references:

- pandas User Guide: https://pandas.pydata.org/docs/user_guide/index.html
- pandas 10 minutes to pandas: https://pandas.pydata.org/docs/user_guide/10min.html
- pandas Intro to data structures: https://pandas.pydata.org/docs/user_guide/dsintro.html
- pandas Indexing and selecting data: https://pandas.pydata.org/docs/user_guide/indexing.html
- pandas Reshaping and pivot tables: https://pandas.pydata.org/docs/user_guide/reshaping.html
- pandas Chart visualization: https://pandas.pydata.org/docs/user_guide/visualization.html
- pandas DataFrame API reference: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
- pandas DataFrame.describe API reference: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
- pandas GroupBy API reference: https://pandas.pydata.org/docs/reference/groupby.html
- pandas SQL IO reference: https://pandas.pydata.org/docs/reference/io.html#sql
- Python sqlite3 documentation: https://docs.python.org/3/library/sqlite3.html
- SQLAlchemy documentation: https://docs.sqlalchemy.org/
- Matplotlib examples: https://matplotlib.org/stable/gallery/index.html
- Matplotlib histogram reference: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
- Matplotlib bar reference: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html
- Matplotlib boxplot reference: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html

---

## Final Notes

pandas is not just a library for reading files. It is a full data analysis workflow tool.

A strong pandas workflow usually follows this structure:

1. Read data.
2. Inspect data.
3. Clean column names and data types.
4. Validate required columns.
5. Handle missing values.
6. Create calculated fields.
7. Filter records.
8. Group and summarize.
9. Calculate statistics.
10. Create charts.
11. Export results.

Once you understand these steps, you can automate many repetitive Excel/reporting tasks with Python.
