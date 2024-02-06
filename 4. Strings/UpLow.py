sent=input('Enter a string-> ')
s=len(sent)
s1=sent[:s//2:1]
s1.upper()
s2=sent[s//2:s:1]
s2.lower()
print(s1+s2)