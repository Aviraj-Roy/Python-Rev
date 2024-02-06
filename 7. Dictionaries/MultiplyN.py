mydict = {"Abhi":20, "Adi":45, "Aka":30}
n=int(input('Enter the value of n -> '))
for i in mydict:
    if(mydict[i]%2==0):
        mydict[i]=mydict[i]*n
print('Modified Dictionary is -> ', mydict)