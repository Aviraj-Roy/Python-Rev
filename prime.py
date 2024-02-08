n=int(input('Enter a no.-> '))
s=0   
for i in range(1,n+1): #starting from 1 and going till n
    if(n%i==0):
        s=s+1
if(s==2):
    print('Prime No.')
else:
    print('Not Prime No.')