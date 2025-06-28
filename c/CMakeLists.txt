cmake_minimum_required(VERSION 3.30)
project(c C)

set(CMAKE_C_STANDARD 11)

add_executable(calc calc.c)
add_executable(hammingWeight hammingWeight.c)
add_executable(isPowerOfTwo isPowerOfTwo.c)