#include <iostream>
#include <string>
#include <cassert>
#include <vector>
#include "sqlite3.h"
class Stock
    {
        public:
        Stock(std::string n){ name = n; }
        std::string name;
        double precio; //precio -> precio actual acción
        double bpa_eps; //beneficio por accion_earning per share

        double net_income; //net income o beneficio neto (EN MILLONES)
        double per; //price to earnings -> (precio accion)/(beneficio neto)
        
        std::vector<double> div_ultimos_años;
        double div_yield;
        double av_div;
        double num_year;

        void PER(){this -> per = (this->precio/this->bpa_eps);}
        void Dividendo(); 
                //a.insert(a.end(), b.begin(), b.end());
        void Av_Div();    
    };

int CreateDataBaseOriginal()//int argc, char** argv
    {
        sqlite3* DB2; 
        int exit = 1; 
        //la funcion sqlite3_open devuelve SQLITE_OK si todo va bien, lo que corresponde a 0, y SQLITE_ERROR que coresponde a 1
        //(0) SQLITE_OK
        //(1) SQLITE_ERROR
        exit = sqlite3_open("stocks.db", &DB2); 
        std::cout << exit << "\n";
        if (exit) { 
            std::cerr << "Error open DB " << sqlite3_errmsg(DB2) << std::endl; 
            return (-1); 
        } 
        else
            std::cout << "Opened Database Successfully!" << std::endl; 
        sqlite3_close(DB2); 
        return (0);
    }