mydict = {'item1':(1,'a',2), 'item2':('b',3,'c'), 'item3':(4,'d',5)}
print('Original -> ',mydict)
n = int(input('Enter the no. to be added -> '))
for key,item in mydict.items():
    if isinstance(item,tuple):
        mydict[key]=tuple([element+n if isinstance(element,(int,float)) else element for element in item])
print('Updated -> ',mydict)