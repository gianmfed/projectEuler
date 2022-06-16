#include <stdio.h>

int main(){
    double number = 600851475143;
    double largest_prime_factor = 0;

    for (double i = 2; i < number; i++){
        if (number / i - (int)(number / i) == 0.0){
            largest_prime_factor = i;
        }
    }
    return 1;
}