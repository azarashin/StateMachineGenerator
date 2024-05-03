#pragma once
#include "IControllee.h"
class BaseState
{
private:
    IControllee* _controllee;
    BaseState* _currentSubState;
public:
    BaseState(IControllee* controllee);
    virtual ~BaseState();
    virtual void Setup(bool resume, bool deepResume);
    virtual BaseState* TransitAborted();
    virtual BaseState* TransitDeepResume();
    virtual BaseState* TransitEnoughData();
    virtual BaseState* TransitFailed();
    virtual BaseState* TransitNewData();
    virtual BaseState* TransitPause();
    virtual BaseState* TransitResume();
    virtual BaseState* TransitSucceeded();
    virtual BaseState* TryTransitWithoutEvent();
    void SetupSubState(BaseState* child, bool resume);
    BaseState* CurrentSubState();
    BaseState* TransitBySubState(BaseState* nextState);
    BaseState* TransitForChild(BaseState* child);
    BaseState* OutlineState();
    void ResumeSubState(BaseState* subState);
    virtual const char* GetStateName() = 0;
    virtual BaseState* GetParent() = 0;
    virtual int GetStateID() = 0;
};