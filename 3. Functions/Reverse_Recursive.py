def rev(r,s=0):
    if r==0:
        return s
    else:
        s=s*10+(r%10)
        return rev(r//10,s)
a=int(input('Enter No.- '))
print('Reverse is = ',rev(a))