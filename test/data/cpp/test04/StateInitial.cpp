#include "StateInitial.h"
StateInitial::StateInitial(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateInitial::~StateInitial()
{
}
BaseState* StateInitial::TransitGoInTo()
{
    _controllee->DoAction0();
    _stateController->InstanceOfNotShooting->Setup(false, false);
    return _stateController->InstanceOfNotShooting;
}
const char* StateInitial::GetStateName()
{
    return "Initial";
}
BaseState* StateInitial::GetParent()
{
    return 0;
}
int StateInitial::GetStateID()
{
    return 3;
}