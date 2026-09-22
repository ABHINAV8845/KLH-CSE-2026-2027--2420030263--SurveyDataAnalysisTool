import pandas as pd
df=pd.read_csv("Iris.csv")
print(df.head())
print(df.head(10))
print()
print(df.tail())
print(df.tail(10))
print(df.info())
print(df.shape())