cmake_minimum_required(VERSION 3.30)
project(cpp)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)
include_directories(morse)

add_executable(cpp
    morse/morse.cpp
    morse/morse.h
    abs.cpp
    pal.cpp
    point.cpp
    pubpre.cpp
    sum.cpp)
