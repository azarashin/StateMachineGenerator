#pragma once
#include "BaseState.h"
#include "StateController.h"
class StateState4 : public BaseState
{
private:
    StateController* _stateController;
    IControllee* _controllee;
public:
    StateState4(StateController* stateController, IControllee* controllee);
    virtual ~StateState4();
    virtual const char* GetStateName();
    virtual BaseState* GetParent();
};