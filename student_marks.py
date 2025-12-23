print("\n" + "=" * 40)
print("STUDENT MARKS ANALYSIS REPORT")
print("=" * 40)

#student marks data 
students = {
    "Amit": 78,
    "rohit": 85,
    "Neha": 68,
    "Babita": 34,
    "rahul": 55
}

print("Student Marks:")
for name, marks in students.items():
    print(f"{name:10} : {marks}")


#calculate class avarage

total_marks = 0

for marks in students.values():
    total_marks = total_marks + marks

count = len(students)
average_marks = total_marks/count

print("\nClass Summary:")
print(f"Total Student   : {count}")
print(f"Total Marks     : {total_marks}")
print(f"Class Average   : {average_marks}")

#Find Class Topper

topper_name = ""
topper_marks = -1

for name, marks in students.items():
    if marks > topper_marks:
        topper_marks = marks
        topper_name = name

print("\nTopper:")
print(f"Name  : {topper_name}")
print(f"Marks : {topper_marks}")


#Pass / Fail analysis 

pass_students = []
fail_students = []

for name, marks in students.items():
    if marks >= 50:
        pass_students.append(name)
    else:
        fail_students.append(name)

print("\nPass Students:")
for name in pass_students:
    print(f"- {name}")

print("\nFail Students:")
for name in fail_students:
    print(f"- {name}")