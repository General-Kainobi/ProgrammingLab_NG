#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//all'esame chiede una funzione che ordina l'array in modo ricorsivo


int *solopari(int a[], int n){
    int p = 0;
    for(int i=0;i<n;i++){
        if(a[i]%2==0){p++;}
        }//Numero di pari all'interno dell'array
        int *b=(int*)malloc(p*sizeof(int)); //array nello heap con dimensione p(numero di pari)
        int j=0;
        for(int i=0;i<n;i++){
            if(a[i]%2==0){b[j]=a[i];j++;} //assegno nel puntatore array b i valori pari presenti nell'array a
        }
    return b;
    }

int *ordina_heap(int c[], int n){    
    for (int i = 0; i < n- 1; i++) {
        for (int j = i + 1; j <n; j++) {
            if (c[i] > c[j]) {  // ordina in modo crescente
                int temp = c[i];
                c[i] = c[j];
                c[j] = temp;
            }
        }
    }
    for(int j=0; j<n;j++ ){
        printf("%d, ", c[j]); // stampa l'array ordinato
    }
    return c;
    }

int *merge(int*a, int n, int *b, int m){
    int* p=(int*)malloc((n+m)*sizeof(int));
    for(int i=0;i<n;i++){
        *(p+i)= *(a+i);
    }
    for(int i=0;i<m;i++){
        *(p+n+i)= *(b+i);
    }
    ordina_heap(p, n+m);
    return p;

}
    
// esercizo 6.1 bis
    int trovamas(int *a, int n){
        int max=a[0];
        for(int i=1; i<n;i++){
            if (a[i]>max){max=a[i];}// a[i] equivalente a scrivere *a(i) poichè gli array sono puntatori
        }
        printf("%d è il massimo valore dell'array\n", max); return max;
    }
    float media(int *a, int n){
        float media;
        int tot = 0;
        for(int i=0; i<n;i++){
            tot+=a[i];
        }
        media = tot/n;
        return media;     
    }
    float varianza(int *a, int n){
        int tmp =0; float k;
        float meda=media(a, n);
        for(int i=0; i<n;i++){
           k= tmp+ (((a[i]-meda) * (a[i]-meda)));
           tmp=k;
        }
        k=k/n;
        printf("%f è la varianza  dell'array\n", k); return k;
    }

int contadupe(int a[], int n) {
    int dupe = 0;
    for (int i=0; i < n; i++) {
        for (int j =i+1; j <n; j++) {
            if (a[i]==a[j]) {
                dupe++;
                break;  // Smette di contare una volta trovato un duplicato
            }
        }
    }
    return dupe;
}
int *duplicati(int *a, int n) {
    int *arraydupe = (int *)malloc((n - contadupe(a, n)) * sizeof(int));  // Correct size
    int z = 0;
    for (int i = 0; i < n; i++) {
        int is_dupe = 0;
        for (int j = 0; j < z; j++) {
            if (a[i] == arraydupe[j]) {
                is_dupe = 1;
                break;
            }
        }
        if (is_dupe==0) {
            arraydupe[z] = a[i];
            z++;
        }
    }

    for (int i = 0; i < z; i++) {
        printf("%d, ", arraydupe[i]);
    }
    return arraydupe;
}

void main(){
    int a[7]={3,4,6,6,3,2,6};
    int b[8]={61,41,23,42,3,5,24};
    //merge(a,7,b,8);
    //varianza(a, 7);
    duplicati(a, 7);

}