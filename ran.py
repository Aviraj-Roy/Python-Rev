import random as r
c=[]

for i in range(0,10):
    c.append(r.randint(1,50))
print('The generated list is:- ',c)

print('The average of the element is:- ',sum(c)/len(c))

print('The largest value is:- ',max(c))
print('The smallest value is:- ',min(c))

d=sorted(c)
c.sort()
print('The sorted list is:- ',c)

print('The second largest is:- ',d[-2])
print('The second smallest is:- ',d[1])
s=0
for i in range(len(c)):
    if(c[i]%2==0):
        print(c[i] ,end=" ")
        s=s+1
print('\nNo. of even elements are:- ',s)