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
for x in range(10):
    lista.append(random.randrange(100))
for x in lista :
    check= int(x/2)
    if check*2 == x :
        print(x)

# stampa 10 nuumeri casuali riportando il numero di giri e rispettando le condizioni
import random 
lista=[]
count=0
for x in range (10):
    r = random.randrange(100)
    lista.append(r)
    if r>50 or r<10:
        print(r)
        count=count+1
        print(count , "questo e il mio count")



#Chiedi all’utente di inserire 5 numeri e stampa i numeri man mano che vengono inseriti

def ciao():
    numeri= int(input("inserisci numero "))
    print(numeri)

for x in range(5):
    ciao()

# farlo solo con il for 

for x in range(5):
    numeri= int(input("inserisci un numero"))
    print(numeri)

#Chiedi all’utente di inserire 5 numeri e stampa i numeri in ordine inverso

lista1=[]

def ciao1():
    numeri= int(input("inserisci numero "))
    lista1.append(numeri)    

for x in range(5):
    ciao1()

lista1.reverse()
print(lista1)

#Chiedi all’utente di inserire 5 numeri e stampa solo i numeri pari in ordine inverso

lista2=[]

def ciao2():
    numeri= int(input("inserisci numero "))
    if numeri%2==0:
        lista2.append(numeri)    

for x in range(5):
    ciao2()
lista2.reverse()
    
print(lista2)

#Chiedi all’utente quanti numeri vuole inserire. Leggi tutti i numeri in input. Stampa tutti i numeri inseriti al quadrato

n_utente= int(input("quanti numeri vuoi inserire "))

def quadrato():
    numero=int(input("inserisci numero"))
    print(numero*numero)
for x in range (n_utente):
    quadrato()

#Definisci una funzione chiamata ‘primo’ che riceva come parametro un numero intero e ritorni true in caso il numero fosse primo
#Chiedi all’utente di inserire un numero. Stampa “primo” nel caso si tratti di un numero primo.


k=int(input("inserisci numero"))

def primo (k):

    for x in range (2,k):
        check= int(k/x)
        if check*2==k : 
            return False
    print("primo")
    return True 
    
print(primo(k))



#Scrivi una funzione che, data una lista di numeri in input, fornisce in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.
#Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:

n= int(input("quanti numeri vuoi inserire "))
lista=[]

def istogramma ():
    a=int(input("inserisci"))
    lista.append(a)

for x in range(n):
    istogramma()

for y in lista :
    print("*" * y)


#Definisci una funzione che riceva in input un numero indefinito di parametri. Stampi solo il terzo e il quarto (se esistono)



a=int(input("scegli numeri"))
lista=[]

def sbo ():
    b=int(input("scegli numeri"))
    lista.append(b)
for x in range(a):
    sbo()

if a<3 :
    print("la lista non e più lunga di due ")
if a ==3:
    print(lista[2])
if a>=4: 
    print(lista[2], lista[3])


#Scrivi una funzione che dato in input un numero h e un carattere c stampi un albero di natale fatto di caratteri di altezza h
h=int(input("inserisci l'altezza"))

c=str(input("inserisci un carattere"))

spazi= 1
caratteri= h-spazi

def albero ():
   print(" " *(h-x-1)+ c * (2*x+1))

for x in range (h):
    albero()





