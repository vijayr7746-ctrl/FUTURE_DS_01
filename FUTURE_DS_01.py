# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv(r"C:\Users\Vijay\Desktop\presidency\PRO\Superstore1.csv", encoding='latin1')
# Show First 5 Rows
print(df.head())

# Check Missing Values
print(df.isnull().sum())

# Convert Order Date to Date Format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# ==============================
# TOTAL SALES
# ==============================
total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)

# ==============================
# TOP 10 PRODUCTS
# ==============================
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

print(top_products)

# Plot Top Products
top_products.plot(kind='bar', figsize=(10,5))
plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=75)
plt.show()

# ==============================
# SALES BY CATEGORY
# ==============================
category_sales = df.groupby('Category')['Sales'].sum()

print(category_sales)

# Pie Chart
category_sales.plot(kind='pie', autopct='%1.1f%%', figsize=(6,6))
plt.title("Sales by Category")
plt.ylabel("")
plt.show()

# ==============================
# SALES TREND OVER TIME
# ==============================
monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()

monthly_sales.plot(figsize=(12,5))
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# ==============================
# REGION WISE SALES
# ==============================
region_sales = df.groupby('Region')['Sales'].sum()

print(region_sales)

region_sales.plot(kind='bar')
plt.title("Region Wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# ==============================
# PROFIT ANALYSIS
# ==============================
profit = df.groupby('Category')['Profit'].sum()

profit.plot(kind='bar', color='green')
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.show()

# ==============================
# BUSINESS INSIGHTS
# ==============================
print("\nBusiness Insights:")
print("1. Identify high revenue products.")
print("2. Focus on profitable categories.")
print("3. Improve low-performing regions.")
print("4. Track monthly sales growth.")