"""
1. Write a Python program that defines a function called "add_numbers" that takes two arguments 
(i.e., numbers) and returns their sum. Within the function, add the two numbers together and return the 
result using the return statement. Call the function with the values 5 and 6, and print out the returned 
result. This will result in the addition of 5 and 6, with the output of the program being the sum of these 
two numbers
"""

# def add_numbers(a,b):
#     return a+b

# fn=add_numbers(5,6)
# print(fn)



"""2. write a program that determines the nature of a given number (in this case, 87) as being positive, 
negative, or zero? The program should be designed to take the number as input and perform the 
necessary calculations to determine if the number is positive (i.e., greater than zero), negative (i.e., less 
than zero), or zero (i.e., equal to zero). The output of the program should indicate which of these three 
categories the given number falls into."""

# def nature_number(num):
    
#     if num>0:
#         return "Positive"
#     elif num<0:
#         return "Negative"
#     elif num==0:
#         return "Zero"
#     else:
#         return IOError
    
# num=int(input("Enter the number"))

# result=nature_number(num)

# print(result)
    
"""Q3. create a program that determines whether a given number (in this case, 98) is even or odd? The 
program should be designed to take the number as input and perform the necessary calculations to 
determine whether it is divisible by two. If the number is divisible by two without leaving a remainder, 
it is an even number, and if there is a remainder, it is an odd number. The output of the program should 
indicate whether the given number is even or odd.
"""

# def even_odd(num):
#     if num%2==0:
#         return "Even Number"
#     else:
#         return "Odd Number"
    
# num=int(input("Enter the Number"))

# result=even_odd(num)

# print(result)


"""Q4. Write a program for sum of digits.the digits are 76543 and the output should be 25. """

# def sum_of_digit(nums):
#     num_str = str(nums)
#     total_sum = 0
#     for char in num_str:
#         total_sum += int(char)
#     return total_sum

# nums = int(input("Enter a number: "))
# result = sum_of_digit(nums)

# print("The sum of the digits is:", result)

# By Using While loop

# def sum_of_digit(nums):
#     total_sum = 0
#     while nums > 0:
#         total_sum += nums % 10  
#         nums //= 10             
#     return total_sum

# nums = int(input("Enter a number: "))
# result = sum_of_digit(nums)

# print("The sum of the digits is:", result)




"""Q5.Write a program for reversing the given number 5436 and the output should be 6345.
"""
# def reverse_number(nums):
#     num_str = str(nums)
#     reverse_str = num_str[::-1]
#     reverse_num = int(reverse_str)
#     return reverse_num

# nums=int(input("Enter the Numbers"))
# result = reverse_number(nums)
# print("The reversed number is:", result)


        
        
""".Create a list in python using the followings: 2,3,4,5,6,7 with variable ‘a’ Add ‘mango to the above
list Also add banana, grapes & orange in the list insert apple in the 5th position of a variable ‘a’ Remove
last item from the list.
"""

# a=[2,'mango',3,'banana',4,'grapes',5,'orange',6,7]
# print("list with 2,3,4,5,6,7, with some str datatype",a)
# a.insert(5,'apple')
# print("insert apple at index 5",a)
# a.remove(7)
# print("remove last elemrnt",a)


"""Q7. L = [1,2,3,4,5,6,7] Using the above list slice from 1:4"""

# L = [1,2,3,4,5,6,7]
# Sl=L[1:4]
# print(Sl)

"""Q8. Reverse the order of given string L = [4,5,6,8,3] Without using reverse() function"""

# L = [4,5,6,8,3]
# Sl=L[::-1]
# print(Sl)


"""9. Use list comprehension(shortcut method) to square the given list L=[2,4,7,3,6,8]"""

# L=[2,4,7,3,6,8]
# sqrt_lst=[x**2 for x in L]
# print(sqrt_lst)
 
"""Q5. Create a function that takes in a tuple of integers and returns the sum of the integers. Test the
function with a tuple of your choice."""

# def tup_int(tup):
#     sum_tup=0
#     for num in tup:
#         sum_tup+=num
#     return sum_tup

# tup=(1,2,3,4,5)
# result=tup_int(tup)

# print("Sum Of Tuple Interger is=",result)


"""Q6. Create two sets of your favourite fruits, and use the union() method to combine them into a single
set. Print the resulting set to the console."""

# st1={'Mango','pineapple','Guava','Leechi','Apple'}
# st2={'grapes','banana','orange','kevie','black grapes'}

