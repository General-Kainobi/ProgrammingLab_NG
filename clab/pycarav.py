import random
import os

"""
Classi
    See Lab1.py 
    Eredetarietà
        Classe principale
        Sottoclasse che eredita tutte le variabili e metodi della classe principale e hanno in aggiunta metodi e variabili specifiche
        Ad esempio:
            Persona di Units - nome cognome , codice fiscale, orario
                Docente - corsi insegnati, durata contratto, data inizio lavoro
                Studente - voti, matricola, media voti, anno immatricolaz.
                Tecnico - etc.
        OverWriting
            Nelle sottoclassi si può sovvrascrivere i metodi della superclasse in modo da avere comportamento diverso per quel specifico oggetto
                Es. Studente e docente hanno entrambi il metodo voti ma nello studente tornerà i voti presi e nel docente i voti dati.
List Comprehension:
    Esempio:
            quad=[]
            for n in range(10):
                quad.append n**2
        Che è equivalente ad:
            [n**2 for n in range(10)]
    Iterabile:
        Qualsiasi insieme di oggetti che abbiano un ordine
        Matematicamente qualsiasi insieme che sia in biezione coi numeri naturali(f: X-->N)
    Creare un iteratore:
        Hanno sempre bisogno dei due metodi __iter__ e __next__
        class iteratore:
            def __iter__(self):
               ---- 
            def __next__(self):
                ----
        Esempio:
            class MyNum:
                def __iter__(self):
                    self.a=0        //stato interno dell'iteratore
                    return self
                def __next__(self):
                    self.a+=1
                    return self.a-1 // calcola e restituisce il prox. elemento
            for x in MyNum(): // iter x un numero infinito di volte poichè self.a+=1 senza mai finire

            class MyRange:
                def __init__(self, s=0,e):
                    self.s=e
                    self.e=e
                def __iter__(self):
                    return self
                def __next__():
                    if self.s>=self.e:
                        raise StopIteration
                    else:
                        self.s+=1
                        return self.s-1
        La scrittura 'for iter in iterabile': è equivalente ad;
           'iter_obj=iter(iterabile)
            while True:
                try: 
                    element=next(iter_obj)
                except StopIteration:
                    break  //interrompe il while di cui fa parte

            '    
"""

class Flusso:
    def __init__(self, x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def __iter__(self):
        return self
    def __next__(self):
        if(self.x>self.y):
            raise StopIteration
        self.x += self.z
        return self.x-self.z
#[print(i) for i in Flusso(1,10,1)]
    


def numprimo(n):
    for i in range(2,n):
        if (n%i==0):
            return 0
    return 1

class NumPrimi:
    def __init__(self, lista):
        l=[]
        for item in lista:
            if numprimo(item)==1:
                l.append(item)
        self.index=0
        self.l=l
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index+1>len(self.l):
            raise StopIteration
        return self.l[self.index-1]
        
a=[1,2,3,3,5,6,7,8,9,10] 
#[print(i) for i in NumPrimi(a)]

class Discre():
    def __init__(self,a,b, n):
        self.a=a
        self.c=a
        self.n=n
        self.delta=(b-a)/(n-1)
    def __iter__(self):
        return self
    def __next__(self):
        self.c+=1
        if self.c>=self.n:
            raise StopIteration
        return (self.a+(self.c-1)*self.delta)**2
        
[print(i) for i in Discre(0,2,5)]    


"""
class PotDue:
    def __init__(self,p,e):
        self.p=2**p
        self.e=2**e
    def __iter__(self):
        return self
    def __next__(self):
        if self.p>self.e:
            raise StopIteration
        else:
            self.p+=1
            return self.p-1
for x in PotDue(6,8):
    print(x)
"""

