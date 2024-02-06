def ith(sent,c):
    sen=sent.split()
    if c in range(len(sen)):
        x=sen.pop(c-1)
        print(x, ' removal is done')
    else:
        print('Not Found')
sent = input('Enter sentence-> ')
c = int(input('Enter the position-> '))
ith(sent,c)