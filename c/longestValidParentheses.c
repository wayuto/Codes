#include <stdio.h>
#include <string.h>

int longestValidParentheses(char* s) {
    int l = 0, r = 0;
    for (int i = 0; i < strlen(s);i++)
        if (s[i] == '(')
            l++;
        else if (s[i] == ')')
            r++;
    int tmp = (l > r) ? (l - r) : (r - l);
    return (l + r - tmp) / 2;
}

int main () {
    char *s = "(()";
    int result = longestValidParentheses(s);
    printf("%d", result);
    return 0;
}