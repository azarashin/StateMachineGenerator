#pragma once
#include "BaseState.h"
#include "StateController.h"
class StateProcessData : public BaseState
{
private:
    StateController* _stateController;
    IControllee* _controllee;
public:
    StateProcessData(StateController* stateController, IControllee* controllee);
    virtual ~StateProcessData();
    virtual const char* GetStateName();
    virtual BaseState* GetParent();
    virtual int GetStateID();
};