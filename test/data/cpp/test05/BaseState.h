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
    virtual void Setup(bool resume, bool deepResume);
    virtual BaseState* TransitEvent2();
    virtual BaseState* TransitEvent21();
    virtual BaseState* TransitEvent31();
    virtual BaseState* TransitEvent42();
    virtual BaseState* TransitEvent421();
    virtual BaseState* TransitEvent431();
    virtual BaseState* TryTransitWithoutEvent();
    void SetupSubState(BaseState* child, bool resume);
    BaseState* CurrentSubState();
    BaseState* TransitBySubState(BaseState* nextState);
    BaseState* TransitForChild(BaseState* child);
    BaseState* OutlineState();
    virtual const char* GetStateName() = 0;
    virtual BaseState* GetParent() = 0;
};