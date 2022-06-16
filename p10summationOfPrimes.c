/*
    Attenzione al trattamento dei numeri (memoria)
*/

#include <stdio.h>
#include <math.h>

const unsigned int LIM = 2000000;
const unsigned int LIM1 = 100;

int isPrime(unsigned int num){
    int primeCheck = 1;
    unsigned int numsqrt = sqrt(num);
    // printf("%i\n%i\n", num,  numsqrt);
    for (unsigned int i = 2; i <= numsqrt; i++){
        unsigned int division = num % i;
        if (division == 0){
            primeCheck = 0;
            break;
        }
    }
    return primeCheck;
}

int main(){
    // 142913828922 è il risultato esatto

    // 1179908154 è sbagliato perchè int non arriva al risultato esatto

    

    double sumOfPrimes = 2;
    // printf("%f\n", sumOfPrimes);
    for (unsigned int x = 3; x < LIM; x += 2){
        if (isPrime(x)){
            // printf("%f\n", sumOfPrimes);
            sumOfPrimes += x;
        }
    }
    printf("%.0f\n", sumOfPrimes);
}