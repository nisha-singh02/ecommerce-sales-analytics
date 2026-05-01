import pandas as pd

# Load data
df = pd.read_csv("data/raw/SampleSuperstore.csv", encoding='latin1')

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")

# Remove nulls
df.dropna(inplace=True)

# Save cleaned data
df.to_csv("data/processed/cleaned_superstore.csv", index=False)

print("✅ Data cleaned successfully")