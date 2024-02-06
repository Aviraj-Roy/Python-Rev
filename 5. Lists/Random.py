import random as r
c=[]
for i in range(0,20):
    c.append(r.randint(1,100))
print('The generated list is:- ',c)
#c.remove(c[0])
c.pop()
c.sort()
print('The new list:- ',c)

s=c[1:-1]
print('After removing 1st & last \d',s)
s=c[1:9]+c[10:-1]
print('The 2nd type is ',s)