# st3=st1.union(st2)

# print(st3)




""""Q7. Create a set of random words, and use the add() method to add a new word to the set. Print the
resulting set to the console."""

# word_lst={'Mango','pineapple','Guava','Leechi','Apple'}
# word_lst.add("elderberry")
# print(word_lst)

"""Q8. Create a set of your favourite animals, and use the remove() method to remove one animal from
the set. Print the resulting set """

# animal_set={'Lion','Horse','Cheetah','Black Panther','Hyena','Hippopotimus'}
# animal_set.pop()
# print(animal_set)



"""Q9. favorite_books = {"1984", "To Kill a Mockingbird", "Pride and Prejudice"} favorite_movies =
["The Shawshank Redemption", "The Godfather", "The Dark Knight"] Use the zip() function to
combine the book set and movie list into a list of tuples representing book/ movie pairs. Print the
resulting list. """
        
# favorite_books = {"1984", "To Kill a Mockingbird", "Pride and Prejudice"}
# favorite_movies =["The Shawshank Redemption", "The Godfather", "The Dark Knight"]

GREEN = '\033[92m'
PURPLE = '\033[95m'
RESET = '\033[0m'

# for book, movie in zip(favorite_books, favorite_movies):
#     print(f"My favorite Books {GREEN}{book}{RESET} and Movies {PURPLE}{movie}{RESET}")


"""Q10. Write a Python program to find the difference between consecutive numbers in a list. """
# def diff_b_consecutive(nums):
#     diff=[]
#     for i in range(len(nums)-1):
#         diffr=nums[i+1]-nums[i]
#         diff.append(diffr)
#     return diff
# nums = [5, 7, 10, 15, 20]
# result=diff_b_consecutive(nums)
# print("Diffrenece b/w cosective numbers",result)

"""Q11. Create a dictionary called fruits with the following key-value pairs:
"apple": 0.75
"banana": 1.25
"orange": 0.90
Then, print out the price of a banana."""

# dicty={"apple": 0.75,"banana": 1.25,"orange": 0.90}
# price=dicty['banana']

# print("Price of banana is =",price)


"""Q12. Create an empty dictionary called ages. Add the following key-value pairs to the dictionary:
"Alice": 30
"Bob": 25
"Charlie": 35
Then, print out the age of Charlie"""
# ages={}
# data={"Alice": 30,"Bob": 25,"Charlie": 35}
# for k,v in data.items():
#     ages[k]=[v]
# print(ages)
# age=ages['Charlie']
# print("Charlie age is =",age)

"""Q13. Write a function called word_count(text) that takes a string as input and returns a dictionary where
each key is a word in the text and its value is the number of times that word appears in the text. For
example, word_count("hello world hello") should return {"hello": 2, "world": 1}."""
# def words_count(words):
#     words = words.lower()
#     words = words.split()
#     word_counts = {}
#     PURPLE = '\033[95m'
#     RESET = '\033[0m'
#     for word in words:
#         if word in word_counts:
#             word_counts[word] += 1
#         else:
#             word_counts[word] = 1
#     return f"In the words the comes {PURPLE}{word_counts}{RESET} times"
# words=("hello world hello")
# result=words_count(words)
# print(result)       

"""Q14. Create a dictionary called phone_book with the following key-value pairs:
"Alice": "555-1234"
"Bob": "555-5678"
"Charlie": "555-9012
Then, prompt the user to enter a name and print out the corresponding phone number. If the name is
not in the phone book, print out a message saying that the name was not found."""

# phone_book={"Alice": "555-1234","Bob": "555-5678","Charlie": "555-9012"}

# for k,v in phone_book.items():
#     print(f"The key of {GREEN}{k}{RESET}'s values are {PURPLE}{v}{RESET}")
    

# userInput=input("Enter the Name =:")

# if userInput in phone_book:
#     phone_number = phone_book[userInput]
#     print(f"Your Serach User is {GREEN}{userInput}{RESET}'s phone number is {PURPLE}{phone_number}{RESET}")
# else:
#     print(" Enter name was not found")


"""Q15. Write a program that prompts the user to enter a number between 1 and 10. If the number is less
than 5, print out "Too low!", otherwise print out "Too high!"."""

# def userInput(nums):
#     if nums>=5:
#         return "Too High or equivalent"
#     else:
#         return "Too Low"
    
# nums=int(input("Enter the number "))

# result=userInput(nums)

# print(result)

