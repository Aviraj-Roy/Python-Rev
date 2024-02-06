L = [(2,3),(7,6),(2,3),(4,2),(7,6)]
T = [tuple(sorted(x)) for x in L]
L1 = list(set(T))
print(L1)