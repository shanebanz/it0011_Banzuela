records = []
filename = "Act-4-List-and-Tuple/students.txt"

while True:
    print("\nMenu:")
    print("1. Open File")
    print("2. Save File")
    print("3. Save As File")
    print("4. Show All Students Record")
    print("5. Show Student Record")
    print("6. Add Record")
    print("7. Edit Record")
    print("8. Delete Record")
    print("9. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        try:
            with open(filename, 'r') as file:
                records = [eval(line.strip()) for line in file.readlines()]
            print("File loaded successfully!")
        except FileNotFoundError:
            print("Error loading file.")
    
    elif choice == "2":
        with open(filename, 'w') as file:
            for record in records:
                file.write(str(record) + "\n")
        print("File saved successfully!")
    
    elif choice == "3":
        filename = input("Enter new filename: ")
        with open(filename, 'w') as file:
            for record in records:
                file.write(str(record) + "\n")
        print("File saved successfully!")
    
    elif choice == "4":
        print("1. Order by Last Name")
        print("2. Order by Grade")
        sub_choice = input("Enter choice: ")
        
        if sub_choice == "1":
            records.sort(key=lambda record: record[1][1])
        elif sub_choice == "2":
            records.sort(key=lambda record: (0.6 * record[2]) + (0.4 * record[3]), reverse=True)
        
        for student_id, (first_name, last_name), class_standing, major_exam in records:
            grade = (0.6 * class_standing) + (0.4 * major_exam)
            print("ID: {}, Name: {} {}, Class Standing: {}, Major Exam: {}, Final Grade: {:.2f}".format(
                student_id, first_name, last_name, class_standing, major_exam, grade))
    
    elif choice == "5":
        student_id = input("Enter Student ID to view: ")
        for record in records:
            if record[0] == student_id:
                student_id, (first_name, last_name), class_standing, major_exam = record
                grade = (0.6 * class_standing) + (0.4 * major_exam)
                print("ID: {}, Name: {} {}, Class Standing: {}, Major Exam: {}, Final Grade: {:.2f}".format(
                    student_id, first_name, last_name, class_standing, major_exam, grade))
                break
        else:
            print("Student not found.")
    
    elif choice == "6":
        student_id = input("Enter Student ID (6-digit): ")
        if not student_id.isdigit() or len(student_id) != 6:
            print("Invalid ID. Must be a 6-digit number.")
            continue
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        class_standing = float(input("Enter Class Standing Grade: "))
        major_exam = float(input("Enter Major Exam Grade: "))
        records.append((student_id, (first_name, last_name), class_standing, major_exam))
        print("Record added successfully!")
    
    elif choice == "7":
        student_id = input("Enter Student ID to edit: ")
        for i, record in enumerate(records):
            if record[0] == student_id:
                first_name = input("Enter New First Name: ") or record[1][0]
                last_name = input("Enter New Last Name: ") or record[1][1]
                class_standing = float(input("Enter New Class Standing Grade: ") or record[2])
                major_exam = float(input("Enter New Major Exam Grade: ") or record[3])
                records[i] = (student_id, (first_name, last_name), class_standing, major_exam)
                print("Record updated successfully!")
                break
        else:
            print("Student ID not found.")
    
    elif choice == "8":
        student_id = input("Enter Student ID to delete: ")
        for i, record in enumerate(records):
            if record[0] == student_id:
                del records[i]
                print("Record deleted successfully!")
                break
        else:
            print("Student ID not found.")
    
    elif choice == "9":
        break
    else:
        print("Invalid choice. Try again.")