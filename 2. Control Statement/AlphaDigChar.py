ch=input('Enter any character-> ')
if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    print(ch,' is an alphabet')
elif(ch>='0' and ch<='9'):
    print(ch,' is digit')
else:
    print(ch, 'Special Character')