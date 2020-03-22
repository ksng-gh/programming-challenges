#include <iostream>
using namespace std;



void calc(int iterations){

    int base = 2;
    int delta = 1;
    for(int i = 0; i < iterations; i++){
        base += delta;
        delta *= 2;
    }

    cout << base * base;
}

int main(){
    int i;
    cin >> i;
    calc(i);
}