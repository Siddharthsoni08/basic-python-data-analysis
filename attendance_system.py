# Student Attendance System - Stage 1

attendance = {
    "Amit": "Present",
    "Neha": "Absent",
    "Rohit": "Present",
    "Pooja": "Present",
    "Rahul": "Absent"
}

print("\n" + "=" * 40)
print("STUDENT ATTENDANCE REPORT")
print("=" * 40)

print("\nAttendance Status:")
for name, status in attendance.items():
    print(f"{name:10} : {status}")

# Count present and absent students

present_count = 0
absent_count = 0

for status in attendance.values():
    if status == "Present":
        present_count += 1
    else:
        absent_count += 1

total_students = len(attendance)

attendance_percentage = (present_count / total_students) * 100

print("\nSummary:")
print(f"Total Students     : {total_students}")
print(f"Present Students   : {present_count}")
print(f"Absent Students    : {absent_count}")
print(f"Attendance Percent : {attendance_percentage:.2f}%")

# Identify low attendance students

low_attendance_students = []

for name, status in attendance.items():
    if status == "Absent":
        low_attendance_students.append(name)

print("\nLow Attendance Students:")
if low_attendance_students:
    for student in low_attendance_students:
        print("-", student)
else:
    print("None")
