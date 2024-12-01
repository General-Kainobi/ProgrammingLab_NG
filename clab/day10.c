#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//es 7.1
int* inverti(int *a, int n){
    int m = n-1;
    for(int i=0;i<n/2;i++){
        int tmp=a[i];
        a[i]=a[m];
        a[m]=tmp;
        m--;
    }
    for(int i=0;i<n;i++){
        printf("%d, ", a[i]);
    }
}

//es7.2

int* triangnum(int n){
    int*a=(int*)malloc(n*sizeof(int));
    for(int i=0; i<n;i++){
        int somma=0;
        for(int j=i; j>0;j--){
            somma+=j;
        }
        a[i]= somma;
    }
    for(int i=0;i<n;i++){
        printf("%d, ", a[i]);
    }


}
int somma(int n){
    int somma=0;
    for(int i=n;i>0;i--){
        somma= somma+i;
    }
}
int* triangric(int*a, int n){
    if (n==0){
        return 0;
    }
    else { a[n-1]=somma(n);}
    return triangric(*a, n-1);
}


int divisore(int *a, int n, int m){
    for(int i=0;i<n;i++){
        if (a[i]%m==0){
            return 1;
        }
    }return 0;
}
int check(int a[], int n){
    if (n<0){
        return 0;
    }
    int m=a[n-1];
    if (a[m]%m==0){
        return 1;
        }
    else{return check(*a, n-1);}
    
}


int main(){
    int lista={1,2,6,4,5};
    //inverti(lista, 5);//es 7.1
    //triangric(lista, 5);
    printf("%d\n", check(lista, 5));
}