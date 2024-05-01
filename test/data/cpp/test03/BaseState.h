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
    virtual BaseState* TransitEscape();
    virtual BaseState* TransitEvConfig();
    virtual BaseState* TransitGoInTo();
    virtual BaseState* TryTransitWithoutEvent();
    virtual const char* GetStateName() = 0;
};