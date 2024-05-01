#pragma once
#include "BaseState.h"
#include "StateController.h"
class StateState21 : public BaseState
{
private:
    StateController* _stateController;
    IControllee* _controllee;
public:
    StateState21(StateController* stateController, IControllee* controllee);
    virtual ~StateState21();
    virtual void Setup();
    virtual BaseState* TransitEvent421();
    virtual BaseState* TransitEvent431();
    virtual const char* GetStateName();
    virtual BaseState* GetParent();
};