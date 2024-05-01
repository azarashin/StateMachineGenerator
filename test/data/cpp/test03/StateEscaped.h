#pragma once
#include "BaseState.h"
#include "StateController.h"
class StateEscaped : public BaseState
{
private:
    StateController* _stateController;
    IControllee* _controllee;
public:
    StateEscaped(StateController* stateController, IControllee* controllee);
    virtual ~StateEscaped();
    virtual const char* GetStateName();
    virtual BaseState* GetParent();
};