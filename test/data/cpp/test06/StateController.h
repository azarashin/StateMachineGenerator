#pragma once
class StateController;
#include "IControllee.h"
#include "BaseState.h"
#include "StateProcessData.h"
#include "StateState1.h"
#include "StateState2.h"
#include "StateState3.h"
#include "StateState4.h"
#include "Statelong1.h"
#include "Statelong2.h"
class StateController
{
public:
    static const int MaxNumberOfStateIDs = 7;
private:
    IControllee* _controllee;
    BaseState* _currentState;
    BaseState* _stateList[MaxNumberOfStateIDs];
    int GetCurrentIdFromState(BaseState* state);
public:
    BaseState* InstanceOfProcessData;
    BaseState* InstanceOfState1;
    BaseState* InstanceOfState2;
    BaseState* InstanceOfState3;
    BaseState* InstanceOfState4;
    BaseState* InstanceOflong1;
    BaseState* InstanceOflong2;
    StateController(IControllee* controllee);
    virtual ~StateController();
    int GetCurrentIdFromStateId(int parentStateId);
    void ResumeState(int parentStateId, int stateId);
    const char* StateName(int parentStateId);
    bool TryTransitWithoutEvent();
    void TransitAborted();
    void TransitDeepResume();
    void TransitEnoughData();
    void TransitFailed();
    void TransitNewData();
    void TransitPause();
    void TransitResume();
    void TransitSucceeded();
    const char* GetCurrentStateName();
};