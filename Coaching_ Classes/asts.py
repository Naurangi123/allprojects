import ast

def add_employees():
    with open('emp.txt','a+') as file:
        name=input("Enter the Name")
        age=input("Enter the Age")
        salary=input("Enter the Saalry")
        loc=input("Enter the Location")
        elist=[name,age,salary,loc]
        file.write(str(elist)+"\n")
        
def show_employee():
    with open('emp.txt','r') as file:
        data=file.readlines()
    for xdata in data:
        elist=ast.literal_eval(xdata)
        print("Name:" ,elist[0])
        print("Age:" ,elist[1])
        print("Salary:" ,elist[2])
        print("Location:" ,elist[3])
        print("------------------")
        
def search_emp():
    with open('emp.txt') as file:
        data=file.readlines()
    name=input("Employee name for searching.")
    for xdata in data:
        elist=ast.literal_eval(xdata)
        if(elist[0]==name):
            print("Name:" ,elist[0])
            print("Age:" ,elist[1])
            print("Salary:" ,elist[2])
            print("Location:" ,elist[3])
            print("------------------")
def delete_emp():
    with open('emp.txt','r') as file:
        data=file.readlines()
    name=input("Enter the Deleting Name")
    for xdata in data:
        index=data.index(xdata)
        elist=ast.literal_eval(xdata)
        if(elist[0]==name):
            del data[index]
    with open('emp.txt','w') as file:
        for xdata in data:
            file.write(xdata)
def update_emp():
    with open('emp.txt','r') as rfile:
        xdata=rfile.readlines()
    name=input("Enter for name Update")
    age=input("Enter for age Update")
    for data in xdata:
        index=xdata.index(data)
        elist=ast.literal_eval(xdata)
        if(elist[0]==name):
            elist[1]+=age
        xdata[index]=str(elist)+'\n'
    with open('emp.txt','w') as file:
        for data in xdata:
            file.write(data)
    
ch=int(input("1.Add\n2.show\n3.search\n4.Delete\n5.Update\n"))
if(ch==1):
    add_employees()
elif(ch==2):
    show_employee()
elif(ch==3):
    search_emp()
elif(ch==4):
    delete_emp()
elif(ch==5):
    update_emp()
else:
    print('Exist')

