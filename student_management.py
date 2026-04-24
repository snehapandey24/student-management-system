students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter name: ")
        roll = int(input("Enter roll number: "))
        marks = int(input("Enter marks: "))

        student = {
            "name": name,
            "roll": roll,
            "marks": marks
        }

        students.append(student)
        print("Student added successfully!")

    # View Students
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print(student)

    # Search Student
    elif choice == "3":
        roll = int(input("Enter roll number to search: "))
        found = False

        for student in students:
            if student["roll"] == roll:
                print(student)
                found = True
                break

        if not found:
            print("Student not found.")

    # Delete Student
    elif choice == "4":
        roll = int(input("Enter roll number to delete: "))

        for student in students:
            if student["roll"] == roll:
                students.remove(student)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found.")

    # Exit
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
