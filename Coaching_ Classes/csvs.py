import csv

def add_employees():
    with open('emp.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        name = input("Enter the Name: ")
        age = input("Enter the Age: ")
        salary = input("Enter the Salary: ")
        loc = input("Enter the Location: ")
        writer.writerow([name, age, salary, loc])

def show_employee():
    with open('emp.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print("Name: ", row[0])
            print("Age: ", row[1])
            print("Salary: ", row[2])
            print("Location: ", row[3])
            print("------------------")

def search_emp():
    name = input("Employee name for searching: ")
    found = False
    with open('emp.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                print("Name: ", row[0])
                print("Age: ", row[1])
                print("Salary: ", row[2])
                print("Location: ", row[3])
                print("------------------")
                found = True
                break
    if not found:
        print("Employee not found.")

def delete_emp():
    name = input("Enter the Name to delete: ")
    rows = []
    found = False
    with open('emp.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                found = True
            else:
                rows.append(row)
    if found:
        with open('emp.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Employee deleted.")
    else:
        print("Employee not found.")

def update_emp():
    name = input("Enter the Name for update: ")
    new_age = input("Enter the new Age: ")
    rows = []
    updated = False
    with open('emp.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                row[1] = new_age
                updated = True
            rows.append(row)
    if updated:
        with open('emp.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Employee updated.")
    else:
        print("Employee not found.")


ch = int(input("1.Add\n2.Show\n3.Search\n4.Delete\n5.Update\n"))
if ch == 1:
    add_employees()
elif ch == 2:
    show_employee()
elif ch == 3:
    search_emp()
elif ch == 4:
    delete_emp()
elif ch == 5:
    update_emp()
else:
    print('Exit')
