#ifndef MORSE_H
#define MORSE_H

#include <map>
#include <string>
#include <iostream>

class morse {
public:
    std::map<std::string, std::string> morse_table;

    morse() { 
        morse_table = {
            {".-", "a"}, 
            {"-...", "b"}, 
            {"-.-.", "c"}, 
            {"-..", "d"}, 
            {".", "e"}, 
            {"..-.", "f"}, 
            {"--.", "g"}, 
            {"....", "h"}, 
            {"..", "i"}, 
            {".---", "j"}, 
            {"-.-", "k"}, 
            {".-..", "l"}, 
            {"--", "m"}, 
            {"-.", "n"}, 
            {"---", "o"}, 
            {".--.", "p"}, 
            {"--.-", "q"}, 
            {".-.", "r"}, 
            {"...", "s"}, 
            {"-", "t"}, 
            {"..-", "u"}, 
            {"...-", "v"}, 
            {".--", "w"}, 
            {"-..-", "x"}, 
            {"-.--", "y"}, 
            {"--..", "z"},
            {".----", "1"},
            {"..---", "2"},
            {"...--", "3"},
            {"....-", "4"}, 
            {".....", "5"}, 
            {"-....", "6"}, 
            {"--...", "7"}, 
            {"---..", "8"}, 
            {"----.", "9"}, 
            {"-----", "0"},
            {".-.-.-", "."}, 
            {"--..--", ","},
            {"..--..", "?"},  
            {"..--.", "!"}, 
            {"---...", ":"}, 
            {".-..-.", "\""}, 
            {".----.", "'"}, 
            {".---.", "="}, 
            {"_", " "}
        };
    }

    void exec(std::string command);
    void print(std::string str);
};

void morse::print(std::string str) {
    std::cout << str << std::endl;
    str.clear();
}

void morse::exec(std::string code) {
    std::string morse = "";
    std::string str = "";
    for (char ch : code) {
        if (ch == '/') {
            for (const auto& pair : morse_table) {
                if (morse == pair.first) {
                    str += pair.second;
                    break;
                }
            }
            morse.clear();
        } else if (ch == ')') print(str);
        else morse += ch;
    }
}

#endif // MORSE_H