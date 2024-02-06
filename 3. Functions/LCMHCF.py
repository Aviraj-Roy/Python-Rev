def lcm(a,b):
    c=max(a,b)
    while True:
        if(c%a==0 and c%b==0):
            return c
        c+=1
def gcd(a,b):
    while(a%b!=0):
        g=a%b
        a=b
        b=g
    return b
a,b = map(int(input('Enter two no.s -> ').split(' ')))
print('LCM of ',a,'and',b,'is',lcm(a,b))
print('GCD of  ',a,'and',b,'is',gcd(a,b))