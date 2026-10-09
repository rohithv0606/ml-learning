#*****renaming and combining dataframes*****
import pandas as pd

df = pd.DataFrame({"nm": ["Asha", "Ravi"], "mk": [88, 72]})
df = df.rename(columns={"nm": "name", "mk": "marks"})   # rename some columns
print(df)
df.columns = ["student", "score"]                       # replace ALL names at once
print(df)
df = df.rename(index={0: "first", 1: "second"})         # rename row labels
print(df)

#*****combining by stacking*****
#using concat() to stack dataframes 
a = pd.DataFrame({"name": ["Asha", "Ravi"], "marks": [88, 72]})
b = pd.DataFrame({"name": ["Meena", "Karan"], "marks": [95, 60]})

both = pd.concat([a, b], ignore_index=True)#without index, the row labels will be repeated
print(both)

#combining by merging
students = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "name":       ["Asha", "Ravi", "Meena", "Karan"],
    "dept_id":    [10, 20, 10, 30],
})
depts = pd.DataFrame({
    "dept_id":   [10, 20, 40],
    "dept_name": ["CSE", "ECE", "MECH"],
})

print(pd.merge(students, depts, on="dept_id"))                  # inner (default)
print(pd.merge(students, depts, on="dept_id", how="left"))
print(pd.merge(students, depts, on="dept_id", how="right"))
print(pd.merge(students, depts, on="dept_id", how="outer"))