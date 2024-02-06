sent=input('Enter a string-> ')
s=input('Enter the word-> ')
sen=sent.split()
j=0
for i in sen:
    j+=1
    if s==i:
        print('Position is = ',j)
        break