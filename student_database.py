#student database: (last updated) 14 August 2026
def main():
    students = []
    while True:
        try:
            choice = int(ask("\n\n1. Add\n2. Search\n3. Display\n4. Exit\n\n> "))
        except ValueError:
            print("\nEnter a number.")
            continue
        match choice:
            case 1:
                while True:
                    try:
                        if add_students(students):
                            print("\n\nStudent added.\n\n")
                            if ask("Add another? (y/n): ") == "y":
                                continue
                            else:
                                break 
                        else:
                            continue
                    except EOFError:
                        if ask("Exit Add? (y/n): ") == "y":
                            break
                        else:
                            continue                
            case 2:
                search_students(students)
            case 3:
                display_students(students)
            case 4:
                break

def ask(prompt):
    return input(prompt)

def add_students(students):
    grade_list = ["A1","A2","B1","B2","C1","C2","D","F"]
    name = ask("Enter student name: ").strip().title()
    marks = ask("Enter marks: ").strip()
    grade = ask("Enter grade: ").strip().capitalize()
    if name.isalpha() and marks.isdigit() and grade in grade_list:
        student = {"name":name, 
                "marks":marks, 
                "grade": grade} 
        students.append(student)
        return True
    else:
        print("\nInvalid credentials.\n")
        return False

def search_students(students):
    search = ask("Enter name to search: ").strip().title()
    found = False
    for student in students:
        if search in student["name"]:
            print(f"{student['name']}-{student['marks']}-{student['grade']}")
            found = True
    if not found :
        print("Student not found.")

def display_students(students):
    if students == []:
        print("\nEmpty database.\nReturning to menu.")
    else:
        print("\n\n")
        for student in students :
            print(f"{student['name']}-{student['marks']}-{student['grade']}")

main()