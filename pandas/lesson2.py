#****selecting rows and filtering data in pandas****
import pandas as pd
import numpy as np

data = {
    "name":  ["Asha", "Ravi", "Meena", "Karan", "Divya", "Arjun", "Priya", "Suresh"],
    "age":   [19, 20, 19, 21, 20, 22, 19, 21],
    "marks": [88, 72, 95, 60, 81, 45, 90, 67],
    "city":  ["Chennai", "Madurai", "Chennai", "Coimbatore",
              "Chennai", "Madurai", "Coimbatore", "Chennai"]
}
df = pd.DataFrame(data)
print(df)

#iloc(integer location) is used to select rows and columns by index position
print(df.iloc[0])          # first row
print(df.iloc[0:3])        # rows 0, 1, 2
print(df.iloc[2, 2])       # row 2, column 2 -> 95
print(df.iloc[:, 0])       # all rows, first column
print(df.iloc[0:3, [0, 2]])  # rows 0-2, columns 0 and 2 (name, marks)

#loc selection by label
print(df.loc[0, "name"])               # Asha
print(df.loc[0:2])                     # rows 0, 1, 2
print(df.loc[:, ["name", "marks"]])    # all rows, two columns
print(df.loc[0:2, "name":"marks"])     # a range of columns by name

# & for and | for or
# Chennai AND marks above 80
print(df[(df["city"] == "Chennai") & (df["marks"] > 80)])

# Madurai OR marks above 90
print(df[(df["city"] == "Madurai") | (df["marks"] > 90)])

#isin is used to filter rows based on a list of values
# city is any of these
print(df[df["city"].isin(["Madurai", "Coimbatore"])])

# ~ flips True/False, so this means "NOT in Chennai"
print(df[~(df["city"] == "Chennai")])
print(df[~df["city"].isin(["Chennai"])])    # same result

# filter rows and pick columns together
print(df.loc[df["marks"] > 80, ["name", "marks"]])

#counting and avg a filtered column
print((df["marks"] >= 60).sum())                        # how many scored 60+
print(df[df["city"] == "Chennai"]["marks"].mean())      # Chennai average
#.sum() on a True/False column counts the Trues

#adding and changing columns
df["bonus"] = df["marks"] + 5                  # new column from math
df["passed"] = df["marks"] >= 50               # True/False column
df["grade"] = np.where(df["marks"] >= 80, "A", "B")   # np.where works here too
print(df)

#Change values in specific rows with loc
df.loc[df["name"] == "Arjun", "marks"] = 50    # set Arjun's marks to 50
