#include <stdio.h>
#include <string.h>

int main(int n) {
    int sum = 0;
	printf("> ");scanf("%d", &n);
    char res[33] = "";
	while (n >= 1) {
		char tmp[2];tmp[0] = (n % 2) + '0';tmp[1] = '\0';
		strcat(res, tmp);
		n /= 2;
	}

	for(int i = 0; i < strlen(res); i++) {
		if (res[i] == '1') {
			sum++;
		}
	}

	printf("%d\n", sum);
    return 0;
}