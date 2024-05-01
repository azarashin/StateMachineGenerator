#include "StateState1.h"
StateState1::StateState1(StateController* stateController, IControllee* controllee) : BaseState(controllee)
{
    _stateController = stateController;
    _controllee = controllee;
}
StateState1::~StateState1()
{
}
BaseState* StateState1::TransitEvent2()
{
    _controllee->DoAction2();
    _stateController->InstanceOfState2->Setup();
    return _stateController->InstanceOfState2;
}
BaseState* StateState1::TransitEvent21()
{
    _controllee->DoAction21();
    _stateController->InstanceOfState21->Setup();
    return _stateController->InstanceOfState21;
}
BaseState* StateState1::TransitEvent31()
{
    _controllee->DoAction31();
    _stateController->InstanceOfState31->Setup();
    return _stateController->InstanceOfState31;
}
const char* StateState1::GetStateName()
{
    return "State1";
}
BaseState* StateState1::GetParent()
{
    return 0;
}