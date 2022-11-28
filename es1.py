#Riempi 5 variabili con nomi di Animali, stampa i nomi
x= "elefante"
y="ciao"
z= "easy"
print(x,y,z)

#Riempi due variabili (x e y) con dei valori. Se x è maggiore di y stampa “ciao”. Se x è minore o uguale a y stampa “arrivederci”
x = 3
y =5 
if x>y:
    print("ciao")  
if x<y:
    print("arrivederci")

#Riempi tre variabili (x, y ,z) con dei valori. Se x è maggiore di y e maggiore di z stampa ‘X è il numero maggiore’ 
x = 300
y =5 
z = 70
if x>y and x>z:
    print(" x è il maggiore")

#Rifai l’esercizio C stampando il nome della variabile con il valore minore
x = 5
y =8
z = 9

lista=[x,y,z]
minore= lista[0]
for a in lista:
    if a < minore:
        minore=a 
print(minore)

#Crea due vettori uno con il nome di città e uno con il nome di persone Stampa usando dei cicli for per ogni città tutti i nomi degli abitanti
#es: [‘torino’, ‘milano’ ] | [‘gino’, ‘lino’]
#stampa: torino - gino | torino - lino | milano - gino | milano - lino

città= ["milano", "verona "]
persone= ["paolo","davide"]
for x in città:
    for y in persone:
        print(x,y)

# Riempi una lista di 5 numeri. E una variabile x. Stampa solo  i numeri maggiori di x
lista=[3,2,4,5,6]
x= 4
for y in lista:
    if y> x :
        print(y)

#Riempi una lista di 5 numeri e stampa il minore
lista=[3,7,5,9,8]
minore= lista[0]
for a in lista :
    if a < minore:
         minore=a
print(minore)

#Riempi una lista con 5 nomi di Animali e stampa la lista in ordine inverso
lista= ["zuppa", "ciao", "canini","bho", "sbomminata"]
lista.reverse()
print (lista)

#Dichiara due liste. Una con nomi di animali e l’altra con numeri. Aggiungi tutti gli elementi della seconda lista alla prima.
#Stampa soltanto i numeri maggiori di 5

animali=["rino","dino"]
numeri=[8,5,3,4,7,17]
lista=[]
for a in numeri:
    if a >5 :  
        lista.append(a)
print(lista+ animali)

#Riempi una lista di 10 numeri casuali (utilizza un ciclo for) e stampa solo i numeri pari
import random 
lista=[]
for x in range(10) :  
    lista.append(random.randrange(100))
    if x % 2 ==0:
     print(x)


import random 
lista=[]
for x in range(10)
    lista.append(random.randrange(100))
for x in lista 
check= (x/2)int 
     if check*2 == x 
     print(x)



