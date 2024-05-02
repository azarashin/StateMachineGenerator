#include "ConsoleOutControllee.h"
#include <stdio.h>
ConsoleOutControllee::ConsoleOutControllee()
{
}
ConsoleOutControllee::~ConsoleOutControllee()
{
}
void ConsoleOutControllee::DoAction2()
{
    printf("Action2\n");
}
void ConsoleOutControllee::DoAction21()
{
    printf("Action21\n");
}
void ConsoleOutControllee::DoAction31()
{
    printf("Action31\n");
}
void ConsoleOutControllee::DoAction42()
{
    printf("Action42\n");
}
void ConsoleOutControllee::DoAction421()
{
    printf("Action421\n");
}
void ConsoleOutControllee::DoAction431()
{
    printf("Action431\n");
}
void ConsoleOutControllee::NoTransition(const char* state, const char* transition)
{
    printf("NoTransition(%s: %s)\n", state, transition);
}
void ConsoleOutControllee::OverTransition(const char* transition)
{
    printf("OverTransition(%s)\n", transition);
}