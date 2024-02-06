s=input('Enter a string')
l=s.split()
n=int(input('Enter value of n:- '))
b=[]
print(l)
for ch in l:
    if ch.isdigit():
        b.append(str(int(ch)+n))
    else:
        b.append(ch)
print(b)