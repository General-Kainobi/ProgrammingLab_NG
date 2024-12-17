#include <stdio.h>
#include <stdlib.h>
#include <math.h>
/*Si considerino due array ordinati E di r > 0 elementi e F di s > 0 elementi, entrambi senza
duplicati e ordinati in modo crescente. Si chiede di implementare in C le seguenti operazioni:
A. Differenza Simmetrica: Elementi presenti in E o in F ma non in entrambi. L’array risultante
deve essere ordinato e senza duplicati.
B. Massimo totale: Calcolare il numero massimo tra tutti gli elementi presenti in entrambi
gli array E e F.
C. Fusione: Creare un nuovo array che contenga gli elementi di E seguiti dagli elementi di
F, mantenendo l’ordine interno di ciascun array ma senza rimuovere i duplicati.*/

int contanondup(int*a,int*b,int n, int m){
    int c=0;
    int l=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if (a[i]==b[j]){
                l=1;
                j=m;
            }
        }if (l==1){c++;}l=0;
    }return (n+m)-(c);
}
int* conc(int*c, int*e,int*f,int n, int m){
    int l=0;
    for (int i=0;i<n;i++){
        c[i]=e[i];
    }
    int b=n;
    for(int j=0;j<m;j++){
        for(int k=0;k<n;k++){
            if(f[j]!=e[k]){
                l=1;
                k=n;
            }
        }if(l==0){c[b]=f[j];b++;}
        l=0;
    }
    return c;
}
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

int*diff_simm(int*e,int*f,int n, int m){
    int l=0;
    int t= contanondup(e,f,n,m);
    int*c =(int*)malloc(t*sizeof(int)); //array con dimensione num di non duplici
    c= conc(c,e,f,n,m);//aggiunge tutto e ad c e poi aggiunge solo gli elementi di b che non sono in a
    c=ordina_a(c,t);
    for(int i=0;i<(t);i++)
        printf("%d\n",c[i]);
}

int sommaarr(int*a,int n){
    int s=0;
    for(int i=0;i<n;i++){
        s+=a[i];
    }return s;
}
int* ordinare(int*a,int n){
    for (int i=0;i<n;i++){
        for (int j=1;j<n-1;j++){
            if(a[j]>a[i]){
                int temp=a[j];
                a[j]=a[i];
                a[i]=a[j];
            }
        }
    }
}
int contak(int*a, int n, int w){
    int c=0;
    for(int k=0;k<n-1;k++){
        int uno= sommaarr(a,k);
        int due= sommaarr(a, k+1);
        int t=due-uno;
        if (uno>=w && w<due){
            c++;
        }
    }return c;
}
int* extract(int*a, int n,int w){
    a=ordinare(a,n);
    int i=0;
    int t= contak(a,n,w);
    int* array_k=(int*)malloc(100*sizeof(int));
    for(int k=0;k<n-1;k++){
        int uno= sommaarr(a,k);
        int due= sommaarr(a, k+1);
        printf("%d\n%d\n", uno,due);
        if (uno>=w && w<due){
            for(int j=0;j<t;j++)
                array_k[i]=a[j]; i++;
        }
    }
    return array_k;
}





int main(){
    int e[4]={1,3,8,9};
    int f[7]={9,10,11,13,14,16,18};
    //int c=contanondup(e,f,9,7);
    //printf("%d\n",c);
    //diff_simm(e,f,9,7);
    int* a=extract(e,4,5);
    for(int i=0;i<contak(e,4,5);i++){
        printf("%d\n", a[i]);
    }
}