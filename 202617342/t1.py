import pandas as pd



dic = {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }

# df = pd.DataFrame(dic)
# print(df)

# df.to_csv("202617342/t1.csv", index=False)
# print("\n")

# a = pd.read_csv("202617342/t1.csv")
# # print(a)

# my_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
# b = pd.DataFrame(my_list, columns=["A", "B", "C", "D", "E"])
# print(b)

df = pd.DataFrame(dic)
# print(df["Name"])

ages = pd.Series(df["Age"], name="Age")
print(ages)

print("\n")