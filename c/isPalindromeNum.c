#include <stdio.h>
#include <stdbool.h>

bool isPalindromeNum(long long int x) {
    long long int tmp = x, result = 0;

    if (x < 10)
        return (x > 0) ? true : false;
    while (x != 0) {
        result = result * 10 + (x % 10);
        x /= 10;
    }

    return tmp == result ? true : false;
}

int main () {
    int x = 12321;
    bool result = isPalindromeNum(x);
    printf("%d", result);
    return 0;
}