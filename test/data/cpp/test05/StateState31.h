#pragma once
#include "BaseState.h"
#include "StateController.h"
class StateState31 : public BaseState
{
private:
    StateController* _stateController;
    IControllee* _controllee;
public:
    StateState31(StateController* stateController, IControllee* controllee);
    virtual ~StateState31();
    virtual BaseState* TransitEvent431();
    virtual const char* GetStateName();
    virtual BaseState* GetParent();
    virtual int GetStateID();
};