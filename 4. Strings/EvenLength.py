sent=input("Enter a sentence")
c=sent.split()
print('The even length strings are:- ')
for i in c:
    if(len(i)%2==0):
        print(i,' ')