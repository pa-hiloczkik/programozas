elso_szam = int(input("Kérek egy számot 1-100ig:"))
masodik_szam = int(input("Kérek egy másik számot 1-100ig:"))
muvelet = input("Válassz egy műveletet (-/+) :")
if muvelet=="+":
    print(elso_szam+masodik_szam)
elif muvelet=="-":
    print(elso_szam-masodik_szam)
