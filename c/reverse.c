#include <stdio.h>
#include <stdbool.h>

long long int reverse(long long int x) {
    long long int tmp = x, result = 0;

    if (x < 10 && x > 0)
        return true;
    while (x != 0) {
        result = result * 10 + (x % 10);
        x /= 10;
    }
    return result;
}

int main () {
    int x = 123;
    int result = reverse(x);
    printf("%d", result);
    return 0;
}