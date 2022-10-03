# elso feladat 9.DK 
idei_ev = 2022
print(type(idei_ev))
print("az idei_ev változó értéke: ",idei_ev, sep='--->')
felhasznalo_kora = input("Hány éves vagy?: ")
print(type(felhasznalo_kora))
print('Te most', felhasznalo_kora, 'éves vagy.')
felhasznalo_kora = int(felhasznalo_kora)
szuletesi_ev = idei_ev - felhasznalo_kora
print('Ekkor születtél: ', szuletesi_ev, '.', sep='')
