students = {}

def add_student(roll, name, grade, attendance):
    students[roll] = {"name": name, "grade": grade, "attendance": attendance}
    print(" student is added:", name)

def update_grade(roll, new_grade):
    if roll in students:
        students[roll]["grade"] = new_grade
        print("Grade updated for roll number:", roll)
    else:
        print("Student is not found")

def update_attendance(roll, new_attendance):
    if roll in students:
        students[roll]["attendance"] = new_attendance
        print("Attendance updated for roll number:", roll)
    else:
        print("Student is not found")

def show_students():
    if not students:
        print("No student records is available")
    else:
        for roll, info in students.items():
            print("Roll:", roll, "Name:", info["name"], "Grade:", info["grade"], "Attendance:", info["attendance"])

add_student(101, "Amit", "A", 90)
add_student(102, "Priya", "B", 85)
show_students()
update_grade(101, "A+")
update_attendance(102, 92)
show_students()
