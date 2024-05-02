#pragma once
#include "IControllee.h"
class ConsoleOutControllee : public IControllee
{
public:
    ConsoleOutControllee();
    virtual ~ConsoleOutControllee();
    virtual void DoSaveResult();
    virtual void NoTransition(const char* state, const char* transition);
    virtual void OverTransition(const char* transition);
};