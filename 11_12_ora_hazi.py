egyikszam=int(input("Kérem az első számot 1-100-ig: "))
masodikszam=int(input("Kérem a második számot 1-100-ig: "))
if egyikszam>masodikszam:
    print("Az első szám nagyobb")
    print("Ennyivel:",egyikszam-masodikszam)
elif egyikszam<masodikszam:
    print("A második szám nagyobb")
    print("Ennyivel:",masodikszam-egyikszam)
else: print("Megegyezik a két szám.")
