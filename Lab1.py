"""
2024/25
Author: Natan Giassi 
@General-Kainobi_
"""
import math 
import random
import os

#Costruire una funzione che dato un array rimuove i duplicati e ne crea un alista con solo uno dei val. indicati
def noduplici(lista):
    noduplic=[]
    for item in lista:
        if item not in noduplic:
            noduplic.append(item)
    return noduplic
        
""" 
    Proprietà delle Liste:
        lista[-1] ritorna l'ultimo elemento della lista e in generale con indice negativo si conta alla rovescia dalla fine dell'array(l'indice -n sarà uguale all'indice 0)
        Se pongo list1=list2 le due liste punterano nello stesso luogo all'interno dell amemoria, quindi modificando uno modifichi l'altro
        se si vuole fare una copia di una lista allora si usa il comando .copy()
            es. list3=[1,4,3,5]
                list4=list3.copy()
        Somma di tutti i valori all'interno di una lista si può usare la funzione sum(lista)
        Mappare:
            Applicare una funzione su ciascun elemento di una sequenza
        Filtrare elementi:
            Selezionare solo alcuni elementi per creare una sottolista desiderata
        List Comprehension: Creare una lista nuova in maniera veloce e compatta 
            (Operazione) FOR (elementi nella lista) IF (condizione richiesta sulla lista(filtro))
    Dizionari:
        sequenza di elementi con chiave-elemento
        es.
            Dizionario= {chiave:elemento, chiave1:elemento1, chiave2:elemento2}
            Per chiamare il dizionario:
                dix[chiave]=elemento
"""

""" 1. Stampare l'equivalente di 538 minuti nel formato 12h:32min
2. Definire una funzione che prende come argomento una parola e una lettera. Ritorna quante volte
quella lettera è contenuta nella parola.
3. Scrivere una funzione che prende in input una stringa e ritorna True se è un palindromo, False
altrimenti.
4. Definire una funzione che dati 3 numeri interi stabilisce se possono essere i valori dei lati di un
triangolo e se si di che tipo di triangolo
5. Definire una funzione che prende in input una lista A, indici i, j, e scambia il valore di A[i] con A[j].
6. Definite la funzione fattoriale
7. Scrivere una funzione che prende in input due liste e ritorna `True` se le due liste hanno almeno un
elemento in comune
8. Definire una funzione che prende in input una lista di numeri interi in [0, 9] e ritorna una lista di
stringhe, corrispondenti ai numeri scritti in Italiano, es. [1,0,7,9,8] ->["uno","zero","sette","nove","otto"]  """


def es1(minuti):
    ore = int(minuti/60)
    minutirim= minuti%60
    print(ore,":",minutirim)
def es2(strings, lettera):
    conta=0
    for lettera in strings:
        conta+=conta+1
    print("La lettera appare ", conta, " volte\n")
def es3(strings):
    j=0
    for i in range(len(strings)):
        if strings[j]!=strings[-j]:
            return False
            j+=1
        else: return True
    #OPPURE stringa[::-1] torna la stringa al contrario quindi posso scrivere: 
    # if stringa==stringa[::-1]: return True 
    # else: return False
    #PERò possiamo scrivere direttamente:
    # return stringa==stringa[::-1]
def es4(l1,l2,l3):
    if l1+l2>l3 or l1+l3>l2 or l2+l3>l1:
        #può essere un triangolo
        if l1==l2 and l2==l3:
            return("Equilatero")
        elif l1==l2 and l2!=l3 or l1==l3 and l3!=l2 or l2==l3 and l3!=l1:
            return("Isoscele")
        else: return("Scaleno")
    else:return("NON é UN TRIANGOLO")
def es5(a, i, j):
    #scambia 
    tmp=a[i]
    a[i]=a[j]
    a[j]=tmp
    return a
def es6(n):
    if n==1:
        return 1
    else: return(n*n-1)
def es7(lista1, lista2):
    for item in lista1:
        if item in lista2:
            return True
    else: return False          
def es8(lista09):
    listanew=[]
    diz={0:"zero", 1:"Uno", 2:"Due", 3:"Tre", 4:"Quattro", 5:"Cinque", 6:"Sei", 7:"Sette", 8:"Otto", 9:"Nove"}
    for item in lista09:
        listanew.append(diz[item])
    return listanew

def main():
    lista=[1,4,3,3,6,3,1,2]
    #print(noduplici(lista))
    #es1(538)
    #es2("ciaobellaciao", "a")
    #print(es3("natan"))
    #print(es8(lista))

"""" 
I file CSV:
    Comma seperated values ---PARTE 3 Slide
    Valori separati da virgole dove ogni riga è una entry e ogni virgola denota una colonna diversa
    Metodi specifici di python per legger i file csv
        Operazione principale(file.estensione, 'modalità di acc')
        Le modalità di accesso sono delle singole lettere(presenti nel file slide parte3 pg 17)
        le operazioni sono:
            file.readline()
                Fornisce la sola  prima riga e poi la seconda etc. non c'è modo di chiamare specificatamente la n-esima riga
            with open(file.ext) as file
                Toglie la necessitazione di usare .open e .close
            file.write('') 
                aggiunge una riga al file con dentro scritto la stringa fornita
                // non lo useremo molto
            file.split('')
                separa le stringhe su un carattere specifico
            
        Quando uso file.read l'oggetto creato è di tipo STRING e si possono usare tutti i metodi associati alle stringhe(print, len, ricerca car. etc)
        Una volta usato l'operazione file.open bisognerà anche chiudere il file con il comando file.close

    Lavorare con i file csv:
    1) Vogliamo lavorare con numeri separati quindi usiamo riga.split(',') che separa in ogni riga i valori separati tra loro dalla virgola
    2) Covertare la stringa in un valore numerico(float, intero etc)//ovviamente la stringa deve essere un numero
    3) Aggiungere ad una lista il valore della riga usando .append()
    Esempio:
        # Inizializzo una lista vuota per salvare i valori
        values = []
        # Apro e leggo il file, linea per linea
        my_file = open('shampoo_sales.csv', 'r')
        for line in my_file:
            # Faccio lo split di ogni riga sulla virgola
            elements = line.split(',')
            # Se NON sto processando l’intestazione...
            if elements[0] != 'Date': #La prima riga la saltiamo poichè ci dice cosa contengono le varie colonne, in questo caso 'Date' è il primo elemento della prima riga
                # Setto la data e il valore
                date = elements[0]
                value = elements[1]
            # Aggiungo alla lista dei valori questo valore
            values.append(value)


    La libreria os
        Fornisce dei comandi per poter navigare e modifcare file e directoy del sistema
        si chiama all'interno del programma con "import os"
        os.getcwd() ritorna il Path del directory nella quale si sta lavorando in quel momento
Importare Moduli
    File.py con al suo interno vari metodi(funzioni) che possiamo chiamare senza dover riscriverli ogni volta
    Per importare moduli senza farli eseguire quando eseguo il mio file principale serve:
        if __name__ == '__main__':
            main()


"""
#Esercizio su csv Scrivete una funzione sum_csv(file_name) che sommi tutti i valori delle vendite degli shampoo del file passato come argomento
def sum_csv():
    elements=[]
    open(shampoo_sales.csv, 'r')
    elements=line.split(",")




if __name__ == '__main__':
    main()