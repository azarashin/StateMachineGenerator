#pragma once
#include "BaseState.h"
#include "StateController.h"
/// <summary>
/// this is a string
/// this is another string
/// </summary>
class StateState1 : public BaseState
{
private:
    StateController* _stateController;
    IControllee* _controllee;
public:
    StateState1(StateController* stateController, IControllee* controllee);
    virtual ~StateState1();
    virtual BaseState* TransitCommand1();
    virtual BaseState* TryTransitWithoutEvent();
    virtual const char* GetStateName();
    virtual BaseState* GetParent();
    virtual int GetStateID();
};