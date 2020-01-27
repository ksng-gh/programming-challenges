#include <iostream>
#include <string>

int main(){
    int n;
    int retVal = 0;
    std::cin >> n;

    for(int i = 0; i < n; i++){
        bool add = true;
        std::string s;
        std::cin >> s;
        for(int j = 0; j < s.length(); j++){
            if(s[j] == 'C'){
                if(s[j + 1] == 'D'){
                    add = false;
                    break;
                }
            }
        }
        if (add){
            retVal++;
        }        
    }
    std::cout << retVal;
}