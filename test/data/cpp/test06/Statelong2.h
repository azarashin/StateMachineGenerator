#pragma once
#include "BaseState.h"
#include "StateController.h"
class Statelong2 : public BaseState
{
private:
    StateController* _stateController;
    IControllee* _controllee;
public:
    Statelong2(StateController* stateController, IControllee* controllee);
    virtual ~Statelong2();
    virtual BaseState* TransitEnoughData();
    virtual BaseState* TransitNewData();
    virtual const char* GetStateName();
    virtual BaseState* GetParent();
    virtual int GetStateID();
};