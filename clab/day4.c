#include <stdio.h>



float aric(int n){
float y;
if(n==1){
    return(0.5);
}else{
    y = ((aric(n-1) +1.0)*0.5);
    printf("%f\n", y);
    return (y);}
}


float aiter(float n){
    float tot=0.5;
    for(int i=n; i>1; i--){
        tot=((tot+1.0)*0.5);
    }
    printf("%f\n", tot);
    return tot;

}



float sricor(float n){
    if(n==0){
        return 1.0;
    }
    else if(n==1){
        return 3.0;
    }
    else
    return((sricor(n-1.0)+3.0)*(1.0/(2.0*n))+sricor(n-2.0));
}

float siter(float n){
    float n0 = 1.0;
    float n1 = 3.0;
    if(n==0){return n0;}
    if(n==1){return n1;}
    for (int i=n; i!=0; i--){
        float j=n1;
        n1=((n1+3)/(2*i)+n1);
       n0=j;
    }
    return (n1);

}



int main(){
    
    //printf("%f \n", aric(10));
    //printf("%f \n", aiter(10));
    printf("%f \n", sricor(2.0));
    printf("%f \n", siter(2.0));



}