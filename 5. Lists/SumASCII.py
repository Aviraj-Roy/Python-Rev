s=input('Enter a string-> ')
l=s.split()
p=[]
sum=0
for i in l:
    sum=0
    for j in i:
        sum+=ord(j)
    p.append(sum)
print(p)