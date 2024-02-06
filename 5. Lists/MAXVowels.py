s=input('Enter a string -> ').lower()
l=s.split()
s2=0
vow='aeiou'
print(l)
for i in l:
    s=len([j for j in i if j in vow])
    if(s>s2):
        s2=s
        p=i 
print('The String is-> ',p)