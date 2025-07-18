# Control Flow - Making Decisions!
# Python can make decisions based on certain conditions, using if-else statements.
# this is called control flow - it helps us control how our code runs.
# Example
temperature = 30

if temperature > 25:
    print("Today it's a hot day!")
else:
    print("Today it's cold day!")

# You can also add elif for multiple conditions:
# Control flow example for grading student marks
# This will ask the user for input and grade the student's performance

# Prompt the user for student marks
marks = float(input("Enter the student's marks (0-100): "))

# Grading system based on marks
if marks > 70:
    print("Grade: Distinction")
elif marks >= 60:
    print("Grade: Credit")
elif marks >= 50:
    print("Grade: Pass")
else:
    print("Grade: Fail")

