#include <iostream>
#include <vector>

//Imprimira un vector de ints que le pasemos como puntero
void ImprimirVector(std::vector<std::string> *vector)
    {
        for (std::string j : *vector)
                {
                    std::cout << j << "\n";
                }
    }