#student marks data 
students = {
    "Amit": 78,
    "rohit": 85,
    "Neha": 68,
    "Babita": 34,
    "rahul": 55
}

print("Student Marks:")
print(students)

#calculate class avarage

total_marks = 0

for marks in students.values():
    total_marks = total_marks + marks

count = len(students)
average_marks = total_marks/count

print("\nClass Summary:")
print("Total Marks:", total_marks)
print("Number of Students:", count)
print("Class Average:", average_marks)

#Find Class Topper

topper_name = ""
topper_marks = -1

for name, marks in students.items():
    if marks > topper_marks:
        topper_marks = marks
        topper_name = name

print("\nTopper:")
print("Name:", topper_name)
print("Marks:", topper_marks)


#Pass / Fail analysis 

pass_students = []
fail_students = []

for name, marks in students.items():
    if marks >= 50:
        pass_students.append(name)
    else:
        fail_students.append(name)

print("\nPass Students:")
print(pass_students)

print("\nFail Students:")
print(fail_students)
