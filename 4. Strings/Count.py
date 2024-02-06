sent=input('Enter a sentence')
v=c=d=0
p="`~!@#$%^&*()_-+=[]{}|\;'/.,:'?><"
vow='aeiou'
dig='0123456789'
for i in sent.lower():
    if i not in p:
        if i in dig:
            d+=1
        elif i in vow:
            v+=1
        else:
            c+=1
print('Vowels= ',v)
print('Digits= ',d)
print('Consonants= ',c)