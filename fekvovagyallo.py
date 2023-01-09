szelesseg=int(input('Kérem a szélességét:'))
magassag=int(input('Kérem a magasságát:'))
terulet= szelesseg*magassag
if szelesseg > magassag:
    print('Ez egy fekvő téglalap.A területe:',terulet)
elif magassag > szelesseg:
    print('Ez egy álló téglalap.',terulet)
elif magassag == szelesseg:
    print('Ez egy négyzet',terulet)
