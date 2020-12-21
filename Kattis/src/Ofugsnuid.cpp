#include <iostream>
#include <vector>

int main(){
    int l;
    std::cin >> l;
    std::vector<int> v;

    for(int i = 0; i < l; i++){
        int omegaLUL;
        std::cin >> omegaLUL;
        v.push_back(omegaLUL);
    }
    for(int i = v.size() - 1; i >= 0; i--){
        std::cout << v.at(i) << std::endl;
    }
}