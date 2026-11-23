def logger(func):
    def wrap():
        print("Before execution")
        print(func())
        print("After execution")
    return wrap

@logger
def greet():
    return "Hello, Python!"
greet()

    