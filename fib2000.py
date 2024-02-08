   
a=0
b=1 
c=0
s=0
while(c<2000):
    print(c,' ')
    if(c%2==0):
        s=s+c
    a=b 
    b=c 
    c=a+b
    
print('Sum is-> ',s)