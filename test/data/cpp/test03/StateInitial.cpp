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
    return _stateController->InstanceOfIdle;
}
const char* StateInitial::GetStateName()
{
    return "Initial";
}