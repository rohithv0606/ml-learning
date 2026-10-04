Project: Student Marks Analyzer

Goal:
Analyze the marks of 40 students across 5 subjects and print a clean report.

data:  #each row = student ; each column = subject. 
np.random.seed(7)
marks = np.random.randint(25, 100, size=(40,5))
subjects = ["Maths", "Physics", "Chemistry", "English", "CS"]

requirments:
1. Overall class average across all marks.
2. Average per subject (one value per subject, printed with its name).
3. Highest and lowest mark in each subject.
4. Each student's total and average (just print the first 5 students).
5. Topper: the student number (starting from 1) with the highest total, and their total.
6. Pass/fail: a student passes only if they score at least 40 in every subject. Print how many passed and how many failed.
7. Subject with the most failures (marks below 40).
8. Grade assignment: create a grades array from each student's average: 80+ is "A", 60 to 79 is "B", 40 to 59 is "C", below 40 is "F". Print how many students got each grade.
9. Normalization: normalize each subject column (subtract the column mean, divide by the column std) and print the first 3 rows of the result.
10. Add bonus marks of 5 to the lowest-scoring subject for every student, capping marks at 100 (look up np.clip).
11. Find the correlation between two subjects with np.corrcoef.