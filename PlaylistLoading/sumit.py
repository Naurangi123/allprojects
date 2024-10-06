# Sumit Exams Study

# a='Sumit kumar'
# print(a[::2])# start:index:step

#given string sumit and output is u ,write code for output
# reverse the given string sumutkumar ,write the code


# l1=[1,2,3,4,5,6,7]

# l2=[2,3,4,5,6,7,8,9]

# l3=l1+l2

# print(l3)

# print(2*(3+5)+6-(4*6)//8)



# loop 1. for loop=> 1.1. nested loop, 2. while loop 

# for loop

#                               ********************************************************
# for i in range(6):
#     for j in range(i):
#         print(end="*")
#     print()
# k=0
# for i in range(6):
#     for j in range(6-i):
#         k+=1
#         print("*",end="")
#     print()
#                          ***********************************************************

#      ***** 
#     ***** 
#    *****
#   *****
#  *****

# for i in range(0,5):
#     for j in range(5-i):
#         print(" ",end="")
#     for k in range(5):
#         print("*",end="")
#     print(" ")
#                              *********************************************************
# * * * * * 
# * * * * 
# * * *
# * *
# *

# for i in range(5):
#     for j in range(5-i):
#         print(" *",end=" ")
#     print("")
 #                              **************************************** 

# for i in range(10):
#     for j in range(i):
#         print(j+1,end=" ")
#     print()


#                            ****************************************************

# for i in range(10):
#     print(' ' * (10 - i) + '*' * (2 * i))

#                             *****************************************************
# for i in range(10):
#     for j in range(10-i):
#         print(" ",end=" ")
#     print(" *" * (2 * i))


#                                ***********************************************************

# k= 1
# for i in range(1,5):
#     for j in range(i):
#         print(k, end=' ')
#         k = k + 1
#     print()


#local variables
# s="python1"
# def fn():
#     a="sumiit"
#     print(a,s)
# print(fn())

# def foo(a=10):
#     a="su"
#     print(s,a)

# print(foo())

#swap tow numbers

# a=int(input("Enter first number :"))
# b=int(input("Enter second number:"))

# print("value before swaping",a,b)

# a,b=b,a

# print("value after swaping",a,b)

# a=10
# b=5
# c=a-b*a
# print(c)

# a=3
# b=5
# c=10

# x=10
# # x=x**4
# # x=x #x=10 => x+= 4=> 10+4 x=14
# x//=4

# print(x)

# a="10"
# b=4.5

# print(type(a),a)
# print(type(b))

# print(a not is b)

# d={1:"sumit","b":"naurangi"}#key:value

# d[2]="python"
# print(d)

# print(d[1])


# a=True

# print(type(a))

# Implicit type conversion

# a=3
# b=4.5
# c=a+b
# print("implicut type conversion",c)

# # Explicit Type conversion

# a=10
# b="20"
# c=a+int(b)
# print("Explicit type conversion",c)

# if else


a=10
b=10
if(a==b):
    if(a>b):
        print("value of a",a)
    else:
        print("value of b",b)
else:
    print("a in not equal to b :",a,b)