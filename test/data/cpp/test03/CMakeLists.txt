cmake_minimum_required(VERSION 3.10)

project(TestSample)

file(GLOB SOURCES ./*.cpp)
file(GLOB HEADERS ./*.h)

add_executable(TestSample ${SOURCES})
