#include <iostream> 
#include <sqlite3.h> 
//g++ createTable.cpp -l sqlite3
int main(int argc, char** argv) 
{ 
    sqlite3* DB; 
    std::string sql = "CREATE TABLE STOCKS("
                      "ID INT PRIMARY KEY     NOT NULL, "
                      "NAME           TEXT    NOT NULL, "
                      "PRECIO          REAL     NOT NULL, "
                      "PER            REAL     NOT NULL, "
                      "ADDRESS        CHAR(50), "
                      "AV_DIVIDEND         REAL );"; 
    int exit = 0; 
    exit = sqlite3_open("stocks.db", &DB); 
    char* messaggeError; 
    exit = sqlite3_exec(DB, sql.c_str(), NULL, 0, &messaggeError); 
  
    if (exit != SQLITE_OK) { 
        std::cerr << "Error Create Table" << std::endl; 
        sqlite3_free(messaggeError); 
    } 
    else
        std::cout << "Table created Successfully" << std::endl; 
    sqlite3_close(DB); 
    return (0); 
}