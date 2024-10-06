"""
Dictionary
1.dict is pair of key and value where kay is unique but value may be duplicate
2.In dictionary data will be store as key:value
3key and value are both hetrogeneous
4.dictionary are create using {} and dict() method
5.dict maybe nested by list or dict()
6.all work in dict like add delete search are done through the key
7. For adding and update in a dict we use same process but if key are not in dictionary then value are update but if key is not dict then paired are add
8.items() items return in the tuple key value form
9. kromkeys() create a new dict by providing set of kays and default
pop() pop remove pair value by providing key after remove it retun value
popitem() pop item remove last pair of value and return in form of tuple 
"""

student={}
n=int(input("Enter the students"))

for i in range(n):
    roll_no=int(input("Enter the number"))
    name=input("Enter the name")
    p=input("Enter the phy")
    c=input("Enter the chem")
    m=input("Enter the math")
    student[roll_no]={'name':name,'Phy':p,'Chem':c,'Math':m}
    
print(student)


# take a list which contain name will be nested list[[5b,hg,ghg,],[tr,iu,y,]]
#take a set which contain roll no