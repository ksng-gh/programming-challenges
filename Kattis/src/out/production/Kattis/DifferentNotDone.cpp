#include <iostream>
#include <string>
#include <sstream>

int getabs(int v1);

int main(){

    std::string s;
    std::string s1;
    std::string s2;

    long v1;
    long v2;

    long retVal = 0;

    bool cont = true;

    while(cont){
        std::getline(std::cin, s);
        std::stringstream split(s);

        split >> s1 >> s2;

        for(int i = 0; i < s1.size(); i++){
            v1 = v1 * 10 + s1[i];
        }

        for(int i = 0; i < s2.size(); i++){
            v2 = v2 * 10 + s2[i];
        }

        //v1 = std::atol(s1.c_str());
        //v2 = std::atol(s2.c_str());

        std::cout << v1 << std::endl << v2 << std::endl;

        retVal = getabs(v1 - v2);

        std::cout << retVal << std::endl;

        if(s == "\0"){
            cont = false;
        }

    }
}

int getabs(int v1){
    if(v1 < 0){
        return -v1;
    } else {
        return v1;
    }
}