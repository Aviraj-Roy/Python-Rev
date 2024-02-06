tup1 = tuple(input('Enter the elements-> '))
x=[]
for ele in tup1:
    x.append([ch for ch in ele if ch.islower()])
print(x)