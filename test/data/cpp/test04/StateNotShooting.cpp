#include "StateNotShooting.h"
StateNotShooting::StateNotShooting(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateNotShooting::~StateNotShooting()
{
}
void StateNotShooting::Setup()
{
    _currentState = _stateController->InstanceOfIdle;
}
BaseState* StateNotShooting::TransitEscape()
{
    _controllee->DoAction3();
    _stateController->InstanceOfEscaped->Setup();
    return _stateController->InstanceOfEscaped;
}
BaseState* StateNotShooting::TransitEvConfig()
{
    if(_currentState == 0)
    {
        return 0;
    }
    BaseState* nextState = _currentState->TransitEvConfig();
    if(nextState == 0)
    {
        return nextState;
    }
    BaseState* parentOfNextState = _currentState->GetParent();
    BaseState* parentOfCurrentState = nextState->GetParent();
    if(parentOfNextState != 0 && parentOfCurrentState != 0 && parentOfNextState == parentOfCurrentState)
    {
        return this;
    }
    return nextState;
}
const char* StateNotShooting::GetStateName()
{
    if(_currentState == 0)
    {
        return "NotShooting(end)";
    }
    return _currentState->GetStateName();
}
BaseState* StateNotShooting::GetParent()
{
    return 0;
}