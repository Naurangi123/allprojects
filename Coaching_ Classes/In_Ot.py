"""
Input Output


if a file have permission
r => (Default mode)
w => (write whenever you can open file in write mode it remove all previous content it means it always overwrite)
a => append the data the end of file.  
these are called file attributes

it have some enhancer mode like
r => read 
w+ => append and create but remove previous data
a+ => append and create both

b => Binary mode

rb+,wb+,ab+


How to open file

open()
open method  return file object

syntax of open() is:

file_object=open('file_name  or string','file_mode or attributes')

e.g

file=open('file.txt,'w')

where file is file_object and 'file.txt' is writing file name and 'w' is file mode that means file write read though.

if a file is open then we need to close that file so we use close() methos for closing the file
syntax for closing the file is:

file_object.close()

file.close()


write()

write is a method fileobject that return no of byte or character written.
write => write the data in string only.

read(no) => print all data or no of character
read()
read(3)
readline() => read one line at a time
readlines() => readline rettun new list and list contain all lines as element

"""
file=open('text.txt','w')

for i in range(3):
    name=input("Enter the name")
    file.write(name+'\n')
file.close()

""" Program 1"""

file1=open('anc.txt','r')

print(file.read(3))
print(file.read(4))
print(file.readline())
print(file.readlines())
file.seek(0)
data=file.readlines()
print(data)

"""Program 2"""

with open('xyz.txt','w') as file:
    file.write("Happy Birthday to Lord Krishna")
    
    
# Program for writing employee data

with open('emp.txt','a+') as emp:
    name=input("Enter name :")
    age=input("Enter age :")
    salary=input("Enter salary :")
    desig=input("Enter disig :")
    loc=input("Enter loc :")
    elist=[name,age,salary,desig,loc]
    emp.write(str(elist)+'\n')
    
    
# Add Data
# Read Data
# Search

#AST#

