count = 1

def num():
    global count 
    if count <= 10:
        print(count)
        count += 1
        num()

num()