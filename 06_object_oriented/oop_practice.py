class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi! My name is {self.name} and I am {self.age} years old.")


student1 = Student("Chelsiya", 25)
student2 = Student("Moni", 22)
student1.age = 26

student1.introduce()
student2.introduce() 

# Inheritance

class Person:
    def introduce(self):
        print("I am a person.")


class Developer(Person):
    def code(self):
        print("I write Python code.")


developer1 = Developer()

developer1.introduce()
developer1.code()

# Method Overriding

class Animal:
    def sound(self):
        print("Animals make sounds.")


class Dog(Animal):
    def sound(self):
        print("Dog says Woof!")


dog1 = Dog()
dog1.sound()                

# Encapsulation

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Current balance:", self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid deposit amount!")    
    
account1 = BankAccount(5000)
account1.show_balance()
account1.deposit(1000)
account1.show_balance() 
account1.deposit(-500)
account1.show_balance() 

# Polymorphism

class Cat:
    def sound(self):
        print("Cat says Meow!")

class Cow:
    def sound(self):
        print("Cow says Moo!")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound() 