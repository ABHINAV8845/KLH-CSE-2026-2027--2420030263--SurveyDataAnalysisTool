import pandas as pd

# Simple dataset
df = pd.DataFrame({
    'ID': [1, 2, 2, 4, 5, 5],
    'Name': ['Alice', 'Bob', 'Bob', 'Charlie', 'David', 'David'],
    'Age': [25, 30, 30, 35, 40, 40]
})

print("Original Data:\n", df)

# Remove exact duplicate rows
df_exact = df.drop_duplicates()

print("\nAfter Exact Match Removal:\n", df_exact)