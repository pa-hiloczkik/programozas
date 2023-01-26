'''
#Eljárás 
def menut_kiir(tipus):

    A menü megjelintése a képernyőt
    if tipus == 2:
        print('1. Új adat bevivetele')
        print('2. Kilépés a programból')
    if tipus == 3:
        print('1. Új adat bevitele')
        print('2. Adatok módosítása / törlése')
        print('3. Kilépés a programból')



#Eljárás hívása
menut_kiir(2)
'''
def koszont():
    print('Üdv a fedélzeten!')
def koszont_nevvel(nev):
    print(f' Szia ' + nev + ', üdv a fedélzeten!')
