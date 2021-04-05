size = int(input("What's your shirt size: "))
name = "James"
message = input("Type your customized message here: ")

def custom_msg(size, message):
    """As simple coding exercise to get customer's size, a customized
    messgae, and output message to James...
    """
    print(f"\nHey {name}, the shirt size is {size},\n\t...Please print '{message}' on it")

custom_msg(size,message)