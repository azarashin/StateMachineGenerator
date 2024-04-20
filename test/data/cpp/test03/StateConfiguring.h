#pragma once

#include "BaseState.h"
#include "StateController.h"

class StateConfiguring : public BaseState
{
private:
    StateController* _stateController;
    IControllee* _controllee;
public:
    StateConfiguring(StateController* stateController, IControllee* controllee);
    virtual ~StateConfiguring();
    virtual BaseState* TransitEscape();
    virtual BaseState* TransitEvConfig();
    virtual const char* GetStateName();
};