"""Q16. Write a program that prompts the user to enter a password. If the password is "password123",
print out "Access granted", otherwise print out "Access denied" """

# userPassoword="Password123"
# userInputPass=input("Enter the Paasword :")

# if userInputPass==userPassoword:
#     print("Access granted")
# else:
#     print("Access denied")
    
    
"""Q17. Write a program that prompts the user to enter a positive integer. Then, use a loop to print out all
the odd numbers from 1 to that integer"""


# userInput=int(input("Enter the Number :"))

# if userInput<=0:
#     print("Positive number")
# else:
#     for i in range(1, userInput + 1):
#         if i % 2 != 0:
#             print(i)


"""Q18. Write a program that prompts the user to enter their age and then prints out whether they are a 
child (age 0-12), a teenager (age 13-19), an adult (age 20-59), or a senior (age 60+)
"""

# userInput=int(input("Enter the Age :"))

# if userInput<=12:
#     print("They are Child")
# elif userInput<=19:
#     print("They are Teenage")
# elif userInput<=59:
#     print("They are Audlt")
# elif userInput<=60:
#     print("They are Senoir")
# else:
#     print("You Enter wrong Number")



    
"""19. Write a Python class called "Rectangle" with attributes for "width" and "height". Implement 
methods to calculate the area and perimeter of the rectangle. Create an instance of this class and use it 
to print out the rectangle's area and perimeter"""


# class Rectangle:
    
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     def area_of_rectangle(self):
#         # A = L x B
#         self.result=self.width*self.height
#         return self.result
    
# area=Rectangle(12,12)
# result=area.area_of_rectangle()
# print("Area of Rectangle is :",result)

"""Q20. Write a program that prints the first 10 even numbers using a for loop."""

# for i in range(0,10,2):
#     print([i],end=" , ")
    
    
"""Q21. Write a program that takes a list of strings and prints out each string in reverse order using a for 
loop. """

# lst=['Apple','Orange','Grapes','Banana']
# result=[]

# for item in lst:
#     if item:
#         rever=item[::-1]
#         result.append(rever)
# print(result)
    
"""Q23. Write a program that prints the multiplication table of a given number using a for loop."""

# number = int(input("Enter a number for  multiplication table: "))

# for i in range(1, 11):  
#     print(f"{number} x {i} = {number * i}")

"""Q24. Write a program that takes a list of integers as input and returns the sum of all the numbers in the 
list using a for loop. """

# userInput=input("Enter the number :")

# lst=[int(item.strip()) for item in userInput.split()]
# sum=0
# for item in lst:
#     sum+=item
# print(f"Sum of all numbers is = {GREEN}{sum}{RESET}")


"""Q25. Write a program that prompts the user for a positive integer and then prints out all the prime 
numbers up to that number using a for loop."""


# max_number = int(input("Enter a positive integer: "))
# for num in range(2, max_number + 1):
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=' ')
# print()  


"""Q26. Write a program that prompts the user to enter a password until the correct password is entered 
using a while loop. """


# adminPass="abc123"

# while adminPass:
#     userPass=input("Enter the password")
#     if userPass==adminPass:
#         break
#     else:
#         continue
# print(f"Your Access granted as {userPass}")
    
"""Q27. Write a program that takes a list of strings and prints out each string in reverse order using a while 
loop."""

# usr_lst=input("Enter the list string")

# str_lst=[item.strip() for item in usr_lst.split(',')]
# result=[]
# while True:
#     rever=str_lst[::-1]
#     result.append(rever)
#     break

# print(f"Revesed list is {GREEN}{result}{RESET}")
    
    
    
    
"""Q28. Write a program that prompts the user to enter a positive integer and then prints out all the 
Fibonacci numbers up to that number using a while loop."""

# num = int(input("Enter a positive integer: "))

# if num > 0:
#     a, b = 0, 1
#     while a <= num:
#         print(a, end=' ')
#         a, b = b, a + b  
#     print()  
# else:
#     print("Please enter a positive integer.")


"""Q29. Write a program that takes a list of integers as input and returns the product of all the numbers in 
the list using a while loop. """


user_input=input("Enter the number")

usr_num_lst=[int(item.strip()) for item in user_input.split()]

result=0
x=0

while x<len(usr_num_lst):
    result+=usr_num_lst[x]
    x+=1
    
print("The Sum of List number is =",result)






"""Q30. Write a program that prompts the user to enter a positive integer and then prints out the factorial 
of that number using a while loop"""