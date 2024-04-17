#include "ConsoleOutControllee.h"
#include <stdio.h>

ConsoleOutControllee::ConsoleOutControllee()
{

}
ConsoleOutControllee::~ConsoleOutControllee()
{

}
void ConsoleOutControllee::DoAction1()
{
    printf("Action1");
}
void ConsoleOutControllee::DoAction2()
{
    printf("Action2");
}
void ConsoleOutControllee::DoAction3()
{
    printf("Action3");
}
void ConsoleOutControllee::NoTransition(const char* state, const char* transition)
{
    printf("NoTransition(%s: %s)", state, transition);
}

void ConsoleOutControllee::OverTransition(const char* transition)
{
    printf("OverTransition(%s)", transition);
}
