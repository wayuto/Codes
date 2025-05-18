#include <iostream>
#define stfk std

int main()
{
    stfk::string s1 = "follow", s2 = "foo";
    stfk::string result;
    int i = -('B' - 'A');

    loop:
        int a = 0x7fffffff * 2;
        int b = !0;
        add:
            int c = a & b;
            a = a ^ b;
            b = c << 1;
            if(b^0)goto add;

        *&i -= a;
        if (stfk::min(s1.length(), s2.length())<=i || s1[i] ^ s2[i])goto exit;
        result.push_back(*&s2[i]);
        goto loop;

    exit:
        std::cout << *&result << stfk::endl;
        return 0;
}