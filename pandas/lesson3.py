#**** summary functions in pandas ****
import pandas as pd
import numpy as np

data={"name":  ["Asha", "Ravi", "Meena", "Karan", "Divya", "Arjun", "Priya", "Suresh"],
    "age":   [19, 20, 19, 21, 20, 22, 19, 21],
    "marks": [88, 72, 95, 60, 81, 45, 90, 67],
    "city":  ["Chennai", "Madurai", "Chennai", "Coimbatore",
              "Chennai", "Madurai", "Coimbatore", "Chennai"]
    }
df = pd.DataFrame(data)

print(df["marks"].describe())
# For a number column, describe() gives count, mean, std, min, quartiles (25%, 50%, 75%), and max. For a text column, it behaves differently:
print(df["city"].describe())   # count, unique, top (most common), freq

# statistics on a filtered column
print(df["marks"].mean())      # average
print(df["marks"].median())    # middle value
print(df["marks"].min())
print(df["marks"].max())
print(df["marks"].sum())
print(df["marks"].std())       # spread
print(df["marks"].count())     # number of non-missing values

#These work on a whole DataFrame too, but only with the number columns.
print(df[["age", "marks"]].mean())   # one average per column

#unique values in a column
print(df["city"].unique())       # array of the different cities
print(df["city"].nunique())      # how many different cities: 3
print(df["city"].value_counts()) # how many times each appears

# findinng who has max or min value in a column
best = df["marks"].idxmax()
print(best)                        # 2 (the row label)
print(df.loc[best, "name"])        # Meena
print(df.loc[best])                # her whole row
# idxmax() and idxmin() give the index label of the biggest and smallest value.

#correlation between two columns
print(df["age"].corr(df["marks"]))  # -0.430
#A value near 1 means they rise together
#near -1 means one rises as the other falls
#near 0 means little relationship.

#*** maps (transforming columns) ****

#easy mapping: plain math
#Operations on a whole column apply to every value, with no loop.
print(df["marks"] - df["marks"].mean())     # difference from the class average
print(df["marks"] / 100)                    # marks as a fraction
print(df["name"] + " from " + df["city"])   # join text columns

# normalization: subtract mean, divide by std
df["marks_norm"] = (df["marks"] - df["marks"].mean()) / df["marks"].std()
print(df[["name", "marks", "marks_norm"]])
#note : Pandas .std() divides by n-1, while NumPy's .std() divides by n. The results differ slightly. Neither is wrong.

#map(): apply a rule to each value in a column
# with dictionary: map a city to its state
state = {"Chennai": "TN", "Madurai": "TN", "Coimbatore": "TN"}
df["state"] = df["city"].map(state) #Any value missing from the dictionary becomes NaN (missing)

# with lambda function: map a mark to a mark out of 10
df["marks_out_of_10"] = df["marks"].map(lambda m: m / 10)

#apply() : user defined.( with your own function)
def grade(m):
    if m >= 90:
        return "A"
    elif m >= 75:
        return "B"
    elif m >= 60:
        return "C"
    else:
        return "D"
df["grade"] = df["marks"].apply(grade)
print(df[["name", "marks", "grade"]])
#note:For a single column, map and apply do almost the same thing. Use whichever reads better, and map for dictionaries.

#apply() across rows
def describe_student(row):
    return f"{row['name']} ({row['city']}) scored {row['marks']}"

print(df.apply(describe_student, axis=1))
# note:Sometimes a rule needs several columns of the same row. Use axis=1 so the function receives one whole row at a time.
