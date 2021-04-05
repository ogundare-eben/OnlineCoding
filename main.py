# first_name = input("First Name: ").title()
# last_name = input("Last Name: ")
# print(f"\n\tWelcome to python class, {first_name}")

# def hello():
#     print("welcome world")

# hello()

# myVar = 10

# def myfunc():
#     #myVar = 5
#     global myVar
#     print(myVar)

# myfunc()

# x = range (5)

# for num in x:
#     print(num)

# name = 

# x = 30
# y = 30

# if x > y:
#     print(x,"is greater")
# elif y > x:
#     print(y,"is greater")
# else:
#     print(x, "and", y, "are equal values")



#creating modules in python
#created a .py file

# from hello1 import hello

# hello()

# from dirHello1 import hellow2

# hellow2.hello_2()


# from hello1 import x, y, hello

# print ( f"{x}, Welcome home! \n")
# hello()

# import maths

#print(sum(x,y))


# print("this is a simple program to great you!\n".upper())
# from maths import greet_user

# greet_user(first_name="james", last_name="luke")



size = int(input("What's your shirt size: "))
name = "James"
message = input("Type your customized message here: ")

def custom_msg(size, message):
    """As simple coding exercise to get customer's size, a customized
    messgae, and output message to James...
    """
    print(f"\nHey {name}, the shirt size is {size},\n\t...Please print '{message}' on it")

custom_msg(size,message)

#===========================================

# print("This page is to get your shirt size and report back to James.\n")

# from maths import custom_msg

# print("\nAre you ok with this information?")
# print("\n[Y / N]")

# answer = input("\n>: ").upper()

# if answer == "Y":
#     print("\nThank you!")
        
# elif answer == "N":
#     print("\nHow can we serve you better?")
#     customer_compliant = input(">" )
#     print("\n\t...This has been noted. Thank you!!!")

# else:
#     print ()
    #I used print() to break from the loop. Break was returning some error   
 #===========================================

# # first_name = "James"
# # last_nmae = ""

# def formatted_name (first_name, last_name, middle_name=" "):
#     """passing an empyth argument in functions - in a dictionary output"""
#     dic_name = {'first': firstname, 'second': last}

 #===========================================
#from exercise import print_models, show_completed_models

 #===========================================
# name = [ ]

# count = 3
# while True:
#     name = input ("Names: ")
#     name =+ 1
#     name == count
#     break

# import challenge

# # challenge.build_profile
# challenge.build_profile('James', 'matthew',location='princeton',
#     field='physics')

#===============================================
# x = int(input("Enter any number: "))
# y = int(input("Enter any number: "))

# def notImplemented(x,y):
#     """function is to attempt pass - to avoid python
#     running the block of code under it."""
#     #pass
#     c = x + y
#     return c

# notImplemented(x,y)

# print("END!")

#===============================================
# name = input("What's your dog name?: ")
# species = input("What is the species?: ")
# age = int(input ("How old?: "))

# class Dog():
#     """running a class for Dog.
#     dog feature - and there actions"""
#     #any function under a class is a method
#     def __init__(self, name, species, age):
#         self.name = name
#         self.species = species
#         self.age = age
    
#     def sit(self):
#         print(f"{self.name.title()} of {self.age}likes to bark")

#     def roll_over(self):
#         print(f"All dog below {self.age} like to roll. \n{self.name.title()} is an example.")

# customer_1 = Dog(name, species,age)

# print(f"\t...loading information about {customer_1.name.title()}.\n")
# print(f"{customer_1.name.title()} of age {customer_1.age} likes to bark.\n")
# print(f"Yes, I mean {customer_1.name.upper()}.\n")


# """Next guess for the next customer, named customer_2"""

# print("Next Guess!!!\n")

# name = input("What's your dog name?: ")
# species = input("What is the species?: ")
# age = int(input ("How old?: "))

# customer_2 = Dog(name, species, age)

# print(f"\t...loading information about {customer_2.name.title()}.\n")

# print(f"\nAll dog below {customer_2.age} like to roll also. \nand {customer_2.name.title()} is an example.\n")

# customer_2.roll_over()
# customer_1.sit()
#===============================================

