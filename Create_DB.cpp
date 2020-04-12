#include <iostream> 
#include <sqlite3.h> 
 //AL COMPILAR HACER ESTO g++ prueba.cpp -l sqlite3
int main(int argc, char** argv) 
{ 
    sqlite3* DB; 
    int exit = 0; 
    exit = sqlite3_open("stocks.db", &DB); 
  
    if (exit) { 
        std::cerr << "Error open DB " << sqlite3_errmsg(DB) << std::endl; 
        return (-1); 
    } 
    else
        std::cout << "Opened Database Successfully!" << std::endl; 
    sqlite3_close(DB); 
    return (0); 
} 