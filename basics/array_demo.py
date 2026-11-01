from array import *

length = int(input("Enter length of array: "))

arr = array('i', [])
for i in range(length):
    x = int(input("Enter next value: "))
    arr.append(x)
print(arr)