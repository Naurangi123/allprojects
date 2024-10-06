import csv
# fields=['Name','Age','Salary']
# rows=[['Naman',23,23040],['Namn',34,22420],['Naan',67,23040]]
# with open('emp.csv','a+') as file:
#     csvwriter=csv.writer(file)
#     csvwriter.writerow(fields)
#     csvwriter.writerows(rows)
# print("File Writing Complete")
    
# with open('emp.csv','r') as rfile:
#     csvfile=csv.reader(rfile)
#     for lines in csvfile:
#         print(lines)
# print("File Writing Complete")



import json
# name=input("enter name")
# age=int(input("ENter age"))
# sal=float(input("Enter salary"))

# di={'Name':name,'Age':age,'Salary':sal}
# jobj=json.dumps(di,indent=4)

# with open('file.json','a+') as jfile:
#     jfile.write(jobj)
    
# print("Json file write completed")



with open('file.json','r') as rfile:
    jfile=json.load(rfile)
    print(jfile)
print("File reading Complete")