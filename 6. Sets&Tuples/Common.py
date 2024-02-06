def cmnele(l1,l2,l3):
    com = set(l1)&set(l2)&set(l3)
    print(list(com))
l1=l2=l3=[]
l1=list(input('Enter for l1 -> '))
l2=list(input('Enter for l2 -> '))
l3=list(input('Enter for l3 -> '))
cmnele(l1,l2,l3)