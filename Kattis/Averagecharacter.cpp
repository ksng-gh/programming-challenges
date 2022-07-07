#include <iostream>
#include <string>
#include <bits/stdc++.h>

int main(){
    int sum = 0;

    std::string s;
    std::getline(std::cin, s);
    int length = s.length();

    for(char& c : s){
        sum += int(c);
    }

    std::cout << char(sum / length);

    return 0;
}