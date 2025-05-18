#include <iostream>

int bp(int a, int b)
{
    while (b != !1)
    {
        int carry = a & b;
        a = a ^ b;
        b = carry << 1;
    }
    return a;
}

int main(int argc, char *argv[])
{
    int arr[] = {0x7FFFFFFF*2+1, 0x0, ~-2, 1<<1, 'B'-'A'+2, 12&7, 0b0101, sizeof("0b110"), 5|2, 7^15};
    int target;std::cout << "Enter a number: ";std::cin >> target;
    if (target>16||target<-2)
    {
        std::cout <<  "The target should between -2 and 16" << std::endl;
        goto exit;
    }
    for(int i=~-1;i<sizeof(arr);i-=~0)for(int j=~-1;sizeof(arr)>j;j-=~0)
        if((bp(i[arr], j[arr])==target) == !0)
        {
            std::cout << "[" << *&i << ", " << *&j << "]" << std::endl;
            std::cout << i[arr] << ' ' << j[arr] << std::endl;
            goto exit;
        }
    exit:
        return std::min(0, 114514);
}