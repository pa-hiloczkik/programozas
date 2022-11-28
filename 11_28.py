''' 
for szam in range(50,101,3):
    print(szam,end= ' ') 
'''
'''
for szam in range(50,101,3):
    print(szam,end= ' ')
print()

for szam in range(50,101,3):
    if szam % 2 == 0:
        print(szam,end=' ')
print("program vége")

'''
'''
szoveg= "Hello Világ"
for kar in szoveg:
    print(kar,end='')
'''
szamlalo=0
nev=input("Add meg a neved kisbetűvel: ")
for kar in nev:
    if szamlalo==0:
        print(kar.upper(),end='')
    else:
        print(kar,end='')
    print(szamlalo,end=' ')
    szamlalo += 1

