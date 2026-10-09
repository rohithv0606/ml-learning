#***** data types and missing values *****
import pandas as pd
import numpy as np

data = {
    "name":  ["Asha", "Ravi", "Meena", "Karan", "Divya", "Arjun"],
    "age":   [19, 20, np.nan, 21, 20, 22],
    "marks": ["88", "72", "95", "N/A", "81", "45"],
    "city":  ["Chennai", "Madurai", None, "Coimbatore", "chennai ", "Madurai"],
}
df = pd.DataFrame(data)
print(df)
#the problms aree:
# 1. age has a missing value (NaN)
# 2. marks is a string, not a number
# 3. city has inconsistent capitalization and whitespace

#check the data types of each column
print(df.dtypes)
#object usually means text.
#int64 is a whole number, and float64 is a decimal number.
#age shows float64 even though the values look like whole numbers. A column with NaN can't be an int, so Pandas turns it into a float.
#marks is object because of the text values, which means you can't do math on it.

# print(df["marks"].mean())   # this would raise an error.

# convwert the types with astype()
ages = df["age"].fillna(0).astype(int)   # fix the NaN first, then convert
print(ages)

#text to nums using pd.to_numeric(). It can handle errors better than astype().
df["marks"] = pd.to_numeric(df["marks"], errors="coerce")
print(df["marks"])
print(df.dtypes)
#errors="coerce" means "anything that can't be converted becomes NaN instead of crashing."
# now n/a becomes nan

#dates are another common data type. Pandas has a special type for them, called datetime64. You can convert a column to this type with pd.to_datetime().
dates = pd.Series(["2026-01-15", "2026-02-20"])
dates = pd.to_datetime(dates)
print(dates.dt.month)      # 1 and 2
print(dates.dt.day_name()) # weekday names
#Once a column is a real date type, you can pull out the year, month, weekday, and so on with .dt

# findinng missing values
print(df.isna())              # True/False table: is each cell missing?
print(df.isna().sum())        # how many missing in each column
print(df.isna().sum().sum())  # total missing in the whole table
print(df[df["city"].isna()])  # the rows where city is missing
df.info()                     # shows non-null counts per column

#handeling missing values
# drop rows with missing values
print(df.dropna())                       # drops any row with at least one NaN
print(df.dropna(subset=["age"]))         # drops only rows where age is missing
print(df.dropna(axis=1))                 # drops columns that contain any NaN

# filling missing values
df["age"] = df["age"].fillna(df["age"].median())
df["marks"] = df["marks"].fillna(df["marks"].mean())
df["city"] = df["city"].fillna("Unknown")
print(df)

# cleaning text data
print(df["city"].value_counts())    # you'd see chennai and Chennai counted separately
#fixing capitalization and whitespace with .str tools
df["city"] = df["city"].str.strip().str.title()
print(df["city"].value_counts())
#.str.strip() removes spaces at the start and end.
#.str.title() capitalizes each word (.str.lower() and .str.upper() also exist).
#.str.replace("a", "b") replaces text.
#.str.contains("Chen") gives True/False, handy for filtering.
