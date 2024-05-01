#pragma once
class StateController;
#include "IControllee.h"
#include "BaseState.h"
#include "StateState1.h"
#include "StateState2.h"
#include "StateState21.h"
#include "StateState31.h"
#include "StateState4.h"
class StateController
{
private:
    IControllee* _controllee;
    BaseState* _currentState;
public:
    BaseState* InstanceOfState1;
    BaseState* InstanceOfState2;
    BaseState* InstanceOfState21;
    BaseState* InstanceOfState31;
    BaseState* InstanceOfState4;
    StateController(IControllee* controllee);
    virtual ~StateController();
    bool TryTransitWithoutEvent();
    void TransitEvent2();
    void TransitEvent21();
    void TransitEvent31();
    void TransitEvent42();
    void TransitEvent421();
    void TransitEvent431();
    const char* GetCurrentStateName();
};