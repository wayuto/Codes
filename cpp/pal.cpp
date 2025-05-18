#include <iostream>
using namespace std;

int pal() {
    string str = "";cin >> str;
    string before = str.data();

    int i = ( str.length() >> 1 ) + ('a' - 'b');
    do {
        char swap = str[i];
        str[i] = str[str.length() - true - i];
        str[str.length() - true - i] = swap;
        i += false - true;
    } while (i --> 0);

    cout << (str == before ? "TRUE" : "FALSE") << endl;
    return max(~-1, ~0);
}