def Arm(n,ln,s=0):
    if n==0:
        return s
    else:
        s=s+n(n%10)**ln
        return Arm(n//10,ln,s)
num = input('Enter a no.')
l = len(num)
num=int(num)
if Arm(num,l) == num:
    print('Armstrong')
else:
    print('Not Armstrong')