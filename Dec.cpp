#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int sum_decmail=0;
    int n1,n2,n3,n4;
    cout << "Enter binary number: ";
    cin >> n1>>n2>>n3>>n4;

    sum_decmail=(n1*8)+(n2*4)+(n3*2)+(n4*1);
    /*while (n > 0)
    {
        int digit = n % 10;
        n /= 10;

        // เปลี่ยนเลขฐานสองในแต่ละตำแหน่งเป็นเลขฐานสิบ
        decimal += digit * pow(2, position);
        position++;
    }*/
    cout << "Decimal value of " <<n1<<n2<<n3<<n4<< " = " << sum_decmail<< endl;
    return 0;
}