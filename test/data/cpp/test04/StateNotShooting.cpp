#include "StateNotShooting.h"

StateNotShooting::StateNotShooting(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateNotShooting::~StateNotShooting()
{
}
BaseState* StateNotShooting::TransitEscape()
{
    _controllee->DoAction3();
    return _stateController->InstanceOfEscaped;
}
const char* StateNotShooting::GetStateName()
{
    return "NotShooting";
}