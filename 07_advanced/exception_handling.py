try:
    number = int(input("Enter a number: "))
    result = number ** 2

    print("The square is:", result)

except ValueError:
    print("Please enter a valid number!")
