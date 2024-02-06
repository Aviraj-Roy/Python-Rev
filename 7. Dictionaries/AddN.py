mydict = {'items1':(1,'a',2), 'items2':('b',3,'c'), 'items3':(4,'d',5)}
print('Original -> ',mydict)
n = int(input('Enter the no. to be added -> '))
for key,item in mydict.items():
    if isinstance(item,tuple):
        