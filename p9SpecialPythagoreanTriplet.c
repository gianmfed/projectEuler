/*
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
*/
#include <stdio.h>
#include <stdbool.h>

bool pythagoreanTriplet(int na, int nb, int nc);

int main(){
    unsigned int abcProduct = 1;
    unsigned int a = 1, b = 2, c = 3;
    for (; a < 1000; a++){
        for (; b < 1000; b++){
            for (; c < 1000; c++){
                if (pythagoreanTriplet(a, b, c)){
                    abcProduct = a * b * c;
                }
            }
            c = b;
        }
        b = a;
    }

    printf("%i", abcProduct);
    return 1;
}

bool pythagoreanTriplet(int na, int nb, int nc){
    if (na + nb + nc == 1000 && na*na + nb*nb == nc*nc){
        return true;
    }
    else {
        return false;
    }
}