#include "StateController.h"
#include <string.h>
StateController::StateController(IControllee* controllee)
{
    _controllee = controllee;
    InstanceOfState1 = new StateState1(this, _controllee);
    InstanceOfState2 = new StateState2(this, _controllee);
    _currentState = InstanceOfState1;
    BaseState* stateList[] = {
        InstanceOfState1,
        InstanceOfState2
    };
    memcpy(_stateList, stateList, sizeof(BaseState*) * MaxNumberOfStateIDs);
}
StateController::~StateController()
{
    delete InstanceOfState1;
    delete InstanceOfState2;
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
    if(state == 0)
    {
        return -1;
    }
    return state->GetStateID();
    }
void StateController::ResumeState(int parentStateId, int stateId)
{
    BaseState* state = 0;
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
    if(_currentState == 0)
    {
        return false;
    }
    BaseState* current = _currentState;
    _currentState = _currentState->TryTransitWithoutEvent();
    if(_currentState != 0)
    {
        _currentState = _currentState->OutlineState();
    }
    return (current != _currentState);
}
void StateController::TransitCommand1()
{
    if(_currentState != 0)
    {
        _currentState = _currentState->TransitCommand1();
        if(_currentState != 0)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("Command1");
    }
}
void StateController::TransitCommand2()
{
    if(_currentState != 0)
    {
        _currentState = _currentState->TransitCommand2();
        if(_currentState != 0)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("Command2");
    }
}
void StateController::TransitCommand3()
{
    if(_currentState != 0)
    {
        _currentState = _currentState->TransitCommand3();
        if(_currentState != 0)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("Command3");
    }
}
const char* StateController::GetCurrentStateName()
{
    if(_currentState == 0)
    {
        return "(end)";
    }
    else
    {
        return _currentState->GetStateName();
    }
}