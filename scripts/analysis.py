import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data/processed/cleaned_superstore.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")

# Convert date column
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# -------------------------------
# KPI METRICS
# -------------------------------
total_sales = df['sales'].sum()
total_profit = df['profit'].sum()
total_orders = df['order_id'].nunique()
aov = total_sales / total_orders

print("\n📊 KEY BUSINESS METRICS")
print(f"Total Sales: {total_sales:.2f}")
print(f"Total Profit: {total_profit:.2f}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value (AOV): {aov:.2f}")

# -------------------------------
# 1. Monthly Revenue Trend
# -------------------------------
monthly_sales = df.groupby(df['order_date'].dt.to_period('M'))['sales'].sum()

plt.figure()
monthly_sales.plot()
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------------
# 2. Region-wise Performance
# -------------------------------
region_data = df.groupby('region').agg({'sales': 'sum', 'profit': 'sum'}).sort_values(by='sales')

plt.figure()
region_data['sales'].plot(kind='bar')
plt.title("Revenue by Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# -------------------------------
# 3. Category Performance
# -------------------------------
category_data = df.groupby('category').agg({'sales': 'sum', 'profit': 'sum'})

plt.figure()
sns.barplot(x=category_data.index, y=category_data['profit'])
plt.title("Profit by Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------------
# 4. Top 10 Customers
# -------------------------------
top_customers = df.groupby('customer_name')['sales'].sum().sort_values(ascending=False).head(10)

plt.figure()
top_customers.plot(kind='bar')
plt.title("Top 10 Customers by Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------------
# 5. Top 5 Loss-Making Products
# -------------------------------
loss_products = df.groupby('product_name')['profit'].sum().sort_values().head(5)

plt.figure()
loss_products.plot(kind='bar')
plt.title("Top 5 Loss-Making Products")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------------
# 6. Discount Impact on Profit
# -------------------------------
plt.figure()
sns.scatterplot(x='discount', y='profit', data=df)
plt.title("Discount vs Profit (Impact Analysis)")
plt.tight_layout()
plt.show()

# -------------------------------
# 7. Sales Contribution by Segment
# -------------------------------
segment_sales = df.groupby('segment')['sales'].sum()

plt.figure()
segment_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales Contribution by Segment")
plt.ylabel("")
plt.tight_layout()
plt.show()

# -------------------------------
# 8. Top 5 Cities by Sales
# -------------------------------
top_cities = df.groupby('city')['sales'].sum().sort_values(ascending=False).head(5)

plt.figure()
top_cities.plot(kind='bar')
plt.title("Top 5 Cities by Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------------
# FINAL INSIGHTS
# -------------------------------
print("\n📈 BUSINESS INSIGHTS:")
print(f"✔ Highest Revenue Region: {region_data['sales'].idxmax()}")
print(f"✔ Most Profitable Category: {category_data['profit'].idxmax()}")
print(f"✔ Top Customer: {top_customers.idxmax()}")
print(f"✔ City Driving Highest Sales: {top_cities.idxmax()}")
print("✔ High discounts negatively impact profit (visible in scatter plot)")
print("✔ Few customers contribute significantly to overall revenue")