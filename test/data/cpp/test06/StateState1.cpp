#include "StateState1.h"
StateState1::StateState1(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateState1::~StateState1()
{
}
BaseState* StateState1::TransitAborted()
{
    return 0;
}
BaseState* StateState1::TransitSucceeded()
{
    _stateController->InstanceOfState2->Setup(false, false);
    return _stateController->InstanceOfState2;
}
const char* StateState1::GetStateName()
{
    return "State1";
}
BaseState* StateState1::GetParent()
{
    return 0;
}