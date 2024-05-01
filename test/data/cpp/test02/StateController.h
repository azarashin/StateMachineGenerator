#pragma once
class StateController;
#include "IControllee.h"
#include "BaseState.h"
#include "StateState1.h"
#include "StateState2.h"
class StateController
{
private:
    IControllee* _controllee;
    BaseState* _currentState;
public:
    BaseState* InstanceOfState1;
    BaseState* InstanceOfState2;
    StateController(IControllee* controllee);
    virtual ~StateController();
    bool TryTransitWithoutEvent();
    void TransitCommand1();
    const char* GetCurrentStateName();
};