#include "morse.h"
#include <fstream>
#include <string>
#include <iostream>


int main(int argc, char *argv[]) {
    morse m;
    if (argv[1]) {
        std::string path_to_file = argv[1];
        std::ifstream file(path_to_file);
        std::string line;
        std::string command;
        if (file.is_open())
            while (getline(file, line)) {
                for (const auto& ch : line) {
                    if (ch == ' ' | ch == '\n')
                        continue;
                    else
                        command += ch;
                }
            }
        else{
            std::cout << "Failed to read file" << std::endl;
            return 1;
        }
        file.close();

        m.exec(command);
    } else 
        while (true) {
            try {
                std::string command;
                std::cout << "> ";
                std::cin >> command;
                m.exec(command);   
            }
            catch(const std::exception& e) {
                std::cerr << e.what() << '\n';
            }
        }
    
    return 0;
}