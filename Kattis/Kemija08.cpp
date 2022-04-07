#include <iostream>
#include <string>

int main(){
    std::string sentence;
    std::string renewed;
    std::getline(std::cin, sentence);

    for(int i = 0; i < sentence.size(); i++){
        if(sentence.at(i) == 'a' || sentence.at(i) == 'e' || sentence.at(i) == 'i' || sentence.at(i) == 'o' || sentence.at(i) == 'u'){
            renewed += sentence.at(i);
            i = i + 2;
        } else {
            renewed += sentence.at(i);
        }
    }

    std::cout << renewed;
    return 0;
}

