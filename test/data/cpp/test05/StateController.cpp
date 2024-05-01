#include "StateController.h"
StateController::StateController(IControllee* controllee)
{
    _controllee = controllee;
    InstanceOfState1 = new StateState1(this, _controllee);
    InstanceOfState2 = new StateState2(this, _controllee);
    InstanceOfState21 = new StateState21(this, _controllee);
    InstanceOfState31 = new StateState31(this, _controllee);
    InstanceOfState4 = new StateState4(this, _controllee);
    _currentState = InstanceOfState1;
}
StateController::~StateController()
{
    delete InstanceOfState1;
    delete InstanceOfState2;
    delete InstanceOfState21;
    delete InstanceOfState31;
    delete InstanceOfState4;
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
void StateController::TransitEvent2()
{
    if(_currentState != 0)
    {
        _currentState = _currentState->TransitEvent2();
        if(_currentState != 0)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("Event2");
    }
}
void StateController::TransitEvent21()
{
    if(_currentState != 0)
    {
        _currentState = _currentState->TransitEvent21();
        if(_currentState != 0)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("Event21");
    }
}
void StateController::TransitEvent31()
{
    if(_currentState != 0)
    {
        _currentState = _currentState->TransitEvent31();
        if(_currentState != 0)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("Event31");
    }
}
void StateController::TransitEvent42()
{
    if(_currentState != 0)
    {
        _currentState = _currentState->TransitEvent42();
        if(_currentState != 0)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("Event42");
    }
}
void StateController::TransitEvent421()
{
    if(_currentState != 0)
    {
        _currentState = _currentState->TransitEvent421();
        if(_currentState != 0)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("Event421");
    }
}
void StateController::TransitEvent431()
{
    if(_currentState != 0)
    {
        _currentState = _currentState->TransitEvent431();
        if(_currentState != 0)
        {
            _currentState = _currentState->OutlineState();
        }
    } else {
        _controllee->OverTransition("Event431");
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