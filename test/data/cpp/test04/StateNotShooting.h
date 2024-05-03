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
    virtual void Setup(bool resume, bool deepResume);
    virtual BaseState* TransitEscape();
    virtual BaseState* TransitEvConfig();
    virtual const char* GetStateName();
    virtual BaseState* GetParent();
    virtual int GetStateID();
};