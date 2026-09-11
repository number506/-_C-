import pandas as pd

url = "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv"
df = pd.read_csv(url)

print(df)

df.to_csv("t2.csv", index=False)
titanic = pd.read_csv("-_C-/t2.csv")
print(titanic.head(8))

titanic.dtypes
titanic.info()

ages = titanic["Age"]

ages.head()

type(titanic["Age"])
pd.Series

titanic["Age"].shape

age_sex = titanic[["Age", "Sex"]]

age_sex.head()

type(titanic[["Age", "Sex"]])
titanic[["Age", "Sex"]].shape

above_35 = titanic[titanic["Age"] > 35]

above_35.head()

titanic["Age"] > 35

above_35.shape

class_23 = titanic[titanic["Pclass"].isin([2, 3])]

class_23.head()

age_no_na = titanic[titanic["Age"].notna()]

age_no_na.head()

age_no_na.shape

adult_names = titanic.loc[titanic["Age"] > 35, "Name"]

adult_names.head()

titanic.iloc[9:25, 2:5]

titanic.iloc[0:3, 3] = "anonymous"

titanic.iloc[:5, 3]
