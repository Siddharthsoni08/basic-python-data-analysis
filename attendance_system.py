# Student Attendance System - Stage 1

attendance = {
    "Amit": "Present",
    "Neha": "Absent",
    "Rohit": "Present",
    "Pooja": "Present",
    "Rahul": "Absent"
}

print("Student Attendance:")
for name, status in attendance.items():
    print(name, "-", status)



# Count present and absent students

present_count = 0
absent_count = 0

for status in attendance.values():
    if status == "Present":
        present_count += 1
    else:
        absent_count += 1

total_students = len(attendance)

print("\nAttendance Summary:")
print("Total Students:", total_students)
print("Present:", present_count)
print("Absent:", absent_count)


