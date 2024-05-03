#pragma once
#include "BaseState.h"
#include "StateController.h"
class Statelong1 : public BaseState
{
private:
    StateController* _stateController;
    IControllee* _controllee;
public:
    Statelong1(StateController* stateController, IControllee* controllee);
    virtual ~Statelong1();
    virtual BaseState* TransitEnoughData();
    virtual BaseState* TransitNewData();
    virtual const char* GetStateName();
    virtual BaseState* GetParent();
    virtual int GetStateID();
};