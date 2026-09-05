#student database(version2): (started) 2 September 2026; (finished) 5 September 2026
import sys,csv
from tabulate import tabulate

core = ("id","name","class","section")  #attributes that must always exist
attributes = []
with open("student_database.csv") as file:
    reader = csv.reader(file)
    reader = list(reader)
    attributes = reader[0] #everything currnetly present in csv...

def main():

    #create CSV file n enter required attributes which is a tuple
    """
    with open("student_database.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=attributes)
        writer.writeheader()
    """
    while True:
        #main menu
        menu = [
                ["STUDENT DATABASE"],
                ["1. Add Student"],
                ["2. Search Student"],
                ["3. Update Student"],
                ["4. Delete Student"],
                ["5. Display All Students"],
                ["6. Sort Students"],
                ["7. Manage Attributes"],
                ["8. Exit"]
                ]
        print(tabulate(menu, headers="firstrow", tablefmt="double_outline", headersglobalalign="center"))

        #choice input as int
        try:
            choice = int(input("\n\n> "))
        except ValueError:
            print("\nInput must be the 'serial no.' of choice interested.\n")
        else:
            match choice:
                case 1:
                    add_student()
                case 2:
                    search_student()
                case 3:
                    update_student()
                case 4:
                    del_student()
                case 5:
                    display_all()
                case 6:
                    sort_student()
                case 7:
                    manage_attr()
                case 8:
                    print("\nExiting...\n\nExited successfully.\n")
                    sys.exit(0)
                case _:
                    print("\nInput must be the 'serial no.' of choice interested.\n")
                    
        print("\nReturning back to main menu...\n\n")


