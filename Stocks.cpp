#include <iostream>
#include <string>
#include <cassert>
#include <vector>
#include "Stocks.h"
#include <sqlite3.h>
//AL COMPILAR HACER ESTO g++ prueba.cpp -l sqlite3


void Stock::Dividendo()
    {
        double div;
        std::cout << "Introduzca dividendos y pulse, del número de años que quiera, cuando ya no quiera, teclee otra cosa\n";
        while(std::cin >> div){
                std::cout << "Introduzca dividendos y pulse, del número de años que quiera, cuando ya no quiera, teclee otra cosa\n";
                this->num_year +=1;
                this->div_ultimos_años.push_back(div);
                }
        
    }
void Stock::Av_Div()
    {
        //std::vector<double> div_ultimos_años=this->div_ultimos_años;
        for (double a : this->div_ultimos_años)
        {
        this->av_div += a;
        }
        this->av_div=this->av_div/this->num_year;
        
        this->div_yield=this->av_div/this->precio*100;
    }   

void CreateDataBase(std::string &name)//int argc, char** argv
    {
        sqlite3* DB; 
        int exit = 1; 
        //la funcion sqlite3_open devuelve SQLITE_OK si todo va bien, lo que corresponde a 0, y SQLITE_ERROR que coresponde a 1
        //(0) SQLITE_OK
        //(1) SQLITE_ERROR
        char char_name[name.size()+1];
        name.copy(char_name,name.size()+1);
        const char* char_name2=name.c_str();
        exit = sqlite3_open(char_name2, &DB); 
        std::cout << "SI exit=0 todo ok, si exit = 1 algo mal | exit = " << exit << "\n";
        
        sqlite3_close(DB); 
        
    }
void CreateTableinDB(std::string &name)
    {
        sqlite3* DB;
        char char_name[name.size()+1];
        name.copy(char_name,name.size()+1);
        sqlite3_open(char_name,&DB);

        std::string sql = "CREATE TABLE STOCKS("
                      "ID INT PRIMARY KEY     NOT NULL, "
                      "NAME           TEXT    NOT NULL, "
                      "PRECIO          REAL     NOT NULL, "
                      "PER            REAL     NOT NULL, "
                      "ADDRESS        CHAR(50), "
                      "AV_DIVIDEND         REAL );";
        int exit = 0;
        char* messaggeError; 
        exit = sqlite3_exec(DB, sql.c_str(), NULL, 0, &messaggeError); 
        sqlite3_close(DB);
    }



int main()
    {   
        //std::string DB_name;
        //std::cout << "Introduzca el nombre de la DB que desea acceder y modificar\n";
        //std::cin >> DB_name;
        Cartera mi_cartera;
        
        //CreateDataBase(DB_name);
        //CreateTableinDB(DB_name);
        
        //std::cout << HOLA <<"\n";

    }
