import json
import os

def load_data():
    """Load data from the JSON file."""
    if os.path.exists('emp.json'):
        with open('emp.json', 'r') as file:
            return json.load(file)
    return []

def save_data(data):
    """Save data to the JSON file."""
    with open('emp.json', 'w') as file:
        json.dump(data, file, indent=4)

def add_employees():
    data = load_data()
    name = input("Enter the Name: ")
    age = input("Enter the Age: ")
    salary = input("Enter the Salary: ")
    loc = input("Enter the Location: ")
    data.append({'Name': name, 'Age': age, 'Salary': salary, 'Location': loc})
    save_data(data)

def show_employee():
    data = load_data()
    for emp in data:
        print("Name: ", emp['Name'])
        print("Age: ", emp['Age'])
        print("Salary: ", emp['Salary'])
        print("Location: ", emp['Location'])
        print("------------------")

def search_emp():
    name = input("Employee name for searching: ")
    data = load_data()
    found = False
    for emp in data:
        if emp['Name'] == name:
            print("Name: ", emp['Name'])
            print("Age: ", emp['Age'])
            print("Salary: ", emp['Salary'])
            print("Location: ", emp['Location'])
            print("------------------")
            found = True
            break
    if not found:
        print("Employee not found.")

def delete_emp():
    name = input("Enter the Name to delete: ")
    data = load_data()
    new_data = [emp for emp in data if emp['Name'] != name]
    if len(new_data) < len(data):
        save_data(new_data)
        print("Employee deleted.")
    else:
        print("Employee not found.")

def update_emp():
    name = input("Enter the Name for update: ")
    new_age = input("Enter the new Age: ")
    data = load_data()
    updated = False
    for emp in data:
        if emp['Name'] == name:
            emp['Age'] = new_age
            updated = True
            break
    if updated:
        save_data(data)
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
