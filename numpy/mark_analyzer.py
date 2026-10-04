import numpy as np

# ---------- Data ----------
np.random.seed(7)
marks = np.random.randint(25, 100, size=(40, 5))   # 40 students x 5 subjects
subjects = ["Maths", "Physics", "Chemistry", "English", "CS"]
PASS_MARK = 40

# ---------- Functions ----------

# Average of every mark in the class
def class_average(marks):
    return marks.mean()

# One average per subject (axis=0 collapses the rows, so we get one value per column)
def subject_averages(marks):
    return marks.mean(axis=0)

# Highest mark in each subject
def subject_max(marks):
    return marks.max(axis=0)

# Lowest mark in each subject
def subject_min(marks):
    return marks.min(axis=0)

# Total marks per student (axis=1 collapses the columns, so we get one value per row)
def student_totals(marks):
    return marks.sum(axis=1)

# Average marks per student
def student_averages(marks):
    return marks.mean(axis=1)

# Returns (student number starting from 1, total) of the highest scorer
def find_topper(marks):
    totals = student_totals(marks)
    index = np.argmax(totals)          # position of the biggest total
    return index + 1, totals[index]

# True for students who scored at least PASS_MARK in EVERY subject
def pass_mask(marks):
    return np.all(marks >= PASS_MARK, axis=1)

# Number of students who scored below PASS_MARK in each subject
def failures_per_subject(marks):
    return (marks < PASS_MARK).sum(axis=0)   # True counts as 1

# Grade for each student based on their average
def assign_grades(marks):
    avg = student_averages(marks)
    return np.where(avg >= 80, "A",
           np.where(avg >= 60, "B",
           np.where(avg >= 40, "C", "F")))

# Normalize each subject column to mean 0 and std 1
def normalize(marks):
    return (marks - marks.mean(axis=0)) / marks.std(axis=0)

# Stretch: add 5 bonus marks to each student's lowest subject, capped at 100
def add_bonus(marks):
    bonus = marks.copy()                          # copy so the original stays unchanged
    rows = np.arange(marks.shape[0])              # 0, 1, 2, ... 39
    lowest = np.argmin(marks, axis=1)             # column of each student's lowest mark
    bonus[rows, lowest] += 5
    return np.clip(bonus, 0, 100)

# ---------- Main ----------
if __name__ == "__main__":
    print("=== MARKS REPORT ===\n")

    print("1. Class average:", round(class_average(marks), 2))

    print("\n2. Subject averages:")
    for name, value in zip(subjects, subject_averages(marks)):
        print(f"   {name}: {value:.2f}")

    print("\n3. Highest / lowest per subject:")
    for name, hi, lo in zip(subjects, subject_max(marks), subject_min(marks)):
        print(f"   {name}: highest {hi}, lowest {lo}")

    print("\n4. First 5 students:")
    totals = student_totals(marks)
    averages = student_averages(marks)
    for i in range(5):
        print(f"   Student {i + 1}: total {totals[i]}, average {averages[i]:.2f}")

    student_no, top_total = find_topper(marks)
    print(f"\n5. Topper: Student {student_no} with total {top_total}")

    passed = pass_mask(marks)
    print(f"\n6. Passed: {passed.sum()}, Failed: {(~passed).sum()}")

    fails = failures_per_subject(marks)
    worst = np.argmax(fails)
    print(f"\n7. Most failures: {subjects[worst]} ({fails[worst]} students)")

    grades = assign_grades(marks)
    letters, counts = np.unique(grades, return_counts=True)
    print("\n8. Grade counts:")
    for letter, count in zip(letters, counts):
        print(f"   {letter}: {count}")

    print("\n9. Normalized marks (first 3 rows):")
    print(np.round(normalize(marks)[:3], 2))

    #correlation between subjects
    print("\n--- Correlation between subjects ---")
    corr = np.corrcoef(marks[:, 0], marks[:, 1])[0, 1]
    print(f"Correlation between {subjects[0]} and {subjects[1]}: {corr:.3f}")

    boosted = add_bonus(marks)
    print("Class average after bonus:", round(boosted.mean(), 2))