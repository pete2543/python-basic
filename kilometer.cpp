#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int start, end, sum;
    int h,m,s;
    cout<<endl<<"Data inputs are integer!.";
    cout << "Enter start kilometer: ";
    cin >> start;
    cout << "Enter end kilometer: ";
    cin >> end;
    cout << "Enter time used(hour minute secoud): ";
    cin >> h>>m>>s;
    // คำนวณระยะทางที่รถเคลื่อนที่
    sum = end - start;
    //แปลงเวลา
    float time = h+static_cast<float>(m)/60+static_cast<float>(s)/3600;
    //สูตรคำนวณความเร็วเฉลี่ย
    float avg= sum/time;

    cout << "Car traveled " << sum << " kilometers in " << h << " hrs " << m << " min " << s<< " sec." << endl;
    cout << "Average velocity was " << avg << " kph." << endl;

    return 0;
}