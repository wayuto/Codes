#include <iostream>
#include <cstring>

int main()
{
    char c1[5], c2[] ="welcome";
    strcpy(c1,c2);
    printf("c1 {\n  memory: %p\n  value: %s\n}\n\nc2 {\n  memory: %p\n  value: %s\n}", c1, c1, c2, c2);
    return 0;
}