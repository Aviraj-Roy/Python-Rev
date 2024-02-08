sent=input('Enter a sentence')
v=c=0
p="`~!@#$%^&*()_-+=[]{}|\;'/.,:'?><"
vow='aeiou'
dig='0123456789'
for i in sent.lower():
    if i not in p:
        if i not in dig:
            if i in vow:
                v+=1
            else:
                c+=1
print('Vowels= ',v)
print('Consonants= ',c)