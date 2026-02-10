
import pandas as pd

# 1. Extract
df = pd.read_csv("raw/raw_data.csv")

# 2. Transform
df = df.drop_duplicates()
df.columns = df.columns.str.lower()
df["margin"] = df["profit"] / df["sales"]

# 3. Load
df.to_csv("output/final_data.csv", index=False)

print("ETL pipeline executed successfully")
