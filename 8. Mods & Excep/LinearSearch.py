import linearmod as lm
n = int(input('Enter the no. of elements -> '))
a = input('Enter the elements -> ')
l=a.split()
key = input('Enter the element to be searched -> ')
lm.linearsearch(l,n,key)