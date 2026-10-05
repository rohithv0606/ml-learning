#**** pandas basics: dataframes and series****
import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)
print(s["b"])   # 20

data = {
    "name":  ["Asha", "Ravi", "Meena", "Karan", "Divya"],
    "age":   [  19  ,  20   ,  19    ,  21    ,  20    ],
    "marks": [88    ,  72   ,  95    ,  60    ,  81    ],
    "city":  ["Chennai", "Madurai", "Chennai", "Coimbatore", "Chennai"]
}
df = pd.DataFrame(data)
print(df)
print(df.head(3))      # first 3 rows
print(df.tail(2))      # last 2 rows
print(df.shape)        # (5, 4) -> 5 rows, 4 columns
print(df.columns)      # column names
print(df.dtypes)       # data type of each column
df.info()              # summary: columns, types, missing values
print(df.describe())   # count, mean, std, min, max for numeric columns

print(df["marks"])             # one column (a Series)
print(df[["name", "marks"]])   # several columns (note the DOUBLE brackets)

#****csv****
df.to_csv("students.csv", index=False)
#index=False stops Pandas from saving the 0, 1, 2... row numbers as an extra column. Run the file, and you'll see students.csv appear in your folder
df2 = pd.read_csv("students.csv")
print(df2)
