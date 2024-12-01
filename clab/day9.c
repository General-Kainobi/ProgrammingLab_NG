#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void stamparray(int*a, int n){
    for(int i=0;i<n;i++){
        printf("%d| ", a[i]);
    }
}

int* swap(int *a, int *b){
    int temp = *a;
    *a=*b;
    *b=temp;
}

/* int* ordinalorenzo(int* a, int n){
    int* c=(int*)malloc(n*sizeof(int));
    int k=0, j=n-1, i=1;
    for (int z=0; z<n; z++){  
        if (a[i] < a[j]) {   // <= per valori uguali nei due array
            int temp = a[i];
            a[i-1] = temp;
            temp =a[i];
            i++;
        } else {
            if(j>=0){
                int temp1 = a[j+1];
                a[j+1] = temp1;
                a[j]= temp1;
                i++;
            }
        }k++; 
    }
    return c;

}
*/

int* ordina_a(int c[], int n){
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (c[i] > c[j]) {  // ordina in modo crescente
                int temp = c[i];
                c[i] = c[j];
                c[j] = temp;
            }
        }
    }
    return c;
    }


int* duplici(int c[], int n){
    int*nodup = (int*)malloc((n+1)*sizeof(int));
    c=ordina_a(c, n);
    for(int i=0; i<n;i++){
        if (c[i]!=c[i+1]){
            nodup[i]=c[i];
        }
    }
    return c;
}



int *trovavalore(int*a, int n,int m, int x){
    int k=(m-1)/2;
    if (x<=a[k]){
        if(x==a[k]){ //valore trovato
            return k;// ritorna l'indirizzo
        }return(trovavalore(a, n, k ,x));
    } 
    else{
       if(x==a[n/2+k]){
            return k; 
        }
        return(trovavalore(a, n, (n+k)/2 ,x));
    }

}








int main(){

    int c[10]={1,13,2,45,7,9,8,6,32,55};
    //stamparray(duplici(c ,9),9);
    printf("%d\n", trovavalore(c,10, 10, 32));
}