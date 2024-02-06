A=[(10,-20,30), (11,22,33), (45,-90,78)]
B=tuple(filter(lambda x:all(i>0 for i in x),A))
print(B)