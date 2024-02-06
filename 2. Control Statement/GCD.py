x,y=map(int,input('Enter 2 no.s').split(' '))
ans=0
while(x%y!=0):
    ans=x%y
    x=y
    y=ans
print(y)