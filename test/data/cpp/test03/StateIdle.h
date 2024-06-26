#pragma once
#include "BaseState.h"
#include "StateController.h"
class StateIdle : public BaseState
{
private:
    StateController* _stateController;
    IControllee* _controllee;
public:
    StateIdle(StateController* stateController, IControllee* controllee);
    virtual ~StateIdle();
    virtual BaseState* TransitEvConfig();
    virtual const char* GetStateName();
    virtual BaseState* GetParent();
    virtual int GetStateID();
};