def palin(sen):
    print(sen)
    print(sen[::-1])
    if(sen==sen[::-1]):
        print('Palindrome')
    else:
        print('Not Palindrome')
sent=input('Enter a word-> ')
palin(sent.lower())