import pandas as pd
df=pd.read_csv("Iris.csv")
print(df.corr(method="spearman",numeric_only=float))