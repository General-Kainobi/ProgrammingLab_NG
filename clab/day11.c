#include <stdio.h>
#include <stdlib.h>
#include <math.h>


//es 7.6
int* inverti(int a[], int n){
    int m = n-1;
    for(int i=0;i<n/2;i++){
        int tmp=a[i];
        a[i]=a[m];
        a[m]=tmp;
        m--;
    }return a;
}

int pmalindromo(int a[], int n){
    int x=0;
    for(int i=0;i<n/2&&n!=n/2;i++){
        if (inverti(a, n)[i]==a[n]){
            x=1;
            n--;
        }else {int x=0;}
}return x;}


int contr(int *a,int n,int i)
{
    if(*(a+i)!=*(a+(n-1-i))) return 0;
    if((i==n/2)&&(*(a+i)==*(a+(n-1-i)))) return 1;
    return contr(a,n,i+1);
}
 
int palindromo(int *a,int n)
{
    int i=0;
    return contr(a,n,i); //1 se è palindromo, 0 se non lo è
}
//es 7.5

float*somma(float *a,int n){
    float tmp=0;
    for(int i=0; i<n; i++){
        a[i]=tmp+1/((2.0*i+1.0)*(2.0*i+1.0));
        tmp=a[i];
    }return a;
}

/*float serie(float *a, int n){
    float*a=somma(a,n);
    for (int i = 0; i < n; i++) {
        printf("%f, \n", a[i]);
    }
}
*/
//es 7.7 compressione di una serie di interi, torna il numero delle instanze contate di un numero seguite dal numero stesso

int* elementiarray(int *a,int n, int*dim){
    int c = 0; // Numero di gruppi distinti
    for (int i = 0; i < n; ) {
        int conta = 1;
        // Conta le occorrenze consecutive di a[i]
        while (i + 1 < n && a[i] == a[i + 1]) {
            conta++;
            i++;
        }
        c++; // Incrementa il numero di gruppi
        i++; // Passa all'elemento successivo
    }

    *dim = 2 * c; // Dimensione del nuovo array
    int *b = (int *)malloc(*dim * sizeof(int));
    int index=0;
    for (int i = 0; i < n; ) {
        int conta = 1;
        // Conta le occorrenze consecutive di a[i]
        while (i + 1 < n && a[i] == a[i + 1]) {
            conta++;
            i++;
        }
        b[index++] = conta;  // Salva il conteggio
        b[index++] = a[i];   // Salva il valore
        i++; // Passa all'elemento successivo
    }
return b;
    }

void es77() {
    int n = 0;
    printf("Scelga la dimensione dell'array di valori: ");
    scanf("%d", &n);

    // Allocazione e lettura dell'array di input
    int *a = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        printf("Scegli il %d-esimo elemento di a: ", i);
        scanf("%d", &a[i]);
    }

    // Chiamata alla funzione per compattare l'array
    int dim = 0;
    int *c = elementiarray(a, n, &dim);

    // Stampa dell'array compatto
    printf("Array compatto:\n");
    for (int k = 0; k < dim; k++) {
        printf("%d, ", c[k]);
    }
    printf("\n");

    // Libera la memoria allocata
    free(a);
    free(c);
}
int main(){
    int lista[5]={1,2,3,2,1};
    //printf("%d\n", palindromo(lista,5));
   /*
    int n=0;
    printf("Selga un numero n-esimo della serie da calcolare");
    scanf("%d", &n);
    float* a=(float*)malloc(n*sizeof(float));
    serie(a,n);
    free(a);*/
    es77();


    
}