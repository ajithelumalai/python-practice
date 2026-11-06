# Student management system

students = [
    {
        "name" : "Ajith",
        "age" : 20,
        "marks" : [76,78,76]
    },
    {
        "name" : "Raja",
        "age" : 21,
        "marks" : [50,78,64]
    },
    {
        "name" : "Pooja",
        "age" : 22,
        "marks" : [76,89,68]
    }
]

subjects = ["python","sql","react"]

while True:
    print("=======STUDENT MANAGEMENT SYSTEM=======")
    print("1. Display all students")
    print("2. Search Students")
    print("3. Calculate students results")
    print("4. Display students results")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Display all students
    if choice == 1:
        for student in students:
            print(f"Student Name: {student['name']}")
            print(f"Student Age: {student['age']}")
        else:
            print("all students displayed successfully")

    # Search Student
    elif choice == 2:
        search_name = input("Enter student name: ")

        for student in students:
            if student["name"] == search_name:
                print("Student Found!!!")
                print(f"Student Name: {student['name']}")
                print(f"Student Age: {student['age']}")
                break

        else:
            print("student not found")

    # calculate marks
    elif choice == 3:
        for student in students:
            total = sum(student["marks"])
            average = total / len(student["marks"])

            print(f"Student Name: {student["name"]}")
            print("Total Marks: ", total)
            print("Average Marks: ", average)

            if total >= 80:
                print("Grade: A")
            elif total >= 60:
                print("Grade: B")
            else:
                print("Grade: C")

    # display marks
    elif choice == 4:
        for student in students:
            print(f"Student Name: {student['name']}")
            for i in range(len(subjects)):
                print(subjects[i], student["marks"],[i])
    # exit
    elif choice == 5:
        print("Thank  you for using student management system")
        break

    # invalid choice
    else:
        print("Invalid choice")
        continue
