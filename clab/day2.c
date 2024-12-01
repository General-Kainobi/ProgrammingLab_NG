#include <stdio.h>


    //Funzioni Nec.    
        int fatrl(int n){
            int x = n;
                if (n==0){
                    n=1; 
                }
                else
                    while (x!=1){
                        n=n*(x-1);
                        x--;
                        }
                    return(n);}
        float coefbin(int n, int k){
            float ris;
            ris = fatrl(n)/ (fatrl(k)*(fatrl(n-k)));
            return ris;
    }



void exe5(){
    float ris,n=0;
    float x=1;
    do{
        
        printf("Inserisci un numero(0 per uscire!): ");
        scanf("%f", &x);
        ris+=x;
        n++;
    }while(x!=0);
    printf("Il risultato è %f \n", ris/n );
}

void exe6(){
    float n,m,x=0;
    do{
        printf("Inserisci un numero(0 per uscire!): ");
        scanf("%f", &x);
        if (x>n){ //massimo
            n=x;
        }            
        if (x<m){   //minimo
            m=x;
        }
    }while(x!=0);
    printf("Il masssimo è %f \n", n );
    printf("Il minimo è %f \n", m );

}

void exe7(){
    int n,k;
    float cfb_nk;
    printf("Inserisici un numero n: ");
    scanf("%d", &n);
    printf("Inserisici un numero k: ");
    scanf("%d", &k);
    if (k>n){
        printf("Numeri non validi\n");
        
    }
    cfb_nk = coefbin(n,k);
    printf("Il coefficente binario di %d su %d è %f \n",n , k, cfb_nk);
    }


int main(){
    int scelta;
    printf("Scegli un numero di esercizio: ");
    scanf("%d", &scelta);
    switch(scelta){
        case 1:
            exe5();
        case 2:
            exe6();
        case 3:
            exe7();
        
    }
}
