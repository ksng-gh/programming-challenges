#include <iostream>

int main(){
    int times = 0;
    int calories = 0;
    int counter = 0;

    std::cin >> times;

    for(int i = 0; i < times; i++){    
        std::cin >> calories;

        while(calories > 0){
            counter++;
            calories -= 400;
        }

        std::cout << counter << std::endl;
        counter = 0;
    }

    return 0;
}