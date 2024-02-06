def SOF(n):
    s=0
    for i in range(1,n-1):
        if(n%i==0):
            s+=i
    return s
a,b = map(int,input('Enter 2 no.s').split(' '))
if(SOF(a)==b and SOF(b)==a):
    print('Amicable')
else:
    print('Not Amicable')