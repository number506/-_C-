import pandas as pd

url = "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv"
df = pd.read_csv(url)

print(df)

df.to_csv("t2.csv", index=False)
# titanic = pd.read_csv("202617342/t2.csv")
# print(titanic.head())