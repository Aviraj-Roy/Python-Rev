def SOD(n):
    s=0
    while(n!=0):
        s+=n%10
        n//=10
    return s
a=int(input('Enter a no.-> '))
b=a
while(b>=10):
    b=SOD(b)
print('Digital Root-> ',b)