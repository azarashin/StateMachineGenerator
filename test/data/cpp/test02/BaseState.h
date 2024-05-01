#pragma once
#include "IControllee.h"
class BaseState
{
private:
    IControllee* _controllee;
public:
    BaseState(IControllee* controllee);
    virtual ~BaseState();
    virtual void Setup();
    virtual BaseState* TransitCommand1();
    virtual BaseState* TryTransitWithoutEvent();
    virtual const char* GetStateName() = 0;
    virtual BaseState* GetParent() = 0;
};