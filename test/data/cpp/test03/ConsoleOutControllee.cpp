#include "ConsoleOutControllee.h"
#include <stdio.h>
ConsoleOutControllee::ConsoleOutControllee()
{
}
ConsoleOutControllee::~ConsoleOutControllee()
{
}
void ConsoleOutControllee::DoAction0()
{
    printf("Action0\n");
}
void ConsoleOutControllee::DoAction1()
{
    printf("Action1\n");
}
void ConsoleOutControllee::DoAction2()
{
    printf("Action2\n");
}
void ConsoleOutControllee::DoAction3()
{
    printf("Action3\n");
}
void ConsoleOutControllee::NoTransition(const char* state, const char* transition)
{
    printf("NoTransition(%s: %s)\n", state, transition);
}
void ConsoleOutControllee::OverTransition(const char* transition)
{
    printf("OverTransition(%s)\n", transition);
}