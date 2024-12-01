#include <stdio.h>
#include <stdlib.h>

int minimo_indice(int a[], int n){
    int min_pos = 0;
    for (int i=1; i<n; i++){  
        if(a[i]<a[min_pos]){
            min_pos=i;
            }
    }return min_pos;
}

int conta_element(int a[], int n, int x){
    int c=0;
    for (int i=0; i<n; i++){
        if (a[i] == x){
            c++;
        }
    }return c;
}

int min_unico(int a[], int n){
    if (conta_element(a, n, minimo_indice(a, n))>1){
        return -1;
    }
    else return(minimo_indice(a, n));
}

int min_unicodue(int a[], int n){
    int indice_min =0;
    int conta =1;
    for (int i=1; i<n; i++){
        if(a[i]<a[indice_min]){
            indice_min=i;
            conta=0;
        }
        if (a[i]==a[indice_min]){
            conta++;
        }
    }
    if (conta>1){
        return -1;
    }else return indice_min;
}


//si consideri un array A di n interi, due elementi x,y > 0 , 
//a) restituire il numero di elementi di A che sono divisbili per x e maggiori di y
//b) Il numero di occorenze di x che si trovino in posizione antecedenti a tutte le occorenze di y


int trova_y(int a[], int n, int y){
    for(int i=0; i<n;i++){
        if (a[i]==y){
            return i;
        }
    }return n;
}
        
int richiesta(int a[], int n, int x, int y){
    int conta_a;
    int conta_b;
    for(int i=0; i<n;i++){
        if(a[i]%x==0 && a[i]>y){
            conta_a++;
        }
    }
    conta_b = conta_element(a, trova_y(a,n,y),x);
}

// Dato un array A di 10 elementi,  dato un array B di 10 elementi, 
//a) costruire un array C di 20 elementi che contenga gli elementi di A e B, ordinati;
//b) Si risolva di nuovo a) supponendo che A e B siano ordinati; 
int trova_max(int a[], int n){
    int max = a[0];
    for (int i=1; i<n-1; i++){  
        if(a[i]>max){
            max=a[i];
            }
    }return max;    
}
int ordina_a(int a[], int b[]){
    int c[12];
    for (int i=0;i<12;i++){
        if (i<6){
            c[i]=a[i];
        }
        else c[i]=b[i-6];
    } //costruisce C
    
    for (int i = 0; i < 12 - 1; i++) {
        for (int j = i + 1; j < 12; j++) {
            if (c[i] > c[j]) {  // ordina in modo crescente
                int temp = c[i];
                c[i] = c[j];
                c[j] = temp;
            }
        }
    }
        for(int j=0; j<12;j++ ){
        printf("%d, ", c[j]); // stampa l'array ordinato
    }
    }

    //se a,b sono ordinati, tra di loro sono comunque disordinati.  
    //Dovremmo controllare che un qualsiasi elemento che scegliamo come minimo di A sia minore di OGNI elemento di B.
    // Se ogni elemento di a è minore di ogni elemento di b posso semplicemente concatenare i due array e sarà C gia ordinato

void ordina_b(int *a, int *b, int n, int m){
    int*c = (int*)malloc((n+m)*sizeof(int));
    int i = 0, j = 0, k = 0;
    while (i < n && j < m) {
        if (a[i] <= b[j]) {   // <= per valori uguali nei due array
            c[k] = a[i]; i++;
        } else {
            c[k] = b[j]; j++;
        }k++; 
    }
    while (i < n) {
        c[k] = a[i];i++; k++;
    }
    while (j < m) {
        c[k] = b[j];j++; k++;
    }
    // I due while per copiare elementi avanzati da A o B nel caso che siano di lunghezze diverse
    for(int j=0; j<(n+m);j++ ){
        printf("%d, ", c[j]); // stampa l'array ordinato
    }free(c);
}

int main(){
    int a[6]={2,4,6,8,9,99};
    int b[9]={1,3,5,7,9,10,56,97,98};
    ordina_b(a,b, 6, 9);
    
}