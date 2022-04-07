#include <iostream>

int main(){
    int times;
    std::cin >> times;

    for(int i = 0; i < times; i++){
        int day, days;
        int candles = 0;
        std::cin >> day >> days;

        for(int j = 0; j < days; j++){
            candles += (j + 2);
        }
        std::cout << day << " " << candles << std::endl;
    }
}