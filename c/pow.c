#include <stdio.h>

double myPow(double x, int n) {
    if (x == 0) 
        return 0; 
    if (n == 0)
        return 1;

    long long N = n;
    if (N < 0) {
        x = 1 / x; 
        N = -N;    
    }

    double res = 1.0;
    while (N > 0) {
        if (N % 2 == 1)
            res *= x;  
        x *= x;
        N /= 2;
    }
    return res;
}

int main () {
    double x = 2.0;
    double result = myPow(x, 2);
    printf("%f", result);
    return 0;
}