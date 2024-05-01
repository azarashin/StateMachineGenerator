#pragma once
#include "IControllee.h"
class BaseState
{
private:
    IControllee* _controllee;
    BaseState* _currentSubState;
public:
    BaseState(IControllee* controllee);
    virtual ~BaseState();
    virtual void Setup();
    virtual BaseState* TransitEscape();
    virtual BaseState* TransitEvConfig();
    virtual BaseState* TransitGoInTo();
    virtual BaseState* TryTransitWithoutEvent();
    void SetupSubState(BaseState* child);
    BaseState* CurrentSubState();
    BaseState* TransitBySubState(BaseState* nextState);
    BaseState* TransitForChild(BaseState* child);
    BaseState* OutlineState();
    virtual const char* GetStateName() = 0;
    virtual BaseState* GetParent() = 0;
};