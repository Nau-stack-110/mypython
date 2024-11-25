#include <iostream>
#include <string>
#include <map>
using namespace std;

int main()
{
    string s;
    map<char,int> a;
    cin >> s;
    cin.ignore();

    for (auto x:s){
        a[x]+=1;
    }
    cout << a['A'] << " " << a['C'] << " " << a['G'] << " " << a['T'];
}
