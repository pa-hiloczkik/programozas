'''
A SZÉLSŐÉRTÉK MEGHATÁROZÁSA esetében azt vizsgáljuk, hogy melyik a legkisebb, 
illetve a legnagyobb érték az adatsorban (itt a listában).
'''
lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

min_10D = lista[0]
max_10D = lista[0]
for szam in lista:
      if szam < min:
            min = szam
      if szam > max:
            max = szam

print('A legkisebb szám a listában: ', min_10D)
print('A legnagyobb szám a listában: ', max_10D)  
