from threading import Thread
from time import sleep

def hello():
    for i in range(5):
        print("Hello ", i + 1)
        sleep(0.3)

def hi():
    for i in range(5):
        print("Hi ", i + 1)
        sleep(0.3)

if __name__ == "__main__":

    t1 = Thread(target=hello)
    sleep(0.2)
    t2 = Thread(target=hi)

    t1.start()
    t2.start()           




num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")



while True:
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: "))
   operation = input("Enter operation (+ or - or * or /): ")

   if operation == "+":
        print(num1 + num2)

   elif operation == "-":
        print(num1 - num2)

   elif operation == "*":
        print(num1 * num2)

   elif operation == "/":
      if num2 == 0:
        print("Cannot divide by zero.")
      else:   
        print(num1 / num2)

   else: 
        print("Invalid operation")

   answer = input("Do you want another calculation? (yes/no): ")

   if answer.lower() == "no":
        print("Thank you for using the calculator.")
        break

import random

secret = random.randint(1, 5)

for i in range(3):

    guess = int(input("Enter the number(1-5): "))

    if guess == secret:
        print("You won!")
        break
    else:
        print("Try again!")