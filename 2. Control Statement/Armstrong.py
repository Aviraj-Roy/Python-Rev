n=int(input('Enter a no.'))
s=0
temp=n
while(temp>0):
    d=temp%10
    s=s+(d*d*d)
    temp=temp/10
if(s==n):
    print('Armstrong')
else:
    print('Not Armstrong')