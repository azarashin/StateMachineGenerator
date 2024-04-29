#pragma once

class StateController;

#include "IControllee.h"
#include "BaseState.h"
#include "StateConfiguring.h"
#include "StateEscaped.h"
#include "StateIdle.h"
#include "StateInitial.h"
#include "StateNotShooting.h"

class StateController
{
private:
    IControllee* _controllee;
    BaseState* _currentState;
public:
    BaseState* InstanceOfConfiguring;
    BaseState* InstanceOfEscaped;
    BaseState* InstanceOfIdle;
    BaseState* InstanceOfInitial;
    BaseState* InstanceOfNotShooting; 
    StateController(IControllee* controllee);
    virtual ~StateController();
    bool TryTransitWithoutEvent();
    void TransitEscape();
    void TransitEvConfig();
    void TransitGoInTo();
    const char* GetCurrentStateName();
};