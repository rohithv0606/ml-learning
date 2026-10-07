#*** grouping and sorting data in pandas
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

# groupby(): split the data into groups based on a column, then apply a function to each group
print(df.groupby("city")["marks"].mean())
# group the rows by city, then find the average marks in each city
print(df.groupby("city")["marks"].max())     # top mark in each city
print(df.groupby("city")["marks"].count())   # students per city
print(df.groupby("city")["marks"].sum())

# we can do multiple aggregations at once with agg()
print(df.groupby("city")["marks"].agg(["mean", "max", "count", "sum"]))

# ***sorting data in pandas***
print(df.sort_values("marks"))                      # lowest to highest
print(df.sort_values("marks", ascending=False))     # highest to lowest
#by many columns: first by city, then by marks within each city
print(df.sort_values(["city", "marks"], ascending=[True, False]))

print(df.nlargest(3, "marks"))     # top 3 by marks
print(df.nsmallest(2, "marks"))    # bottom 2

# sorting by index (row labels)
print(df.sort_index())  # sort by row labels
#Sorting never changes your original df. It returns a new sorted copy
