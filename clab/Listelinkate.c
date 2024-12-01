#include <stdio.h>
#include <stdlib.h>
#include <math.h>
/*esercizio per martedi:
Data una lista ed un valore x presente nella lista, eliminare dalla lista x
ossia, andare a cambiare il puntatore che punta ad x e farlo puntare al valore dopo x, e liberare la memoria da x


*/

//creazione struct di lista linkata
struct listalinkata{
    int valore;
    struct listalinkata *next;
};
typedef struct listalinkata lista;
typedef lista* elemento;


elemento riempimentolista(){
    int x;
    int i=0;
    printf("Che valore metto al primo posto? ");
    scanf("%d", &x);//valore del primo posto(0)
    if(x!=-1){
        elemento primo =malloc(sizeof(lista));
        primo->valore=x;
        primo->next =NULL;//metto nella posizione 1 il puntatore nullo(non abbiamo altri valori a cui puntare)
        elemento nuovo =primo;  // in questo modo fisso il puntatore di testa(primo) e ho una copia del suo puntatore per poter scorrere la lista(penso) 
        while(x!=-1){
            printf("Che valore metto all'%d-esimo posto?: ",i);
            scanf("%d",&x);//inserisco nel posto "nuovo" il valore che voglio
            if(x!=-1){
                (*nuovo).next=malloc(sizeof(lista));// come scrivere nuovo->next=...
                nuovo= nuovo->next;//"scorro" avanti di un posto nella lista mettendo in nuovo il puntatore all'elemento successivo
                nuovo->valore=x;
                nuovo->next=NULL;//chiudo la coda della lista
                i++;
            }        
        }return primo;    //torna la testa della lista che è rimasto invariato(teoricamente)}
    }return NULL;
}

//es 8.1 all parts
void lunghezzalista(elemento testa){
    int c=0;
    while(testa->next!=NULL){
        c++;
    }
    printf("La lista contiene %d elementi", c);
}

elemento eliminax(int x, elemento testa){
    elemento attuale=testa;// parto dal primo puntatore della lista(questo contiene in realtà sia un puntatore all'elemento successivo(next) che il valore della lista(valore))
    elemento preced= NULL;// il puntatore precedente è chiaramente nullo poichè non esiste puntatore definito alla testa della lista
    
    while(attuale!=NULL){
        if(attuale->valore==x){//controllo se nell'elemento della lista attuale ci sia il valore corrispondente a x{
            if(preced==NULL){//in caso x sia proprio il primo elemento
                elemento temp=attuale;//salvo temporanemente l'elemento attuale in modo da poter deallocare l'elemento giusto della lista senza perdere la testa(sennò non potrei accedere alla lista(almeno cosi ho capito che funzionino le liste))
                testa=attuale->next;//salvo una nuova posizione iniziale come il puntatore successivo(in questo caso il secondo elemento)
                free(temp);//dealloco la variabile temporanea
                attuale=testa;// metto l'elemento corrente come la nuova testa
            }
            else{
                preced->next=attuale->next;//l'elemento (x) viene messo a puntare all'elemento successivo
                free(attuale);//Dealloco la posizione attuale(x) ella lista(rimane vuoto ma esiste lo stesso la posizione in memoria ora vuota(speculazione))
                attuale=preced->next;//ossia, dalle dichiarazioni precedenti, attuale=attuale->next ossia avremmo un elemento della lista vuoto che punta al valore successivo(in teoria)
            }
        }else{
            preced=attuale;
            attuale=attuale->next;
            //se non ho trovato x, "scorro" la lista in avanti
        }
    }
    return testa;//torno la testa dell a lista che è quello che mi serve per poterne accedere
}


void stampalist(elemento testa){
    printf("[ ");
    while(testa!=NULL){//finchè non arrivo all'ultimo puntatore della lista che ovviamente punterà a NULL
        printf("%d, ", testa->valore);
        testa=testa->next;
    }printf(" ]\n");
    
}

int main(){
    int x;
    elemento testa = riempimentolista();//creazione lista da poter poi modificare/scorrere etc
    /*
    printf("Inserisci il valore da eliminare: ");
    scanf("%d", &x);*/
    testa = eliminax(x, testa);
    printf("lista: \n");
    stampalist(testa);

}


//Disegnare la memoria di questa funzione
    /*   struct liste{
            int info;
            struct liste*next;
        };

        typedef struct liste list;
        typedef list* nodo;
        aggiungi_in_coda(lista*liste, int x){
            nodo nuovonodo=(nodo*)malloc(sizeof(nodo));
            (*nuovonodo).info=x;
            nuovonodo->next=NULL;
            if(liste==NULL){
                liste=nuovonodo;
            }
            else{
                nodo obj=liste;
                while(obj->next!=NULL){
                    obj=obj->next;
                    obj->next=nuovonodo;
                }
            }
        }*/ 