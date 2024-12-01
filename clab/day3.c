
#include <stdio.h>

int potenza_2(int y){
    printf("%d \n", y);
    if (y==1){
        return 1;
        }
    else if(y==0){
        return 0;}
    printf("%d \n", y);
    return(potenza_2(y/2));
}

int xalla(int x, int n){
    if (n==0){
        return 1;
    }
    else{
        return(x*xalla(x, n-1));
    }

}

int main(){
    int y;
    // printf("%d\n", sommajk(y, 0));
    // potenza_2(y);
    //  xalla(2,y);
}

int sommajk(int k, int i){
    if (k==i){
        return i-1;
    }
    else
        return(k-1+sommajk(k-1, i));
}
