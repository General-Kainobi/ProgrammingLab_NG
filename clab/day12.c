#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct lista{
    int valore;
    struct lista*next;
};
typedef struct lista lista;
typedef lista* elemento;

//funzioni utili
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
        while((*nuovo).valore!=-1){
            (*nuovo).next=malloc(sizeof(lista));// come scrivere nuovo->next=...
            nuovo= nuovo->next;//"scorro" avanti di un posto nella lista mettendo in nuovo il puntatore all'elemento successivo
            printf("Che valore metto all'%d-esimo posto?: ",i);
            scanf("%d",&x);//inserisco nel posto "nuovo" il valore che voglio
            if(x!=-1){
                nuovo->valore=x;
                nuovo->next=NULL;//chiudo la coda della lista
                i++;//lunghezza lista for bugs
            }else{break;  }     
        }return primo;    //torna la testa della lista che è rimasto invariato(teoricamente)}
    }return NULL;
}
int lunghezzalista(elemento testa){
    int c=0;
    while(testa->next!=NULL){
        c++;
    }
    return c;
}
void stampalista(elemento testa){
    printf("[ ");
    while(testa!=NULL){//finchè non arrivo all'ultimo puntatore della lista che ovviamente punterà a NULL
        printf("%d | ", testa->valore);
        testa=testa->next;
    }printf(" ]\n");
    
}
void freelist(elemento testa){
    while(testa!=NULL){
        elemento tmp=testa;
        free(testa);
        testa->next=tmp->next;
    }
}

elemento listadaarray(int*a, int n){
    elemento testa=(elemento)malloc(sizeof(elemento));
    testa->valore=a[0];
    testa->next=NULL;
    elemento attuale=testa;
    for(int i=1;i<n;i++){
        attuale->next=(elemento)malloc(sizeof(elemento));
        if (attuale->next == NULL) return testa;
        attuale=attuale->next;
        attuale->valore=a[i];
        attuale->next=NULL;
    }return testa;
}
//--

//es 8.2

void riempimento(int *array, int n){
    elemento testa=malloc(sizeof(elemento));
    testa->valore=array[0];
    testa->next=NULL;
    elemento attuale=testa;
    int c=0;
    for(int i=2; i<n;i+=2){
                attuale->next=(elemento)malloc(sizeof(elemento));
                attuale=attuale->next;//scorro avanti
                attuale->valore=array[i];
                attuale->next=NULL;
                c++;//conta i pari
        }//si potrebbe anche fare tutto quanto all'interno di questo for, e quando si arriva all'elemento n/4-esimo( ossia la metà degli elementi di indice pari(che sono a loro volta la metà degli elementi totali(n))
        // arrivati all'elemento n/4-esimo, tramite if inserirei il codice seguente che è dentro il for 
    attuale=testa;//una volta riempito la lista "torno" al puntatore iniziale ossia la testa per poterlo scorrere di nuovo fino a metà e aggiungere l'elemento richiesto
    int meta=(c/2);
    for(int i=0;i<=meta;i++){
        if (i==meta)
        {
            elemento temp =(elemento)malloc(sizeof(elemento));
            temp->valore = array[3];
            (temp->next)=(attuale->next);
            attuale->next=temp;
        }
        attuale=attuale->next;//sennò scorro avanti la lista

    }
    stampalista(testa);
    freelist(testa);//funzione che libera la memoria della lista
    free(array);
}


//es8.3 --- data una lista ordinata inserire un valore k in modo che la lista rimanga in ordine

elemento inseririmento_k(elemento testa, int k){
    elemento attuale=testa;
    while(attuale!=NULL){
        if(attuale->next==NULL&&k>=(attuale->valore)){
            elemento temp =(elemento)malloc(sizeof(elemento));
            temp->valore = k;
            (temp->next)=NULL;
            attuale->next=temp;
            return testa;
        }
        if((k>=attuale->valore && k<(attuale->next)->valore)){
            elemento temp =(elemento)malloc(sizeof(elemento));
            temp->valore = k;
            (temp->next)=(attuale->next);
            attuale->next=temp;
            attuale=attuale->next;
        }

        attuale=attuale->next;
    }
return testa;
}



int main(){
    int array[10]={0,1,2,3,4,4,6,7,8,9};
    int* array_din=(int*)malloc(10*sizeof(int));
    for(int i=0;i<10;i++){
        array_din[i]=array[i];
    }
    elemento testa= listadaarray(array, 10);
    //riempimento(array_din,10);
    stampalista(inseririmento_k(testa, 11));
    //freelist(testa);
    //free(array_din);
}