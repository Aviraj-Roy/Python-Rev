def sum_digits(n):
    s=0
    while(n!=0):
        s=s+n%10
        n=n//10
    return s
a=int(input('Enter a no.-> '))
print('Sum of digits is-> ',sum_digits(a))