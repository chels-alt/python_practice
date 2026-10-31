class A:
    def show(self):
        print("A show")

class B(A):
    def show(self):
        print("B show")
        super().show()

obj = B()
obj.show()                