#pragma once

#include "IControllee.h"

class BaseState
{
private:
    IControllee* _controllee; 
public:
    BaseState(IControllee* controllee);
    virtual ~BaseState();
    virtual BaseState* TransitCommand1();
    virtual BaseState* TransitCommand2();
    virtual BaseState* TransitCommand3();
    virtual BaseState* TryTransitWithoutEvent();

    virtual const char* GetStateName() = 0;
}; 
