#pragma once
#include "BaseState.h"
#include "StateController.h"
class StateState3 : public BaseState
{
private:
    StateController* _stateController;
    IControllee* _controllee;
public:
    StateState3(StateController* stateController, IControllee* controllee);
    virtual ~StateState3();
    virtual void Setup(bool resume, bool deepResume);
    virtual BaseState* TransitAborted();
    virtual BaseState* TransitFailed();
    virtual BaseState* TransitPause();
    virtual BaseState* TransitSucceeded();
    virtual BaseState* TransitEnoughData();
    virtual BaseState* TransitNewData();
    virtual const char* GetStateName();
    virtual BaseState* GetParent();
    virtual int GetStateID();
};