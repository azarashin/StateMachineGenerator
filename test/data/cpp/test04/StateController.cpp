#include "StateController.h"

StateController::StateController(IControllee* controllee)
{
    _controllee = controllee;
    InstanceOfConfiguring = new StateConfiguring(this, _controllee);
    InstanceOfEscaped = new StateEscaped(this, _controllee);
    InstanceOfIdle = new StateIdle(this, _controllee);
    InstanceOfInitial = new StateInitial(this, _controllee);
    InstanceOfNotShooting = new StateNotShooting(this, _controllee);
    _currentState = InstanceOfInitial;
}
StateController::~StateController()
{
    delete InstanceOfConfiguring;
    delete InstanceOfEscaped;
    delete InstanceOfIdle;
    delete InstanceOfInitial;
    delete InstanceOfNotShooting;
}
bool StateController::TryTransitWithoutEvent()
{
    if(_currentState == 0)
    {
        return false;
    }
    BaseState* current = _currentState;
    _currentState = _currentState->TryTransitWithoutEvent();
    return (current != _currentState);
}
void StateController::TransitEscape()
{
    if(_currentState != 0)
    {
        _currentState = _currentState->TransitEscape();
    } else {
        _controllee->OverTransition("Escape");
    }
}
void StateController::TransitEvConfig()
{
    if(_currentState != 0)
    {
        _currentState = _currentState->TransitEvConfig();
    } else {
        _controllee->OverTransition("EvConfig");
    }
}
void StateController::TransitGoInTo()
{
    if(_currentState != 0)
    {
        _currentState = _currentState->TransitGoInTo();
    } else {
        _controllee->OverTransition("GoInTo");
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