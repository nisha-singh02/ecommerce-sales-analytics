import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

df = pd.read_csv("data/processed/cleaned_superstore.csv")

# Fix column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")

# ✅ FIX DATE FORMAT
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce')

conn = psycopg2.connect(
    host="localhost",
    database="ecommerce",
    user="postgres",
    password="123"
)

cur = conn.cursor()

execute_values(
    cur,
    """
    INSERT INTO sales (
        row_id, order_id, order_date, ship_date, ship_mode,
        customer_id, customer_name, segment, country, city,
        state, postal_code, region, product_id, category,
        sub_category, product_name, sales, quantity, discount, profit
    ) VALUES %s
    """,
    df.values.tolist()
)

conn.commit()
cur.close()
conn.close()

print("✅ Data loaded into PostgreSQL")