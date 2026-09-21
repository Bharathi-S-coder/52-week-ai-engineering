students = []


def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!")


def view_students():
    print("\n--- Student List ---")

    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print("----------------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])


def search_student():
    print("\n--- Search Student ---")

    search_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == search_id:
            print("Student Found!")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")

    delete_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == delete_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


while True:
    print("\n==============================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()
        
    elif choice == "5":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")