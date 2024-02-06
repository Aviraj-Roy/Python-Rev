s=input('Enter a string-> ')
l=s.split()
R=[wd for wd in l if wd.islower() or wd.isupper()]
print(R)