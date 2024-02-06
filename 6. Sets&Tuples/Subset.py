import itertools as it
A = {10,20,30,40}
n = int(input('Enter n-> '))
B = set(it.combinations(A,n))
print(B)