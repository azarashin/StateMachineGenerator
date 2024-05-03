#pragma once
class StateController;
#include "IControllee.h"
#include "BaseState.h"
#include "StateState1.h"
#include "StateState2.h"
class StateController
{
public:
    static const int MaxNumberOfStateIDs = 2;
private:
    IControllee* _controllee;
    BaseState* _currentState;
    BaseState* _stateList[MaxNumberOfStateIDs];
    int GetCurrentIdFromState(BaseState* state);
public:
    BaseState* InstanceOfState1;
    BaseState* InstanceOfState2;
    StateController(IControllee* controllee);
    virtual ~StateController();
    int GetCurrentIdFromStateId(int parentStateId);
    void ResumeState(int parentStateId, int stateId);
    const char* StateName(int parentStateId);
    bool TryTransitWithoutEvent();
    void TransitCommand1();
    void TransitCommand2();
    void TransitCommand3();
    const char* GetCurrentStateName();
};