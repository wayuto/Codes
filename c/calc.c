#include <stdio.h>

int main(void) {
	char formula[sizeof(char *)];
	printf("> ");
	scanf("%s", formula);
	unsigned long long int left = 0, right = 0, res;
	char symbol;
	unsigned long long int *n = &left;
	for (char *ptr = &formula[0]; *ptr != '\0'; ptr++) {
		if ('0' <= *ptr && *ptr <= '9') {
			*n = 10 * *n + (*ptr - '0');
		} else if (*ptr == '+' || *ptr == '-' || *ptr == '*' || *ptr == '/') {
			symbol = *ptr;
			n = &right;
		}
	}
	switch (symbol) {
		case '+':
			res = left + right;
			break;
		case '-':
			res = left - right;
			break;
		case '*':
			res = left * right;
			break;
		case '/':
			if (right != 0)
				res = left / right;
			else {
				printf("Error: Divide by Zero\n");
				goto exit;
			}
			break;
		default:
			res = left;
			break;
	}
	printf("%d\n", res);
exit:
	return 0;
}
