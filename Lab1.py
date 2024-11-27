"""
2024/25
Notes for the Programming laboratory at the University of Trieste
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
    sum=0
    open('shampoo_sales.csv', 'r')
    for line in 'shampoo_sales.csv':
        elements=line.split(",")
    for element in elements:
        sum+=element 
    print(sum)

"""
1. Definire una funzione che prende in input un file ed una parola e conta quante volte
quella parola è presente sul file
2. Definire una funzione che prende come input un file e conta quante volte ogni parola è
presente
3. Definire una funzione che prende in input un file e costruisce un dizionario con chiavi la
lettere iniziali e con valore le parole di lunghezza maggiore contenute nel file che
iniziano con quelle lettere.
4. Definire una funzione conteggio che prende come input un file e ritorna un dizionario
con chiave la prima parola di ogni frase e valore il numero di volte che una frase inizia
con quella parola. Considerare come inizio di frase qualsiasi parola che segue un
punto, un punto esclamativo, un punto interrogativo o si trova all'inizio del testo.
5. Definire una funzione legge prende come input un file, rimuove tutte le righe duplicate,
scrive il risultato in un nuovo file chiamato unique.txt.

"""
def es2_1(file, word):
    words=[]
    c=0
    with open(file, 'r'):
        for line in file:
            words=line.split(" ")
        for element in words:
            if word==element:
                c+=1
        print("Your file has ", c, " uses of the word: ", word,"\n")

def es2_2(file):
    count=[]
    with open(file, 'r'):
        for line in file:
            words=line.split(" ")
        print("Counter of words: \n")
        for i in range(len(words)):
            count.append(words.count(words[i]))
            print(words[i],": ", count[i], "Occurrences")

def es2_3(file):
    words=[]
    dic={}
    with open(file, 'r'):
        for line in file:
            words.extend(line.split())
        for word in words:
            if word.split()[0] not in dic or len(word)>len(dic[word.split()[0]]):
                dic[word.split()[0]]=word
    
def es2_4(file):
    count={}
    phrase=[]
    with open(file, 'r'):
        for line in file:
            phrase.extend(line.split("!", ".", "?"))
        for word in phrase:
            first=word.split()[0]
            if first not in count:
                count[first]=phrase.count(first)
        return count

def es2_5(file):
    with open(file, 'r'):
        temp=""
        for line in file:
            if line!=temp:
                'unique.txt'.write(line)
            temp=line
    return 'unique.txt'
        
"""
Costrutto WITH per i file
    Esegue per se i metodi __enter__ ed __exit__ per aprire e chiudere i file 
    in modo automatico. Usato anche nei databae, nei file compressi e nelle conessioni a rete