def add_student():
    student = {}
    with open("student_database.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=attributes)
        for key in attributes:
            while True:
                val = input(f"\nEnter {key}:\n> ").strip()
                if key == 'id':
                    with open("student_database.csv") as file :
                        reader = csv.DictReader(file)
                        for row in reader:
                            if val == row[key]:
                                return print(f"{val} already exists\n")
                        if val == "" or not val.isalnum():
                            print(f"{key} must be Numeric or Alphanumeric\n")
                            continue
                elif key == 'name':
                    if val.strip() == '':
                        print("Name cannot be blank.\n")
                        continue
                    else:
                        val = val.title()
                if val != "":
                    break
                else:
                    print(f"{key} cannot be blank; type '-' or 'N/A' if no data to be input\n")
            student[key] = val
        writer.writerow(student)

    print("\nStudent successfully added.\n")


def search_student():
    while True:
        student = []
        #sub menu
        search = [
                ["Search Student"],
                ["1. Search by ID"],
                ["2. Search by name"],
                ["3. Back"]
                ]
        print(tabulate(search, headers="firstrow", tablefmt="pretty", colglobalalign="left", headersglobalalign="center"))

        #choice input as int
        try:
            choice = int(input("\n\n> "))
        except ValueError:
            print("\nInput must be the 'serial no.' of choice interested.\n")
        else:
            flag = False   #flag
            match choice:

                #search by id
                case 1:
                    id = input("\nEnter id:\n> ").strip()
                    with open("student_database.csv",newline="") as file:
                        reader = csv.DictReader(file, fieldnames=attributes)
                        for row in reader:
                            display_row = {}
                            if id == row['id']:
                                flag = True
                                print("Student found.")
                                for key in row:
                                    display_row[key.capitalize()] = row[key]
                                student.append(display_row)                
                    if not flag:
                        print("Student not found.")
                    else:
                        print(tabulate(student, headers="keys",tablefmt="rst", colglobalalign="left", headersglobalalign="center"))

                #search by name       
                case 2:
                    name = input("\nEnter name:\n> ").strip().title()
                    with open("student_database.csv", newline="") as file:
                        reader = csv.DictReader(file, fieldnames=attributes)
                        for row in reader:
                            display_row = {}
                            names = row['name'].split(' ')
                            if name == row['name'] or name in names:
                                flag = True
                                for key in row:
                                    display_row[key.capitalize()] = row[key]
                                student.append(display_row)
                        print(f"\n{len(student)} Student(s) found.\n")
                        if not flag:
                            print("Student not found.")
                        else:
                            student = sorted(student, key=lambda row:row['Name'])
                            print(tabulate(student, headers="keys",tablefmt="rst", colglobalalign="left", headersglobalalign="center"))

                #back
                case 3:
                    return print("\nReturning back to main menu...\n\n")

                #default case
                case _:
                    print("\nInput must be the 'serial no.' of choice interested.")

            print("\nReturning back to sub menu...\n\n")


def update_student():
    #sub-heading
    print(tabulate([["Update Student"]], headers="firstrow", tablefmt="pretty", headersglobalalign="center"))
    id = input("\nEnter id:\n> ")
    flag = False #flag
    #first find the student in read mode
    with open("student_database.csv") as file:
        reader = csv.DictReader(file, fieldnames=attributes)
        rows = list(reader)
        for row in rows:
            if id == row['id']:
                flag = True
                print("\nStudent found.\n")
                attr = ''
                while True:
                    #print the  found student data
                    print(tabulate([row], headers="keys",tablefmt="rst", colglobalalign="left", headersglobalalign="center"))
                    attr = input("\nEnter attribute to update:\n> ").strip().lower()
                    if attr not in row:
                        print("\nAttribute not found.\nEnter correct attribute from the table header.\n\n")
                        continue
                    else:
                        new_value = input("\nNew value:\n> ").strip()
                        if new_value == '' :
                            if attr != 'id' and attr!='name':
                                print(f"\n{attr.capitalize()} cannot be blank; type '-' or 'N/A' if no data to be input\n") 
                                continue
                            else:
                                print(f"\n{attr.capitalize()} must be Alphanumeric.\n")  
                                continue
                        if attr == 'id':
                            if not new_value.isalnum():
                                print(f"\n{attr.capitalize()} must be Alphanumeric.\n")
                                continue

                        if attr == 'name':
                            if new_value == '':
                                print("Name cannot be blank.\n")
                                continue
                            new_value = new_value.title()
                        if attr == 'id':
                            for line in rows:
                                if line['id'] == new_value:
                                    return print(f"\n{attr.capitalize()} already exists.\n")
                        row[attr] = new_value
                        break
                
                #update student in write mode  
                with open("student_database.csv", "w", newline='') as file:   
                    writer = csv.DictWriter(file, fieldnames=attributes)
                    writer.writerows(rows)
        if not flag:
            return print("\nStudent not found.\n")


def del_student():
    #sub-header
    print(tabulate([["Delete Student"]], headers="firstrow", tablefmt="pretty", headersglobalalign="center"))
    #getting id
    while True:
        id = input("\nEnter id:\n> ")
        if id == '':
            print(f"\nId cannot be blank.\n")
            continue
        if not id.isalnum():
            print(f"\nId must be Alphanumeric.\n")
            continue
        break
    flag =False
    confirm = ''
    students = []
    with open("student_database.csv") as file:
        reader = csv.DictReader(file, fieldnames=attributes)
        for row in reader:
            if id == row['id']:
                flag = True
                while True:
                    print(tabulate([row], headers="keys",tablefmt="rst", colglobalalign="left", headersglobalalign="center"))
                    confirm = input(f"\nDelete student {id}? (y/n)\n> ").strip()
                    if confirm in ('y','n','Y','N'):
                        break
                    print("\nConfirm to delete : 'y' for Yes and 'n' for No.\n")
                if confirm in ('y','Y'):
                    continue
            students.append(row)
    
    #update student in write mode  
    with open("student_database.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=attributes)
        writer.writerows(students)

    if not flag:
        print("\nStudent not found.\n")
    
    return print("\nReturning back to main menu...\n\n")


def display_all():
    #sub-header
    print(tabulate([["Display All Students"]], headers="firstrow", tablefmt="pretty", colglobalalign="left", headersglobalalign="center"))
    students = []

    with open("student_database.csv") as file:
        reader = csv.DictReader(file, fieldnames=attributes)
        rows = list(reader)
        for row in rows[1:]:
            display_row ={}
            for key in row:
                display_row[key.capitalize()] = row[key]
            students.append(display_row)
    #students = sorted(students, key=lambda row:int(row['Id'])) no need to display sorted by Id
    print("\n")
    #print table
    print(tabulate(students, headers="keys", tablefmt="fancy_grid", colglobalalign="left", headersglobalalign="center"))


def sort_student():
    while True:
        numeric = []
        non_numeric = []
        final = []
        #sub menu
        count = 0
        sort = [["Sort Students By"]]
        add_sort = [["Sort In Order"],["1. Ascending"],["2. Descending"]]
        for attr in attributes:
            count += 1
            sort.append([f"{count}. {attr.capitalize()}"])
        count += 1
        sort.append([f"{count}. Back"])
        print(tabulate(sort, headers="firstrow", tablefmt="pretty", colglobalalign="left", headersglobalalign="center"))

        #choice input as int
        try:
            choice_int = int(input("\nEnter choice:\n> "))
        except ValueError:
            print("\nInput must be the 'serial no.' of choice interested.\n")
        else:
            #check choice_int
            if choice_int not in range(len(sort)) or choice_int == 0:
                print("\nInput must be the 'serial no.' of choice interested.\n")
                continue
            #if Back is chosen
            if choice_int == count:
                break

            #print additional sort by order
            print(tabulate(add_sort, headers="firstrow", tablefmt="rounded_outline", colglobalalign="left", headersglobalalign="center"))

            try:
                order = int(input("\nEnter sorting order:\n> "))
            except ValueError:
                print("\nInput must be the 'serial no.' of choice interested.\n")
            else:
                #check order
                if order not in range(len(add_sort)) or order == 0:
                    print("\nInput must be the 'serial no.' of choice interested.\n")
                    continue
                #sorting
                attr = sort[1:-1]

                #sorting only when choice is correct
                if (choice_int-1) in range(len(attributes)):
                    #sort in read mode
                    with open("student_database.csv", newline='') as file:
                        reader = csv.DictReader(file, fieldnames=attributes)
                        reader = list(reader)     #list of dictionaries to be sorted
                        key = attributes[choice_int -1]
                        for row in reader[1:]:
                            if row[key].isnumeric():
                                numeric.append(row)
                            else:
                                non_numeric.append(row)

                        #reverse if order is two
                        if order == 2:
                            numeric = sorted(numeric, key= lambda row:int(row[key]), reverse=True)
                            non_numeric = sorted(non_numeric, key= lambda row:row[key], reverse=True)
                        else:
                            numeric = sorted(numeric, key= lambda row:int(row[key]))
                            non_numeric = sorted(non_numeric, key= lambda row:row[key])

                        #final sorted list
                        for row in numeric:
                            final.append(row)
                        for row in non_numeric:
                            final.append(row)
                    # write the sorted csv
                    with open("student_database.csv", 'w', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=attributes)
                        writer.writeheader()
                        writer.writerows(final)
                    print(f"\nStudent sorted by {(str(attr[choice_int-1]).split(' '))[1].rstrip("']")} in {(str(add_sort[order]).split(' '))[1].rstrip("']")} order.")
                    print("\nReturning back to sub-menu...\n\n")

    return print("\nReturning back to main menu...\n\n")


def manage_attr():
    while True:
        new = []
        #sub-menu
        manage = [
                ["Manage Attributes"],
                ["1. View Attributes"],
                ["2. Add Attribute"],
                ["3. Remove Attribute"],
                ["4. Back"]
                ]
        print(tabulate(manage, headers="firstrow", tablefmt="pretty", colglobalalign="left", headersglobalalign="center"))

        #input choice as int
        try:
            choice = int(input("\nEnter choice:\n> "))
        except ValueError:
            print("\nInput must be the 'serial no.' of choice interested.\n")
        else:
            match choice:

                #view attributes
                case 1:
                    count = 0
                    #sub-sub-menu
                    view = [["Current Attributes"]]
                    for attr in attributes:
                        count += 1
                        view.append([f"{count}. {attr.capitalize()}"])
                    #print 
                    print(tabulate(view, headers="firstrow", tablefmt="rounded_outline", colglobalalign="left", headersglobalalign="center"))

                
                # add attribute
                case 2:
                    add = input("\nAttribute name:\n> ").strip().lower()
                    if add in attributes:
                        print("Attribute cannot be added, already exists.\n\nReturning back to sub-menu...\n\n")
                        continue
                    if add == '':
                        print("\nAttribute cannot be empty.\n")
                        continue    
                    attributes.append(add)
                    with open("student_database.csv", newline='') as file:
                        reader = csv.DictReader(file, fieldnames=attributes)
                        reader = list(reader)
                        for row in reader[1:]:
                            new.append(row)
                    with open("student_database.csv",'w', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=attributes)
                        writer.writeheader()
                        writer.writerows(new)

                    print("\nAttribute successfully added.\n")

                    
                # remove attribute
                case 3:
                    remove = input("\nEnter Attribute:\n> ").strip().lower()
                    if remove in core:
                        print("\nCore attribute cannot be removed.\n\nReturning back to sub-menu...\n\n")
                        continue
                    if remove not in attributes:
                        print("\nAttribute does not exist.\n\nReturning back to sub-menu...\n\n")
                        continue
                    #removing
                    with open("student_database.csv", newline='') as file:
                        reader = csv.DictReader(file, fieldnames=attributes)
                        reader =list(reader)
                        attributes.remove(remove)                        
                        for row in reader[1:]:
                            temp = {}
                            for attr in attributes:
                                temp[attr] = row[attr]
                            new.append(temp)
                    #rewriting the new
                    with open("student_database.csv",'w',newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=attributes)
                        writer.writeheader()
                        writer.writerows(new)

                    print("\nAttribute successfully removed.\n")
                                
                
                #back
                case 4:
                    return print("\nReturning back to main menu...\n\n")


                #default case
                case _:
                    print("\nInput must be the 'serial no.' of choice interested.\n")
                    
            print("\nReturning back to sub-menu...\n\n")


if __name__ == "__main__":
    main()