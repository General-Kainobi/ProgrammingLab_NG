#include <stdio.h>

float sit(int n){
    int s1=0;
    int s2=0;
    int sm;
    for(int i=3; i<n+1; i++){
        if (s1/2 >=3*s2){
            sm=(s2*s1)/i;
        }
        else{
            sm=(s2+s1)/i;}
    s2=s1;
    s1=sm;
    printf("s-1= %d\n s-2= %d\n sm= %d\n",s1,s2,sm);
    return sm;
    }
}


float F_jk(int j, int k){
    int i=j;
    if (k==i){
        return(sit(k));
    }
    return(sit(k)*F_jk(i, k-1));

}

int main(){
    sric(5);
    return 0;
}