Gli oggetti in Python:
    Paradigma di programmazione differente dal C
    Si ragiona in termini di entità e non solo di funzioni
    Gli oggetti sono definiti con le classi, una struttura che contiene attributi(variabili) e metodi(funzioni)
    Una volta inizializzata una classe si dice ISTANZA della classe
    Una classe instanziata si dice OGGETTO e ha le proprietà generalizzate della classe con valori specifici che lo differiscono dagli altri oggetti(Classe di cani: oggetto: cane maltese piccolo di 2 anni color bianco)
    Possiamo ad esempio definire
    Classe persona
        - nome ---attributo
        -saluta() ---metodo
            print'ciao!'
    istanza persona:
        - nome=mario
        - saluta()
    Perche si usano?
        Permettono di sfruttare e definire delle gerarchie e sfruttare caratterisiche comune
        Una volte istanziato un oggetto si può facilmente mantenere lo stato, senza dovermi appoggiare ad altre strutture dati di appoggio
     Convenzioni:
        Notazione snake_case (carattere minuscolo e underscore) per i nomi dei metodi variabili e delle istanze degli oggetti            Notazione CamelCase per il nome delle classi(Maiuscole e parole unite)
        Doppi underscore prima e dopo il nome di un metodo indicano un metodo ad uso esclusivamente interno
        Che non vengono richiamati al di fuori della classe
        Apici doppi per le stringhe interne e singole agli estremi
    Operazioni in-place
        Modificano l'oggetto dato originale, non ha nessun return
            ad esempio string.reverse()
    Operazione non in-place
        come return ti torna il risultato della operazione ma non modifica l'oggetto originale
            ad esempio string.split()
    Può essere utile non creare una nuova istanza e fare le operazioni in-place per risparmiare memoria e potere computazionale
    !! bisogna stare attenti e ricordarsi che quando si usano le operazioni in place si ha modificato il dato iniziale
    Definire oggetti
        class Person():
            pass //è l'istruzione nulla, serve per avere il blocco vuoto
        
        person=Person() // creo una istanza "person" della classe Person()
        print person
    ----------------------------------------------------------------------
        import random //libreria per randomizzare scelte
        class Person(): // come paramatrei la classe non ha nulla se non la classe di gerarchia superiore
            def __init__(self, name,surname): //Metodo interno(costruttore) che è responsabile per inizializzare l'oggetto
                self.name=name                 //self è obbligatorio come paramtero in tutti i metodi degli oggetti
                self.surname=surname
            def __str__(self): //metodo speciale che viene eseguito quando si chiama print(istanza oggetto)
                return'Person "{} {}"'.format(self.name,self.surname) 
            def say_hi(self): //metodo "opzionale" che viene chiamato con istanza.say_hi
                randnum=random.randint(0,2)
                if randnum==0:
                    print('Hello, I am {}, {}'.format(self.name, self.surname))
                if randnum==1:
                    print('Hi, I am {}!'.format(self.name))
                if randnum==2:
                    print('Yo bro! {} here!'.format(self.name))
            

        person=Person('Mario', 'Rossi') // vengono presi come argomenti del metodo init
        print(person) ==== Mario Rossi
        person.say_hi() ==== una a caso tra i tre saluti definiti
    -----------------------------------------------------------------
    Gli oggetti sono mutabili
        Si possono assegnare nuovi valori agli attributi di oggetti già definiti
    Estendere oggetti: l'ereditarietà e la gerarchia
        Il concetto di erederitarietà permette,  a partire dalla classe genitore, di creare classi figlie, cioe di definire nuovi classi come versioni modificate di classi gia definite
            Esempio di gerarchia:
                Essere viventi:
                    Mammiferi
                        Bipedi
                        Quadrupedi
                    Rettili
        L'estensione di una classe si chiama anche SPECIALIZZAZIONE
        Le classi figlie
            -ereditano tutti gli attributi e metodi della classe genitori
            - MA possono sovreascrivere i metodi ereditati per personalizzarli e possono aggiungerne di nuovi per estendere la funzionalità ad uso specifico
            - Le modifiche alla classe figlia non impattano la classe genitore
        ESEMPIO:
            class Person():
                ----

            class Student(Person):
                def __str__(self):
                    return'Student "{} {}"'.format(self.name,self.surname)
    
            class Professore(Person):
                def __str__(self):
                    return'Prof.  "{} {}"'.format(self.name,self.surname)
                def day_hi(): //sovvrascrivo il metodo say_hi() della funzione padre
                    return'Hello I am professor  "{} {}"'.format(self.name,self.surname)
                def og_say_hi():
                    super().say_hi() // il metodo super mi accede alla funzione dell'oggetto padre, anche se l'ho sovvrascritta
    ----------------------------------------------------------------------------
    Stile di codice
        • Usa un'indentazione di 4 spazi e non usare tabulazioni. Le tabulazioni
        introducono confusione e sarebbe meglio evitarle.

        • Suddividi le righe in modo che non superino 79 caratteri. Questo aiuta gli
        utenti con display piccoli e rende possibile visualizzare più file di codice
        affiancati su schermi più grandi.

        • Usa righe vuote per separare funzioni e classi, oltre che per separare blocchi
        di codice più grandi all'interno delle funzioni.

        • Quando possibile, inserisci i commenti su una loro riga separata.
        • Usa le docstring.

        • Usa spazi intorno agli operatori e dopo le virgole, ma non direttamente
        all'interno delle parentesi: ad esempio a = f(1, 2) + g(3, 4).
        Dai un nome alle tue classi e funzioni in modo coerente, CamelCase per le
        classi, snake_case per funzioni e variabili.

        ● Usa sempre self come nome per il primo argomento di un metodo

        ● Non utilizzare codifiche complesse se il tuo codice è destinato a essere
        utilizzato in ambienti internazionali. Il semplice ASCII funziona meglio in ogni
        caso.

        ● Tutte le convenzioni e molto altro lo trovare nei PEP (Python Enhancement
        Proposal). Servono come documentazione tecnica per spiegare le
        motivazioni, i dettagli e gli effetti delle modifiche proposte.

        ● Il PEP 8 - Style Guide for Python Code: https://peps.python.org/pep-0008/
"""
#Classe della moneta col metodo per lanciarla
class moneta():
    def __init__(self):# self può anche essere cambiato con un qualsiasi nome poichè è una var. locale
        self.lato= "testa" # però per convenzione si usa il nome self
    def __str__(self):
        return(self.lato)
    def lancia_moneta(self):
        randnum=random.randint(0,1)
        if randnum==0:
            self.lato="Testa"
        else:
            self.lato="Croce"

"""
Esercizio 1
Create un oggetto CSVFile che rappresenti un file CSV, e che:
1) venga inizializzato sul nome del file csv, e
2) abbia un attributo “name” che ne contenga il nome
3) abbia un metodo “get_data()” che torni i dati dal file CSV come lista di liste,
ad es: [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ]
Provatelo sul file “shampoo_sales.csv”.
Poi, scaricate il vostro script Python e testatelo su autograding
p.s. il massimo punteggio è 9/10 con quello che abbiamo visto fino ad oggi a lezione.


Esercizio 2: Classe Veicolo
Scrivete una classe denominata Veicolo che disponga di questi attributi dati:
● modello (per il modello del veicolo);
● marca (per la marca del veicolo);
● anno (per l'anno del veicolo).
● speed (per la velocità del veicolo)
E di questi metodi:
● __init__ che accetti come argomenti l’anno, il modello, e la marca. Il metodo dovrebbe inoltre
assegnare 0 all’attributo dati speed.
● __str__ che restituisce una stringa con i dettagli del veicolo (marca, modello, anno e velocità)
● accellerare che aggiunge 5 all’attributo dati speed ogni volta che viene chiamato.
● frenare che sottrae 5 dall’attributo dati speed ogni volta che viene chiamato.
● get_speed che restituisce la velocità corrente.


Esercizio 3
● Crea una sottoclasse auto che ha in aggiunta l'attributo numero_porte e
cambia il metodo _str__ di conseguenza
● Crea una sottoclasse moto che ha in aggiunta l'attributo tipo (ad esempio,
"Sportiva" o "Touring") e cambia il metodo _str__ di conseguenza

"""
def ogg_es1():
    class CsvFile():
        def __init__(self,nome):
            self.nome=nome
        def getdata(self):
            list=[]
            for line in self.nome:
                list.append(line)


    



def main():
    #lista=[1,4,3,3,6,3,1,2]
    #print(noduplici(lista))
    #es1(538)
    #es2("ciaobellaciao", "a")
    #print(es3("natan"))
    #print(es8(lista))
    #es2_2('shampoo_sales.csv')
    pass

if __name__ == '__main__':
    main()