#include <iostream>

bool Calc(double a, double b, int c);

int main(){
    int cases;
    std::cin >> cases;

    for(int i = 0; i < cases; i++){
        double one, two, equals;
        std::cin >> one >> two >> equals;

        if(Calc(one, two, equals)){
            std::cout << "Possible" << std::endl;
        } else {
            std::cout << "Impossible" << std::endl;
        }
    }

    return 0;
}

bool Calc(double a, double b, int c){
    if(a + b == c){
        return true;
    } else if (a * b == c){
        return true;
    } else if (a - b == c){
        return true;
    } else if (b - a == c){
        return true;
    } else if (b / a == c){
        return true;
    } else if (a / b == c){
        return true;
    } else {
        return false;
    }
}

