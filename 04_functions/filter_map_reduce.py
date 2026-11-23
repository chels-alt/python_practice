from functools import reduce

print(reduce(lambda m,n: m+n,list(map(lambda x:x**3,[2,3,4]))))