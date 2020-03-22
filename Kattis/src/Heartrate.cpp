#include <iostream>
#include <stdlib.h>
#include <iomanip>

void calculate(int b, double p){
    double BPM = (60 * b) / p;

    std::cout << std::fixed;
    std::cout << std::setprecision(4);
    std::cout << BPM - 60 / p << " " << BPM << " " << BPM + 60 / p << "\n";
    //printf("%.4f %.4f %.4f", BPM - 60 / p, BPM, BPM + 60 / p);
}

int main(){
    int instances;
    int b;
    double p;
    std::cin >> instances;

    for(int i = 0; i < instances; i++){
        std::cin >> b >> p;
        calculate(b, p);
    }
    
}

