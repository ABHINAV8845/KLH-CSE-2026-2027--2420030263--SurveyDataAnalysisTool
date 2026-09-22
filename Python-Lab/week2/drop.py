import pandas as pd
import numpy as np
#simmple dataset
df=pd.DataFrame({'Age':[25,30,np.nan,40,35],'Department':['HR','Finance','Finance',np.nan,'IT']})
print("Original Dataset (with missing values)")
print(df)
df_drop_rows=df.dropna()
print("After dropping rows:\n",df_drop_rows)