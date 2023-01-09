'''
nev = (input('Kérek egy nevet:'))
eletkor = int(input('Kérek egy életkort:'))
if eletkor < 2:
    print('A kora alapján',nev,'Csecsemő')
elif eletkor < 6:
        print('A kora alapján',nev,'Kisgyerek')
elif eletkor < 12:
        print('A kora alapján',nev,'gyerek')
elif eletkor < 16:
        print('A kora alapján',nev,'Serdülő')
elif eletkor < 25:
        print('A kora alapján',nev,'Ifjú')
elif eletkor < 65:
        print('A kora alapján',nev,'Felnőtt')
elif eletkor > 65:
        print('A kora alapján',nev,'Nyugdíjas')
'''

#------------------------------------------------------------------------------------------------------------


nev = (input('Adja meg a keresztnevét: '))
kor = int(input('Adja meg az életkorát: '))
if kor < 1:
    print('A kora alapján',nev,'csecsemő!')
elif kor < 6:
        print('A kora alapján',nev,'kisgyerek!')
elif kor < 12:
        print('A kora alapján',nev,'gyerek!')
elif kor < 16:
        print('A kora alapján',nev,'serdülő!')
elif kor < 25:
        print('A kora alapján',nev,'ifjú!')
elif kor < 65:
        print('A kora alapján',nev,'felnőtt!')
#else
     #   print('A kora alapján',nev,'nyugdíjas!')
elif kor >= 65:
    print(f"A kora alapján {nev} nyugdíjas!")
