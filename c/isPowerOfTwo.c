#include <stdio.h>
#include <string.h>

int main() {
    int n = 16;
    char bin[33] = "";
    int ipot = 0;
    while (n >= 1) {
        char tmp[2];tmp[0] = (n % 2) + '0';tmp[1] = '\0';
        strcat(bin, tmp);
        n /= 2;
    }
    for (int i = 0;i<strlen(bin);i++) {
        if(bin[i]=='1')ipot++;
    }
    if (ipot==1)
        printf("YES\n");
    else
        printf("NO\n");
}