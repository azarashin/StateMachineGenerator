#include "StateController.h"
StateController::StateController(IControllee* controllee)
{
    _controllee = controllee;
    InstanceOfState1 = new StateState1(this, _controllee);
    InstanceOfState2 = new StateState2(this, _controllee);
    _currentState = InstanceOfState1;
}
StateController::~StateController()
{
    delete InstanceOfState1;
    delete InstanceOfState2;
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