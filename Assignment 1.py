# Assign values to variables
a = float(input("Enter your 1-1 semester percentage: "))
b = float(input("Enter your 1-2 semester percentage: "))
c = float(input("Enter your 2-1 semester percentage: "))
d = float(input("Enter your 2-2 semester percentage: "))
e = float(input("Enter your 3-1 semester percentage: "))
f = float(input("Enter your 3-2 semester percentage: "))
g = float(input("Enter your attendance percentage: "))
h = int(input("Enter your extracurricular activities score: "))
i = int(input("Enter your academic awards and achievements score: "))
j = int(input("Enter your coding skills score: "))

# Create list of semester grades
semester_grades = [a, b, c, d, e, f]

# Calculate dropout
dropout = 1 if min(semester_grades) < 35 and g < 30 else 0

# Calculate good performance
good_performance = 1 if all(grade > 60 for grade in semester_grades) else 0

# Calculate poor performance
poor_performance = 1 if max(semester_grades) < 40 else 0

# Calculate support required
support_required = 1 if any(40 <= grade < 60 for grade in semester_grades) else 0

# Calculate eligibility for placement
eligible_for_placement = 1 if all(grade > 65 for grade in semester_grades) and (j or i or h) else 0

# Print results
print("Dropout: ", dropout)
print("Good Performance: ", good_performance)
print("Poor Performance: ", poor_performance)
print("Support Required: ", support_required)
print("Eligible for Placement: ", eligible_for_placement)
