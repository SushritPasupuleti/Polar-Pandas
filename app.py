import pandas as pd
from pandasql import sqldf

# load the dataset & set backend to pyarrow
df = pd.read_csv("data/insurance-w-claims.csv").convert_dtypes(dtype_backend="pyarrow")
df["id"] = df.index

print(df.dtypes)

print("Source: \n", df.head())

sql = "SELECT *, rank() OVER (PARTITION BY claim ORDER BY claim DESC, id) AS overall_claim_rank, rank() OVER (PARTITION BY job_title ORDER BY claim DESC, id) AS job_wise_claim_rank  FROM df WHERE age > 50 ORDER BY age ASC"

res = sqldf(sql, locals())

print("SQL Res: \n", res.head())

# res = res.sort_values(by="claim_rank", ascending=True)

sorted = df[df["age"] > 50]
sorted = sorted.sort_values(by="age", ascending=True)

# print("Sorted: \n", sorted.head())
