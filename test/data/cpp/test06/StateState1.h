#pragma once
#include "BaseState.h"
#include "StateController.h"
class StateState1 : public BaseState
{
private:
    StateController* _stateController;
    IControllee* _controllee;
public:
    StateState1(StateController* stateController, IControllee* controllee);
    virtual ~StateState1();
    virtual BaseState* TransitAborted();
    virtual BaseState* TransitSucceeded();
    virtual const char* GetStateName();
    virtual BaseState* GetParent();
};