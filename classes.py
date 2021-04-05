"""script on class in python"""

name = input("What's your dog name?: ")
species = input("What is the species?: ")
age = int(input ("How old?: "))

class Dog():
    """running a class for Dog.
    dog feature - and their actions"""
    #any function under a class is a method
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    
    # def sit(self):
    #     print(f"{self.name.title()} of {self.age}likes to bark")

    # def roll_over(self):
    #     print(f"All dog below {self.age} like to roll. \n{self.name.title()} is an example.")

customer_1 = Dog(name, species,age)

print(f"\t...loading information about {customer_1.name.title()}.\n")
print(f"{customer_1.name.title()} of age {customer_1.age} likes to bark.\n")
print(f"Yes, I mean {customer_1.name.upper()}.\n")


"""Next guess for the next customer, named customer_2"""

print("Next Guess!!!\n")

name = input("What's your dog name?: ")
species = input("What is the species?: ")
age = int(input ("How old?: "))

customer_2 = Dog(name, species, age)

print(f"\t...loading information about {customer_2.name.title()}.\n")

print(f"\nAll dog below {customer_2.age} like to roll also. \nand {customer_2.name.title()} is an example.\n")


# customer_2.roll_over()
# customer_1.sit()