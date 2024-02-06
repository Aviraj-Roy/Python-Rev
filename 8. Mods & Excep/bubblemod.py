def bubbleSort(a,n):
    for i in range(n):
        for j in range(n-i-1):
            if(a[j]>a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
    print('Sorted Result is -> ')
    for i in range(n):
        print(a[i],' ')