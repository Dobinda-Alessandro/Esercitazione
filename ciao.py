import random 
lista=[]
for x in range(10):
    lista.append(random.randrange(100))
for x in lista:
     check= int(x/2) 
     if check*2 == x : 
        print(x)
