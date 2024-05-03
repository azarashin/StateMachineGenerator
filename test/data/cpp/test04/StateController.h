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
public:
    static const int MaxNumberOfStateIDs = 5;
private:
    IControllee* _controllee;
    BaseState* _currentState;
    BaseState* _stateList[MaxNumberOfStateIDs];
    int GetCurrentIdFromState(BaseState* state);
public:
    BaseState* InstanceOfConfiguring;
    BaseState* InstanceOfEscaped;
    BaseState* InstanceOfIdle;
    BaseState* InstanceOfInitial;
    BaseState* InstanceOfNotShooting;
    StateController(IControllee* controllee);
    virtual ~StateController();
    int GetCurrentIdFromStateId(int parentStateId);
    void ResumeState(int parentStateId, int stateId);
    const char* StateName(int parentStateId);
    bool TryTransitWithoutEvent();
    void TransitEscape();
    void TransitEvConfig();
    void TransitGoInTo();
    const char* GetCurrentStateName();
};