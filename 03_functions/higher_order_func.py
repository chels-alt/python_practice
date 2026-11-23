def square(num):
    return num * num

def operate(nums, operation):

    for i in nums:
        result = operation(i)
        print(result)

nums = [9, 10, 12]
operate(nums, square)