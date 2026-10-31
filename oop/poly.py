class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

class Trainer:
    def train(self, animal):
        print("Training started...")
        animal.sound()

d = Dog()
c = Cat()
t = Trainer()
t.train(c)                        