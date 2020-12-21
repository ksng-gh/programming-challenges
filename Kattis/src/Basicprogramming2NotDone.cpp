#include <iostream>
#include <string>
#include <vector>


std::vector<int> insort(std::vector<int> arr){
    int i = 1;
    while(i < arr.size()){
        int j = i;
        while(j > 0 && arr[j - 1] > arr[j]){
            int temp = arr[j];
            arr[j] = arr[j - 1];
            arr[j - 1] = temp;
            j -= 1;
        }
        i++;
    }
    return arr;
}


std::string opt1(std::vector<int> arr){
    for(int i = 0; i < arr.size() - 1; i++){
        for(int j = i + 1; j < arr.size(); j++){
            if(arr[i] != arr[j] && arr[i] + arr[j] == 7777){
                return "Yes";
                
            }
        }
    }
    return "No";
}

std::string opt2(std::vector<int> arr){
    for(int i = 0; i < arr.size() - 1; i++){
        for(int j = i + 1; j < arr.size(); j++){
            if(arr[i] == arr[j]){
                return "Contains duplicate";
                
            }
        }
    }
    return "Unique";
}

int opt3(std::vector<int> arr){
    int counter = 0; 
    for(int i = 0; i < arr.size() - 1; i++){
        for(int j = i + 1; j < arr.size(); j++){
            if(arr[i] == arr[j]){
                counter++;
            }
        }
        if(counter > arr.size()/2){
            return arr[i];
            
        }
    }
    return -1;
}

std::string opt4(std::vector<int> arr){
    std::vector<int> sorted = insort(arr);
    int l = arr.size() % 2;
    if(l == 1){
        return std::to_string(sorted[sorted.size()/2]);
    } else {
        return std::to_string(sorted[sorted.size()/2 - 1]) + " " + std::to_string(sorted[sorted.size()/2]);
    }
}

std::string opt5(std::vector<int> arr){
    std::vector<int> sorted = insort(arr);
    std::string concat = "";
    for(int i = 0; i < sorted.size(); i++){
        if(sorted[i] > 99 && sorted[i] < 1000){
            concat = concat + std::to_string(sorted[i]) + " ";
        }
    }
    return concat.erase(concat.length() - 1);
}

int main(){
    int content, option, input;
    std::cin >> content >> option;
    std::vector<int> arr;

    for(int i = 0; i < content; i++){
        std::cin >> input;
        arr.push_back(input);
    }

    if(option == 1){
        std::cout << opt1(arr);
    } else if (option == 2)
    {
        std::cout << opt2(arr);
    } else if (option == 3)
    {
        std::cout << opt3(arr);
    } else if (option == 4)
    {
        std::cout << opt4(arr);
    } else {
        std::cout << opt5(arr);
    }
   
    
    return 0;
}

