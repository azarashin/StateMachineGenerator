#include "ConsoleOutControllee.h"
#include <stdio.h>
ConsoleOutControllee::ConsoleOutControllee()
{
}
ConsoleOutControllee::~ConsoleOutControllee()
{
}
void ConsoleOutControllee::DoSaveResult()
{
    printf("SaveResult\n");
}
void ConsoleOutControllee::NoTransition(const char* state, const char* transition)
{
    printf("NoTransition(%s: %s)\n", state, transition);
}
void ConsoleOutControllee::OverTransition(const char* transition)
{
    printf("OverTransition(%s)\n", transition);
}