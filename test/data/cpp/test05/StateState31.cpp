#include "StateState31.h"
StateState31::StateState31(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateState31::~StateState31()
{
}
BaseState* StateState31::TransitEvent431()
{
    _controllee->DoAction431();
    _stateController->InstanceOfState4->Setup(false, false);
    return _stateController->InstanceOfState4;
}
const char* StateState31::GetStateName()
{
    return "State2.State21.State31";
}
BaseState* StateState31::GetParent()
{
    return _stateController->InstanceOfState21;
}
int StateState31::GetStateID()
{
    return 3;
}