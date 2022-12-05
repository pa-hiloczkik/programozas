#A python lista
lista= ["alma","banán","cseresznye"]
print(lista)
#----------------------------------------------------------------------------------
lista= ["alma","banán","cseresznye","alma","banán"]
print(lista)
print(lista[0])
print(lista[3])
#----------------------------------------------------------------------------------
lista= ["alma","banán","cseresznye"]
print(len(lista))
hossza = len(lista)
print(hossza)
#----------------------------------------------------------------------------------
lista1= ["alma","banán","cseresznye"] #string
lista2=[1, 5, 7, 9, 3] #int
lista3=[True, False, True] #bool
#----------------------------------------------------------------------------------
lista1 = ["abc", 34, True, 40, "férfi"]
print(lista1)
#----------------------------------------------------------------------------------
lista5 = ["alma","banán","cseresznye"] 
print(type(lista5))
#----------------------------------------------------------------------------------
lista= list(("alma", "banán", "cseresznye")) # vegye figyelembe a zárójeleket
print(lista)
#----------------------------------------------------------------------------------
# írassuk ki a lista utolsó elemét:
lista= ["alma","banán","cseresznye"]
print(lista[-1])
print(lista[2])
#cseresznye
#----------------------------------------------------------------------------------
lista= ["alma-0","banán-1","cseresznye-2","alma-3","banán-4","narancs-5","kivi-6"]
print(lista[2:5])
#----------------------------------------------------------------------------------
lista= ["alma-0","banán-1","cseresznye-2","alma-3","banán-4","narancs-5","kivi-6"]
print(lista[:4])
#----------------------------------------------------------------------------------
lista= ["alma-0","banán-1","cseresznye-2","alma-3","banán-4","narancs-5","kivi-6"]
print(lista[2:])
ujlista=(lista[2:])
print(ujlista)
#----------------------------------------------------------------------------------
lista= ["alma-0","banán-1","cseresznye-2","alma-3","banán-4","narancs-5","kivi-6"]
print(lista[-4:1])
#----------------------------------------------------------------------------------
lista_10D_1csop=[]
lista_10D_1csop=["FB","GM","HK","KG","MM","OA","PJ","PP","SP","SR","SM","TB","TS","TT"]
csop1=[]
csop2=[]
csop3=[]

csop1= lista_10D_1csop[0:5]
csop2= lista_10D_1csop[5:10]
csop3= lista_10D_1csop[10:]

print(csop1)
print(csop2)
print(csop3)

#-----------------------------------------------------------------------------------
lista= ["alma-0","banán-1","cseresznye-2","alma-3","banán-4","narancs-5","kivi-6"]
print(lista[-4:- 1])
#-----------------------------------------------------------------------------------
lista_10D_1csop=[]
lista_10D_1csop=["FB","GM","HK","KG","MM","OA","PJ","PP","SP","SR","SM","TB","TS","TT"]
megbukottak=lista_10D_1csop[10:]
print(megbukottak,"megbuktak")
#-----------------------------------------------------------------------------------
