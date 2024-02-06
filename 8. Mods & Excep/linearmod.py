def linearsearch(a,n,key):
    k=0
    for i in range(n):
        if key==a[i]:
            k=1 
            break
    if k==1:
        print(key,' element is at ',i+1)
    else:
        print(key, ' not found')