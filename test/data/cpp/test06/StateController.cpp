#include "StateController.h"
#include <string.h>
StateController::StateController(IControllee* controllee)
{
    _controllee = controllee;
    InstanceOfProcessData = new StateProcessData(this, _controllee);
    InstanceOfState1 = new StateState1(this, _controllee);
    InstanceOfState2 = new StateState2(this, _controllee);
    InstanceOfState3 = new StateState3(this, _controllee);
    InstanceOfState4 = new StateState4(this, _controllee);
    InstanceOflong1 = new Statelong1(this, _controllee);
    InstanceOflong2 = new Statelong2(this, _controllee);
    _currentState = InstanceOfState1;
    BaseState* stateList[] = {
        InstanceOfProcessData,
        InstanceOfState1,
        InstanceOfState2,
        InstanceOfState3,
        InstanceOfState4,
        InstanceOflong1,
        InstanceOflong2
    };
    memcpy(_stateList, stateList, sizeof(BaseState*) * MaxNumberOfStateIDs);
}
StateController::~StateController()
{
    delete InstanceOfProcessData;
    delete InstanceOfState1;
    delete InstanceOfState2;
    delete InstanceOfState3;
    delete InstanceOfState4;
    delete InstanceOflong1;
    delete InstanceOflong2;
}
int StateController::GetCurrentIdFromStateId(int parentStateId)
{
    if(parentStateId == -1)
    {
        return GetCurrentIdFromState(_currentState);
    }
    if(parentStateId < -1 || parentStateId >= MaxNumberOfStateIDs)
    {
        return -1;
    }
    return GetCurrentIdFromState(_stateList[parentStateId]->CurrentSubState());
}
int StateController::GetCurrentIdFromState(BaseState* state)
{
    if(state == nullptr)
    {
        return -1;
    }
    return state->GetStateID();
    }
void StateController::ResumeState(int parentStateId, int stateId)
{
    BaseState* state = nullptr;
    if(stateId >= 0 && stateId < MaxNumberOfStateIDs)
    {
        state = _stateList[stateId];
    }
    if(parentStateId == -1)
    {
        _currentState = state;
        return;
    }
    if(parentStateId < -1 || parentStateId >= MaxNumberOfStateIDs)
    {
        return;
    }
    _stateList[parentStateId]->ResumeSubState(state);
}
const char* StateController::StateName(int parentStateId)
{
    if(parentStateId >= 0 && parentStateId < MaxNumberOfStateIDs)
    {
        return _stateList[parentStateId]->GetStateName();
    }
    return "(None)";
}
bool StateController::TryTransitWithoutEvent()
{
    if(_currentState == nullptr)
    {
        return false;
    }
    BaseState* current = _currentState;
    _currentState = _currentState->TryTransitWithoutEvent();
    if(_currentState != nullptr)
    {
        _currentState = _currentState->OutlineState();
    }
    return (current != _currentState);
}
void StateController::TransitAborted()
{
    if(_currentState != nullptr)
    {
        _currentState = _currentState->TransitAborted();
        if(_currentState != nullptr)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("Aborted");
    }
}
void StateController::TransitDeepResume()
{
    if(_currentState != nullptr)
    {
        _currentState = _currentState->TransitDeepResume();
        if(_currentState != nullptr)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("DeepResume");
    }
}
void StateController::TransitEnoughData()
{
    if(_currentState != nullptr)
    {
        _currentState = _currentState->TransitEnoughData();
        if(_currentState != nullptr)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("EnoughData");
    }
}
void StateController::TransitFailed()
{
    if(_currentState != nullptr)
    {
        _currentState = _currentState->TransitFailed();
        if(_currentState != nullptr)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("Failed");
    }
}
void StateController::TransitNewData()
{
    if(_currentState != nullptr)
    {
        _currentState = _currentState->TransitNewData();
        if(_currentState != nullptr)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("NewData");
    }
}
void StateController::TransitPause()
{
    if(_currentState != nullptr)
    {
        _currentState = _currentState->TransitPause();
        if(_currentState != nullptr)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("Pause");
    }
}
void StateController::TransitResume()
{
    if(_currentState != nullptr)
    {
        _currentState = _currentState->TransitResume();
        if(_currentState != nullptr)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("Resume");
    }
}
void StateController::TransitSucceeded()
{
    if(_currentState != nullptr)
    {
        _currentState = _currentState->TransitSucceeded();
        if(_currentState != nullptr)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("Succeeded");
    }
}
const char* StateController::GetCurrentStateName()
{
    if(_currentState == nullptr)
    {
        return "(end)";
    }
    else
    {
        return _currentState->GetStateName();
    }
}