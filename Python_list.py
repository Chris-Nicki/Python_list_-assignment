# Python Lists
# 1. Python List Transformation
"""Problem Statement: You've been given a list of numerical grades
 from a class exam. You need to process and analyze these grades.
"""
# Task 1: Given the list of grades:
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
# Sort the grades in descending order and display the sorted list.
print("Test Grades", grades)
grades.sort(reverse=True)
print("Descending Grades", grades)
# Task 2: Find the average and display
average_grade = sum(grades)//len(grades)
print(f"This was the average grade:", average_grade)

# 2. Advanced List Methods and Identity Operators
"""Problem Statement: You have two lists of student names. One list contains the names
of students who have submitted their assignments,
and the other list contains the names of students who attended the last class.
"""
# Task 1: Given the two lists:
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
print(f"Submitted Papers:",submitted)
print(f"Attended Class:",attended)
# Find out which students both submitted their assignments and attended the class.
submitted_and_attended = [for i in submitted if i in attended]
print(f"Great Job! {submitted_and_attended}, you made it to class and submitted your Python List assignment!")

# 3. Advanced Slicing Techniques
"""Problem Statement: You have a list of daily temperatures for a month, and you'd like to
 extract specific data from it.
"""

# Task 1: Given the list of temperatures:
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93,
                 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print(f"Upcoming Forecast",temperatures)
# Extract the temperatures for the second week (7 days) of the month (index 7 to index 14).
second_week = temperatures[7:14]
print(f"Second Week Temperatures:",second_week)
# Task 2: Extract all the temperatures above 100. **hint** add the temperatures over 100 to a new list.
temperatures_over_100 = temperatures[23:-1]
print(f"Temperatures Over 100 Coming Up!",temperatures_over_100)


