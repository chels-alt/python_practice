class Laptop():
    def details(self, brand, ram):
        print("Brand: ", brand)
        print("RAM: ", ram)

lap1 = Laptop()
lap2 = Laptop()

lap1.cpu = "i7"
lap2.cpu = "i5"

print("lap1 CPU: ", lap1.cpu)
print("lap2 CPU: ", lap2.cpu)

lap1.details("Dell", "16GB")
lap2.details("HP", "8GB")