
# x = int(input("Type in two numbers: "))
# y = 29

# def sum(x, y):
#     c = x+y
#     return c

# print("Sum is", sum(x,y))

#===================================
# first_name = input("First Name: ")
# last_name = input("Last Name: ")

# def greet_user(first_name, last_name):
#     """ This function is to great the your with thier first name"""
#     print(f"Hello {first_name}, welcome to python class")

# greet_user(first_name.upper(), last_name)

#======================================

size = int(input("What's your shirt size: "))

name = "James"
message = input("Type your customized message here: ")

def custom_msg(size, message):
    """As simple coding exercise to get customer's size, a customized
    messgae, and output message to James...
    """
    print(f"\nHey {name}, the shirt size is {size},\n\t...Please print '{message}' on it")

custom_msg(size,message.upper())