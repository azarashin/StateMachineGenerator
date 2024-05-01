#pragma once
#include "IControllee.h"
class ConsoleOutControllee : public IControllee
{
public:
    ConsoleOutControllee();
    virtual ~ConsoleOutControllee();
    virtual void DoAction2();
    virtual void DoAction21();
    virtual void DoAction31();
    virtual void DoAction42();
    virtual void DoAction421();
    virtual void DoAction431();
    virtual void NoTransition(const char* state, const char* transition);
    virtual void OverTransition(const char* transition);
};