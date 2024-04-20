#pragma once

#include "IControllee.h"

class ConsoleOutControllee : public IControllee
{
public:
    ConsoleOutControllee();
    virtual ~ConsoleOutControllee();
    virtual void DoAction0();
    virtual void DoAction1();
    virtual void DoAction2();
    virtual void DoAction3();
    virtual void NoTransition(const char* state, const char* transition);
    virtual void OverTransition(const char* transition);
};