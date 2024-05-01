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
    printf("Action2");
}
void ConsoleOutControllee::DoAction21()
{
    printf("Action21");
}
void ConsoleOutControllee::DoAction31()
{
    printf("Action31");
}
void ConsoleOutControllee::DoAction42()
{
    printf("Action42");
}
void ConsoleOutControllee::DoAction421()
{
    printf("Action421");
}
void ConsoleOutControllee::DoAction431()
{
    printf("Action431");
}
void ConsoleOutControllee::NoTransition(const char* state, const char* transition)
{
    printf("NoTransition(%s: %s)", state, transition);
}
void ConsoleOutControllee::OverTransition(const char* transition)
{
    printf("OverTransition(%s)", transition);
}