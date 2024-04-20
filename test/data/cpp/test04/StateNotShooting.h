#pragma once

#include "BaseState.h"
#include "StateController.h"

class StateNotShooting : public BaseState
{
private:
    StateController* _stateController;
    IControllee* _controllee;
public:
    StateNotShooting(StateController* stateController, IControllee* controllee);
    virtual ~StateNotShooting();
    virtual BaseState* TransitEscape();
    virtual const char* GetStateName();
};