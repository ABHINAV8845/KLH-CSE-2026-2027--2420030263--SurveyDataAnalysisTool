import pandas as pd

df = pd.DataFrame({

    'name': ['abhinav', 'rashul', 'charan', 'nani', 'radha'],

    'ds': [98, 99, 100, 100, 99],

    'cd': [90, 94, 89, 90, 100],

    'toc': [99, 90, 59, 89, 100],

    'alt': [98, 29, 49, 89, 100],

    'kn': [43, 76, 87, 98, 100]

})

print("Pearson Correlation:")
print(df.corr(method='pearson', numeric_only=True))

print("\nSpearman Correlation:")
print(df.corr(method='spearman', numeric_only=True))