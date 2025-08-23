# Simple University Grading System

# Taking input from user
name = input("Enter Your Name: ")
reg_no = input("Enter Your Registration Number: ")
marks = int(input("Enter Your Marks (0-100): "))

# Deciding grade
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"


print("\n----- Student Result -----")
print("Name: ", name)
print("Registration Number: ", reg_no)
print("Marks: ", marks)
print("Grade: ", grade)
