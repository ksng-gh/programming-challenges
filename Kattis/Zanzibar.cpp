#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>

int main(){
    std::string c;
    getline(std::cin, c);
    int cases = stoi(c);

    for (int i = 0; i < cases; i++){
        int outsiders = 0;

        std::string s;
        getline(std::cin, s);
        std::stringstream ss(s);

        int current;
        int next;
        ss >> current;

        while(current != 0){
            ss >> next;
            if (!(next <= current * 2)){
                outsiders += next - (current * 2);
            }
            current = next;
        }
        
        std::cout << outsiders << std::endl;
    }
}