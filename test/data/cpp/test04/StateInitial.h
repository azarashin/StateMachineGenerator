#pragma once
#include "BaseState.h"
#include "StateController.h"
class StateInitial : public BaseState
{
private:
    StateController* _stateController;
    IControllee* _controllee;
public:
    StateInitial(StateController* stateController, IControllee* controllee);
    virtual ~StateInitial();
    virtual BaseState* TransitGoInTo();
    virtual const char* GetStateName();
};