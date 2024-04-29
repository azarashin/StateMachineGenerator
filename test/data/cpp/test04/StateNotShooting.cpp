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
    return _stateController->InstanceOfEscaped;
}
BaseState* StateNotShooting::TransitEvConfig()
{
    if(_currentState != 0)
    {
        return _currentState->TransitEvConfig(); 
    }
    return 0; 
}
const char* StateNotShooting::GetStateName()
{
    return "NotShooting";
}