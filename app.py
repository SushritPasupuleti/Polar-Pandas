import pandas as pd
from pandasql import sqldf

# load the dataset & set backend to pyarrow
df = pd.read_csv("data/insurance-w-claims.csv").convert_dtypes(dtype_backend="pyarrow")

print(df.dtypes)

print("Source: \n", df.head())

sql = "SELECT * FROM df WHERE age > 50 ORDER BY age ASC"

res = sqldf(sql, locals())

print("SQL Res: \n", res.head())

sorted = df[df["age"] > 50]
sorted = sorted.sort_values(by="age", ascending=True)

print("Sorted: \n", sorted.head())
