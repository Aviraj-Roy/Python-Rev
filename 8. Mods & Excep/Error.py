try:
    a=int(input('Enter a no.'))
    b=int(input('Enter 2nd no.'))
    c=a/b
    print(c)
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print('Should not be zero')