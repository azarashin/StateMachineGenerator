#pragma once
#include "BaseState.h"
#include "StateController.h"
class StateState2 : public BaseState
{
private:
    StateController* _stateController;
    IControllee* _controllee;
public:
    StateState2(StateController* stateController, IControllee* controllee);
    virtual ~StateState2();
    virtual BaseState* TryTransitWithoutEvent();
    virtual const char* GetStateName();
    virtual BaseState* GetParent();
    virtual int GetStateID();
};