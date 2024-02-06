import operator as op
mydict = {"Abhi":20, "Adi":45, "Aka":30}
A = dict(sorted(mydict.items(),key=op.itemgetter(1)))
print(A)
B = dict(sorted(mydict.items(),key=op.itemgetter(1), reverse=True))
print(B)