#include "StateController.h"
#include <string.h>
StateController::StateController(IControllee* controllee)
{
    _controllee = controllee;
    InstanceOfConfiguring = new StateConfiguring(this, _controllee);
    InstanceOfEscaped = new StateEscaped(this, _controllee);
    InstanceOfIdle = new StateIdle(this, _controllee);
    InstanceOfInitial = new StateInitial(this, _controllee);
    InstanceOfNotShooting = new StateNotShooting(this, _controllee);
    _currentState = InstanceOfInitial;
    BaseState* stateList[] = {
        InstanceOfConfiguring,
        InstanceOfEscaped,
        InstanceOfIdle,
        InstanceOfInitial,
        InstanceOfNotShooting
    };
    memcpy(_stateList, stateList, sizeof(BaseState*) * MaxNumberOfStateIDs);
}
StateController::~StateController()
{
    delete InstanceOfConfiguring;
    delete InstanceOfEscaped;
    delete InstanceOfIdle;
    delete InstanceOfInitial;
    delete InstanceOfNotShooting;
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
void StateController::TransitEscape()
{
    if(_currentState != nullptr)
    {
        _currentState = _currentState->TransitEscape();
        if(_currentState != nullptr)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("Escape");
    }
}
void StateController::TransitEvConfig()
{
    if(_currentState != nullptr)
    {
        _currentState = _currentState->TransitEvConfig();
        if(_currentState != nullptr)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("EvConfig");
    }
}
void StateController::TransitGoInTo()
{
    if(_currentState != nullptr)
    {
        _currentState = _currentState->TransitGoInTo();
        if(_currentState != nullptr)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("GoInTo");
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